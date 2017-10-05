
##To generate response from fullfilment, you have to follow the response structure in path - https://api.ai/docs/fulfillment#response.

The code present here, sends a very simple static response 
{
    "displayText": "Its an awesome Company",
    "speech": "Its an awesome Company",
    "source": "apiai_simple_python_webhook",
    "data": {
    }
}

Webhook code can be extended to retireve the responses from databases/files or infact run a predictive model here to generate responses.

Webhook should only set output context and if need be it should lookup input context, if it is correct or not. Webhook is not responsible for managing the context of complete chatbot.

apiai_chatbot_main.py is responsible for maintaining the context by saving it in local variable. It only shows how to save the context but can be extended to handle complex situation. 
