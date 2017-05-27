import json
import os

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


# return URLQuery to dict
def get_parameters(event):
    params = event["queryStringParameters"]
    print(params)
    print(params.keys())
    print(params.values())
    print(type(params))
    return event["queryStringParameters"]
