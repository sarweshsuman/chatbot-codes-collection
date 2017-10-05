from rasa_nlu.model import Metadata,Interpreter
from rasa_nlu.config import RasaNLUConfig
import sys

from rasa_dm.util import one_hot
import numpy as np
from rasa_dm.policies import Policy
from rasa_dm.agent import Agent
from rasa_dm.domain import TemplateDomain
from rasa_dm.policies.memoization import MemoizationPolicy
from rasa_dm.channels.console import ConsoleInputChannel
from rasa_dm.tracker_store import InMemoryTrackerStore
from rasa_dm.actions.action import ACTION_LISTEN_NAME

import logging
logger = logging.getLogger(__name__)
logger.setLevel(10)

class SimplePolicy(Policy):
    def predict_action_probabilities(self, tracker, domain):
        # type: (DialogueStateTracker, Domain) -> List[float]
        if tracker.latest_action_id_str == ACTION_LISTEN_NAME:
            print(tracker.latest_message.entities)
            key = tracker.latest_message.intent["name"]
            action = domain.action_map['action_'+key][0]
            return one_hot(action, domain.num_actions)
        else:
            print("in else part")
            return np.zeros(domain.num_actions)

full_config_path = "/home/cdpai/online_implementation_of_chatbot/rasa/config_spacy.json"
full_model_path = "/home/cdpai/online_implementation_of_chatbot/rasa/models/model_20170918-060638"

metadata = Metadata.load(full_model_path)
interpreter1 = Interpreter.load(metadata,RasaNLUConfig(full_config_path))
domain=TemplateDomain.load("pss_domain.yml")
tracker = InMemoryTrackerStore(domain)
agent = Agent.load("./models/model",interpreter=interpreter1,tracker_store=tracker)

#agent = Agent(domain,policies=[SimplePolicy()],interpreter=interpreter1,tracker_store=tracker)
agent.handle_channel(ConsoleInputChannel())

