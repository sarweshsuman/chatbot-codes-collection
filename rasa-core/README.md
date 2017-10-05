# Rasa Core Sample Implementation

Rasa Core is a framework which enables us to build a chatbot which is able maintain context and respond to user queries. It is a very flexible framework. It allows us to use any nlu interpreter we want to use, it allows us to connect to external services to pull in the information on user request. We can do lot of things with this framework.

In this implementation you will see I train some stories and use rasa-nlu as interpreter. I am also connecting to postgres in one of the stories. I am also deploying a software to tomcat when the user request it. I maintain context via slots all throughout the conversation.

To train the rasa-core model,

python train_init.py

To start the conversation,

python run.py <CONFIG_PATH> <INTERPRETER_MODEL_PATH>
