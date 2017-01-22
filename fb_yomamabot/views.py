from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import pprint
import requests 

class YoMamaBotView0(generic.View):
    def get(self, request, *args, **kwargs):
         HttpResponse("Hello World!")

class YoMamaBotView1(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '123456':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

class YoMamaBotView(generic.View):
    # The get method is the same as before.. omitted here for brevity
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                if 'message' in message:
                    # Print the message to the terminal
                    pprint(message)
                    post_facebook_message(message['sender']['id'], message['message']['text'])
        return HttpResponse()
        
def post_facebook_message(fbid, recevied_message):           
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=1996659387227637|9NHz1K3EP_5VfrEpCwkUBeLMSZA' 
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())
    
    
'''
7c799c0b62effe6bcd3933ffbb7533d2
7c799c0b62effe6bcd3933ffbb7533d2
EAAcX832DXfUBAAhufjegpZAc8SraMtMjtyCmx74tV9GtRCWqHZCWubjdCZBPQ4ItKKCfo5EkUk9QhWhmT3yZBZCl2UYQ9yg0H7uf5hZCIKgFSlKIa9m8VcHRVq0p3kvaAq3vflCxns8r1apaHV0rdAxXYFUU4sZAUajlNNgT03lBAZDZD

C:\Users\SE\AppData\Local\Programs\Python\Python35\python

set p=C:\Users\SE\AppData\Local\Programs\Python\Python35\python.exe
%p%
set da=C:\Users\SE\AppData\Local\Programs\Python\Python35\Scripts\django-admin
%da%

%da% startproject yomamabot
%p% manage.py runserver 80
%da% startapp fb_yomamabot

http://127.0.0.1:8000/fb_yomamabot/76c5893a5db705c3c7a70f33152ba5d043ce0d9b6ff0835b75
854bf6f2.ngrok.io/fb_yomamabot/76c5893a5db705c3c7a70f33152ba5d043ce0d9b6ff0835b75
'''