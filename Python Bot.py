import base64
import hashlib
import hmac

import json
import requests

access_token = 'qgdntcUqQibpcFZwTLOarjqCmPtXS/d5E8zovhoZS/Rd7e1Ue0JLVMzSGLwQB6r4+rDpddQcEBRILXlWXA4X80ZNWRToRf1ex1oi2RqR/jXjb/iNQbHjlZmxnqLfgKDnnlSa1KWeGtWqxptHoD0dGgdB04t89/1O/w1cDnyilFU='

# Load Json file to test
#with open('Webhook.json') as json_file:
##with open('JSonBody.json') as json_file:
##    events = json.load(json_file)
    #pprint(events)

events = open('//input')


# Validate parsed JSon data
if(events != None):
    # Loop through each event
    for event in body_json['events']:
        # Reply only text message.
        if(event['type'] == 'message' and event['message']['type'] == 'text'):
            # Get message and replyToken
            userID = event['source']['userId']
            replyToken = event['replyToken']
            text = event['message']['text']
            
            # User message content
            #print('\nUser Said')
            #print('UserID: ' + userID)
            #print('ReplyToken: ' + replyToken )
            #print('Text: ' + text)

            # Build message to reply back.
            replyMessage = {'type' : 'text', 'text' : text}

            # Bot reply message content
            #print('\nLine Bot Reply')
            #print(replyMessage['text'])

            # Make Post Request to Messaging API to reply to sender.
            url = 'https://api.line.me/v2/bot/message/reply'
            data = {'replyToken' : replyToken, 'messages' : replyMessage}
    
            # Parse reply message to Json 
            post = json.JSONEncoder().encode(data)            
            #print(post)
            
            headers = ['Content-Type: application/json', 'Authorization: Bearer ' + access_token]
            
            requests.post(url,post)
            
            #print(requests)
            
                       
