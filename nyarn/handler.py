import sys

sys.path.append('./slack')
sys.path.append('./flickr')

import json
import os
import env
import slack
import flickr_api as flickr


# POST cat picture to slack
def nyarn(event, context):
    slack.post_slack(
        username = "nyarn",
        channel = env.NYARN_POST_CHANNEL,
        message = flickr.random_url()
    )
    return { "statusCode": 200, "body": json.dumps({ "body": "OK" }) }

