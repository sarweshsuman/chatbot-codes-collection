# Rasa NLU Sample Implementation

Rasa-NLU provides two models out of the box,
- MITIE
- SpaCy + sklearn
We can use combinations in following ways,
 - MITIE + sklearn
 - SpaCy _ sklearn
> Performance of these models varies depending on the domain and dataset.

## This is implementation of intent classification and entity extraction using rasa framework

Usage pattern

```
python predict.py ./config_mitie.json model_20170908-063537_MITIE
```

**Dataset is not uploaded to github**

Context is created as an stack of states variable.
> This is sample implementation, but incase you are using rasa-core then context implementation can be done via slots.

states variable stores dictionary of {entities:{},intent:}

algorithm is

```
extract entity and intent from message

if it is first message then push to stack by default

if not, then check with which previous state, current extracted state matches,

if match found then bring that state to the top of the stack, also update the entities ( if new entities are present then it will add it to the state and old entities values will be overriden )

if no match is found then current state is new state hence push it to the top of the stack.

Next to generate response current_state and top of the stack state can be used. 

Current state might not have any entities but top of the stack state might have entities which can be used to generate response.
```

To train rasa-nlu

```
python -m rasa_nlu.train -c ./config_spacy.json
```
