from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_dm.policies.keras_policy import KerasPolicy

logger = logging.getLogger(__name__)


class PssPolicy(KerasPolicy):
    def _build_model(self, num_features, num_actions, max_history_len):
        """Build a keras model and return a compiled model.
        :param max_history_len: The maximum number of historical turns used to decide on next action"""
        from keras.layers import Activation, Masking, Dense, SimpleRNN
        from keras.models import Sequential

        n_hidden = 8  # size of hidden layer in RNN
        # Build Model
        model = Sequential()
        model.add(Masking(-1, batch_input_shape=(None, max_history_len, num_features)))
        model.add(SimpleRNN(n_hidden, batch_input_shape=(None, max_history_len, num_features)))
        model.add(Dense(input_dim=n_hidden, output_dim=num_actions))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        logger.debug(model.summary())
        return model

