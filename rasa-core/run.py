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
import sys

import logging
logger = logging.getLogger(__name__)
logger.setLevel(10)

full_config_path = sys.argv[1]
full_model_path = sys.argv[2]

metadata = Metadata.load(full_model_path)
interpreter1 = Interpreter.load(metadata,RasaNLUConfig(full_config_path))
domain=TemplateDomain.load("pss_domain.yml")
tracker = InMemoryTrackerStore(domain)
agent = Agent.load("./models/model",interpreter=interpreter1,tracker_store=tracker)

#agent = Agent(domain,policies=[SimplePolicy()],interpreter=interpreter1,tracker_store=tracker)
agent.handle_channel(ConsoleInputChannel())

