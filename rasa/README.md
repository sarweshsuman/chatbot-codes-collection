This is implementation of intent classification and entity extraction using rasa framework

Usage pattern

python predict.py ./config_mitie.json model_20170908-063537_MITIE

Data set is not uploaded to github

Context is created as an stack of states variable.

states variable stores dictionary of {entities:{},intent:}

algorithm is

extract entity and intent from message

if it is first message then push to stack by default

if not, then check with which previous state, current extracted state matches,

if match found then bring that state to the top of the stack, also update the entities ( if new entities are present then it will add it to the state and old entities values will be overriden )

if no match is found then current state is new state hence push it to the top of the stack.

Next to generate response current_state and top of the stack state can be used. 

Current state might not have any entities but top of the stack state might have entities which can be used to generate response.

