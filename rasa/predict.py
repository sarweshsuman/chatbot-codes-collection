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
	global states
	current_state = {
			'entities':{},
			'intent':'unknown'
	}
	
	# Extracting state from current message

	if 'entities' in json_data:
		for entity in json_data['entities']:
			ent = entity['entity']
			ent_value = entity['value']
			current_state['entities'][ent]=ent_value
	if 'intent' in json_data:
		current_state['intent']=json_data['intent']['name']

	# State extraction complete

	if len(states) == 0:
		print("First state")
		states.append(current_state)
		return current_state

	new_states = []
	state_index=len(states) - 1
	matched=False

	while len(states) > 0:
		state = states.pop()
		if state['intent'] == current_state['intent']:
			matched=True
			for ent in current_state['entities']:
				state['entities'][ent]=current_state['entities'][ent]
			new_states.append(state)
			break
		# expire old states here
		new_states.insert(0,state)
		state_index -= 1
	while len(states) > 0:
		state = states.pop()
		# expire old states here
		new_states.insert(0,state)
	
	if matched == False:
		# None of the state was matched
		new_states.append(current_state)
	states = new_states
	return current_state

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
	current_state=extract_info(json_data)
	print("Total state {}\nCurrent state {}".format(states,current_state))
