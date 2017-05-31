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

def ttest(event, context):
    print("here")
    print(env.SLACK_TOKEN)
    slack.post_slack(username="lambda", channel="#dev_null", message="lambda test")
    body = {
        "env": env.SLACK_TOKEN
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
