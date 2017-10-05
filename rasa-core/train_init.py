from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from policy import PssPolicy
from rasa_dm.agent import Agent
from rasa_dm.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")

    training_data_file = './data/stories.md'
    model_path = './models/model/'

    agent = Agent("./pss_domain.yml",
                  policies=[MemoizationPolicy(), PssPolicy()])

    agent.train(
        training_data_file,
        max_history=5,
        epochs=100,
        batch_size=5,
        validation_split=0.1
    )

    agent.persist(model_path)
