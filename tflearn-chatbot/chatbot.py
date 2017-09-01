# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 23:38:07 2017

@author: BGH47373
"""

TRAINING_DATA_PATH=r'C:\Users\bgh47373\Documents\Chatbot-Codes\dataset\chatbot-aricent-dot-com'

import tflearn
import tensorflow as tf

import os
import nltk
import random
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

files = os.listdir(TRAINING_DATA_PATH)

words = []
classes = []
documents = []

for fn in files:
    FILE_NAME=os.path.join(TRAINING_DATA_PATH,fn)
    fh=open(FILE_NAME)
    lines=fh.readlines()
    fh.close()
    for ln in lines:
        local_words = word_tokenize(ln)
        words.extend(local_words)
        new_words= [w for w in local_words if w not in ['?']]
        documents.append((new_words,fn))

words = [stemmer.stem(w.lower()) for w in words]
words = sorted(list(set(words)))

classes = sorted(list(files))

print(classes)

# Creating bag of words representation
# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)

# create train and test lists
train_x = list(training[:,0])
train_y = list(training[:,1])
print(train_x[:5])
print(train_y[:5])


# reset underlying graph data
tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training (apply gradient descent algorithm)
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')



# Now lets predict some

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))
    

p = bow("Who are you ELTs?", words)

import pickle
# saving words classes in order so that later prediction can be made on this.
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" ) )

""" Till here we generated intent """"

