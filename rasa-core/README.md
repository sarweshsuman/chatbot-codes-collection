# Rasa Core Sample Implementation

Rasa Core is a framework which enables us to build a chatbot which is able maintain context and respond to user queries. It is a very flexible framework. It allows us to use any nlu interpreter we want to use, it allows us to connect to external services to pull in the information on user request. We can do lot of things with this framework.

In this implementation you will see I train some stories and use rasa-nlu as interpreter. I am also connecting to postgres in one of the stories. I am also deploying a software to tomcat when the user request it. I maintain context via slots all throughout the conversation.

To train the rasa-core model,

```
python train_init.py
```

To start the conversation,

```
python run.py <CONFIG_PATH> <INTERPRETER_MODEL_PATH>
```

Sample output 1

### In this output deployment fails
```
Bot loaded. Type a message and press enter :
hi
hello there
what are the features of software dudu
what is the software version?
2.0
feature for software dudu version 2.0 is DUMMY VARIABLE 1 DUMMY VARIABLE 2
what is its hardware requirement?
hardware for software dudu version 2.0 is DUMMY VARIABLE 1 DUMMY VARIABLE 2
deploy it please
what is the source_location?
/home/software_dump/
what is the destination_location?
tomcat
Missing configuration in 'software' table, no row in software table with name dudu and version 2.0
There are no configurations defined, will try to deploy with information we have
Deployment status (False, 'File /home/software_dump/dudu-2.0.tar not found')
```

Sample output 2
### In this output deployment succeeds
```
hi
hello there
what are the features of WatsonSearch
what is the software version?
0.0.1
feature for software WatsonSearch version 0.0.1 is DUMMY VARIABLE 1 DUMMY VARIABLE 2
can you deploy it please?
what is the source_location?
/home/cdpai/software_to_deploy
what is the destination_location?
tomcat
Missing configuration in 'software' table, no row in software table with name WatsonSearch and version 0.0.1
There are no configurations defined, will try to deploy with information we have
**LOG TRUNCATED**
WatsonSearch/search/vendor.tomcat.bundle.js.gz
Using CATALINA_BASE:   /home/cdpai/tomcat/apache-tomcat-8.5.20
Using CATALINA_HOME:   /home/cdpai/tomcat/apache-tomcat-8.5.20
Using CATALINA_TMPDIR: /home/cdpai/tomcat/apache-tomcat-8.5.20/temp
Using JRE_HOME:        /usr
Using CLASSPATH:       /home/cdpai/tomcat/apache-tomcat-8.5.20/bin/bootstrap.jar:/home/cdpai/tomcat/apache-tomcat-8.5.20/bin/tomcat-juli.jar
Using CATALINA_BASE:   /home/cdpai/tomcat/apache-tomcat-8.5.20
Using CATALINA_HOME:   /home/cdpai/tomcat/apache-tomcat-8.5.20
Using CATALINA_TMPDIR: /home/cdpai/tomcat/apache-tomcat-8.5.20/temp
Using JRE_HOME:        /usr
Using CLASSPATH:       /home/cdpai/tomcat/apache-tomcat-8.5.20/bin/bootstrap.jar:/home/cdpai/tomcat/apache-tomcat-8.5.20/bin/tomcat-juli.jar
Tomcat started.
Deployment status (True, 'Deployment successful')
```
