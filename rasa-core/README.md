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
user: hi
bot : hello there
user: what are the features of software dudu
bot : what is the software version?
user: .0
bot : feature for software dudu version 2.0 is DUMMY VARIABLE 1 DUMMY VARIABLE 2
user: what is its hardware requirement?
bot : hardware for software dudu version 2.0 is DUMMY VARIABLE 1 DUMMY VARIABLE 2
user: deploy it please
bot : what is the source_location?
user: /home/software_dump/
bot : what is the destination_location?
user: tomcat
bot : Missing configuration in 'software' table, no row in software table with name dudu and version 2.0
bot : There are no configurations defined, will try to deploy with information we have
bot : Deployment status (False, 'File /home/software_dump/dudu-2.0.tar not found')
```

Sample output 2
### In this output deployment succeeds
```
user: i
bot : hello there
user: hat are the features of WatsonSearch
bot : what is the software version?
user: .0.1
bot : feature for software WatsonSearch version 0.0.1 is DUMMY VARIABLE 1 DUMMY VARIABLE 2
user: an you deploy it please?
bot : what is the source_location?
user: home/cdpai/software_to_deploy
bot : what is the destination_location?
user: omcat
bot : Missing configuration in 'software' table, no row in software table with name WatsonSearch and version 0.0.1
bot : There are no configurations defined, will try to deploy with information we have
**LOG TRUNCATED**
bot : WatsonSearch/search/vendor.tomcat.bundle.js.gz
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
bot : Deployment status (True, 'Deployment successful')
```
