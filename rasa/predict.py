from __future__ import unicode_literals
from rasa_nlu.model import Metadata,Interpreter
from rasa_nlu.config import RasaNLUConfig
import sys
import json

"""
	states --> [
			{
				entities: {name:value}
				intent:intent
			}
	]
"""

states = []

def extract_info(json_data):
	dicti = {
			'entities':[],
			'intent':'unknown'
	}
	already_existing=dicti
	if len(states) > 0:
		already_existing = states.pop()
	if 'entities' in json_data:
		for entity in json_data['entities']:
			ent = entity['entity']
			ent_value = entity['value']
			dicti['entities'].append({ent:ent_value})
	if 'intent' in json_data:
		dicti['intent']=json_data['intent']['name']
	if already_existing['intent'] == dicti['intent']:
		# Not merging intent right now.
		states.append(already_existing)
		return dicti
	states.append(already_existing)
	states.append(dicti)
	return dicti

if len(sys.argv) != 3:
	print("Incorrect amount of input parameters")
	print("python predict.py <CONFIG_FILE> <MODEL_DIR_NAME>")
	sys.exit(1)

config_to_use = sys.argv[1]
model_to_use = sys.argv[2]

model_directory = 'models/'+model_to_use
metadata = Metadata.load(model_directory)

interpreter = Interpreter.load(metadata,RasaNLUConfig(config_to_use))

while True:
	question = raw_input("Me:")
	json_data=interpreter.parse(question.decode('utf-8'))
	extract_info(json_data)
	print states

