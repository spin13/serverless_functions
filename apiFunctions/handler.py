import sys

sys.path.append('./slack')
sys.path.append('./flickr')

import json
import os
import env
import slack
import flickr_api as flickr

# get environment variable
# os.environ.get("env01")

def hello(event, context):
    #params = get_parameters(event)

    body = {
        "input": event
        #"params": str(params),
        #"param_names": str(params.keys())
    }

    response = {
        "statusCode": 200,
        # "body": json.dumps(body)
        "body": "body"
    }

    return response

def slack_say(event, context):
    """
    post slack to message

    Args:
        
    """

    params = get_parameters(event)
    message = params["message"]
    channel = params["channel"]

    slack.post_slack(
        username = "lambda",
        channel = channel,
        message = message
    )
    body = {
        "env": "ok"
    }
    response = {
        "statusCode": 200,
        # "body": json.dumps(body)
        "body": json.dumps(body)
    }

    return response

# return URLQuery to dict
def get_parameters(event):
    params = event["queryStringParameters"]
    print(params)
    print(params.keys())
    print(params.values())
    print(type(params))
    return event["queryStringParameters"]
