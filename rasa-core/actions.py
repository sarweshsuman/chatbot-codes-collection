from rasa_dm.actions.action import Action
from rasa_dm.events import SetSlot
import psycopg2
import os
import sys
import time

class DeployToTomcat:
	def __init__(self):
		self.tomcat_deployment_location=os.path.join(os.environ['TOMCAT_HOME'],'webapps')
		self.tomcat_script_to_start=os.path.join(os.environ['TOMCAT_HOME'],'bin','startup.sh')
		self.tomcat_script_to_stop=os.path.join(os.environ['TOMCAT_HOME'],'bin','shutdown.sh')
	def deploy(self,software_name,software_version,source_location):
		expected_full_software_name=software_name+'-'+str(software_version)+'.tar'
		expected_full_software_path = os.path.join(source_location,expected_full_software_name)
		if os.path.isfile(expected_full_software_path) == False:
			return (False,"File {} not found".format(expected_full_software_path))
		os.system("cp {} {}".format(expected_full_software_path,self.tomcat_deployment_location))
		new_full_software_deployed_path=os.path.join(self.tomcat_deployment_location,expected_full_software_name)
		os.system("tar xvf {} -C {} ".format(new_full_software_deployed_path,self.tomcat_deployment_location))
		os.system(self.tomcat_script_to_stop)
		time.sleep(5)
		os.system(self.tomcat_script_to_start)
		return (True,"Deployment successful")

class PostgresClient:
	def __init__(self):
		self.query1="select distinct configuration_id from software where software_name='SOFTWARE_NAME' and software_version='SOFTWARE_VERSION'" 
		self.query2="select configuration_name from configuration where configuration_id=CONFIGURATION_ID and mandatory='Y'"
		# To connect to postgres, insert dbname,user,password
		self.connection_client=psycopg2.connect("dbname='<>' user='<>' host='localhost' password='<>")
		self.cursor = self.connection_client.cursor()

	def get_list_of_configuration_name(self,software_name,software_version):
		query1=self.query1
		query2=self.query2
		query1=query1.replace('SOFTWARE_NAME',software_name)
		query1=query1.replace('SOFTWARE_VERSION',software_version)
		self.cursor.execute(query1)
		results=self.cursor.fetchall()
		if len(results) > 1:
			print("Problem with configuration in 'software' table, more than one row in software table with name {} and version {}".format(software_name,software_version))
		if len(results) == 0:
			print("Missing configuration in 'software' table, no row in software table with name {} and version {}".format(software_name,software_version))
			return []
		config_id = results[0][0]
		#print(config_id)
		query2=query2.replace('CONFIGURATION_ID',str(config_id))
		self.cursor.execute(query2)
		results=self.cursor.fetchall()
		to_return=[]
		for res in results:
			to_return.append(res[0])
		return to_return
			
class ActionFetchProductInformation(Action):
    @classmethod
    def name(cls):
        return 'product_information'

    @classmethod
    def run(cls, dispatcher, tracker, domain):
	software_version = tracker.get_slot("software_version")
	software_name = tracker.get_slot("software_name")
	whatisrequired = tracker.get_slot("whatisrequired")
	to_return=[]
	if software_name is None:
		software_name=dispatcher.utter_expecting_response_message("what is the software name?")
		to_return.append(SetSlot("software_name",software_name))
	if software_version is None:
		software_version=dispatcher.utter_expecting_response_message("what is the software version?")
		to_return.append(SetSlot("software_version",software_version))

        dispatcher.utter_message("{} for software {} version {} is DUMMY VARIABLE 1 DUMMY VARIABLE 2".format(whatisrequired,software_name,software_version))
        return to_return
		
class ActionSaveToSlots(Action):
    @classmethod
    def name(cls):
        return 'save_to_slots'

    @classmethod
    def run(cls, dispatcher, tracker, domain):
	return_value=[]
	#print(tracker.latest_message.intent)
	entities = tracker.latest_message.entities
	for ent in entities:
		#print(ent['entity'],ent['value'])
		return_value.append(SetSlot(ent['entity'],ent['value']))
        return return_value

class ActionProductDeployment(Action):
    @classmethod
    def name(cls):
        return 'product_deployment'

    @classmethod
    def run(cls, dispatcher, tracker, domain):
	#print(tracker.latest_message.intent)

	software_version = tracker.get_slot("software_version")
	software_name = tracker.get_slot("software_name")
	source_location = tracker.get_slot("source_location")
	destination_location = tracker.get_slot("destination_location")

	to_return=[]
	if software_name is None:
		software_name=dispatcher.utter_expecting_response_message("what is the software name?")
		to_return.append(SetSlot("software_name",software_name))
	if software_version is None:
		software_version=dispatcher.utter_expecting_response_message("what is the software version?")
		to_return.append(SetSlot("software_version",software_version))
	if source_location is None:
		source_location=dispatcher.utter_expecting_response_message("what is the source_location?")
		to_return.append(SetSlot("source_location",source_location))
	if destination_location is None:
		destination_location=dispatcher.utter_expecting_response_message("what is the destination_location?")
		to_return.append(SetSlot("destination_location",destination_location))

	client=PostgresClient()
	config_lists=client.get_list_of_configuration_name(software_name,software_version)
	configurations=[]
	if len(config_lists) != 0:
		dispatcher.utter_message("There are some configurations that are needed to proceed..")
		for config in config_lists:
			configurations.append((config,dispatcher.utter_expecting_response_message(config+"?")))
		dispatcher.utter_message("Proceeding with configurations {}".format(configurations))
	else:
		dispatcher.utter_message("There are no configurations defined, will try to deploy with information we have")

	deploy = DeployToTomcat()
	resp=deploy.deploy(software_name,software_version,source_location)
	dispatcher.utter_message("Deployment status {}".format(resp))
        return to_return
