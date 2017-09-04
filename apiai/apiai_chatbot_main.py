""" 
This is sample api ai implementation for chatbot 
It is by no means production like. It only helps in starting of with the work.
"""

import apiai
import json
CLIENT_ACCESS_TOKEN = 'CLIENT_ACCESS_TOKEN'

class Bot(object):
    _contexts=[]
    def __init__(self, client_token='<clientToken>'):
        self.AI = apiai.ApiAI(client_token)
        self.request = self.AI.text_request()
        self.request.lang = 'en'

    def reinitialize(self):
	self.request = self.AI.text_request()

    def handle(self, text):
        self.request.query = text
        response = self.request.getresponse().read().decode("utf-8")
        contexts = json.loads(response)['result']['contexts']
	if len(contexts) != 0:
		self._contexts.append(contexts[0])
        intent = str(json.loads(response)['result']['metadata']['intentName'])
	print("Contexts ",self._contexts)
	print("Intent ",intent)
	print("\n\n",response)

def main():
    b = Bot(CLIENT_ACCESS_TOKEN)
    while True:
        cmd = raw_input('me; ')
        b.handle(cmd)
	b.reinitialize()

if __name__ == '__main__':
    main()
