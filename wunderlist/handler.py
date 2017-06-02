# -*- coding: utf-8 -*-
import sys

sys.path.append('./wunderlist')
sys.path.append('./slack')

import json
import os
import env
import wunderlist_api as wunderlist
import slack


def will_expire_tasks(event, context):
    """
    Args:
        event["queryStringParameters"]["project_name"]

    Returns:
        N days later expires task list json
    """
    params = __get_parameters(event)
    sess = wunderlist.create_session()
    tasks = wunderlist.will_expire_tasks_by_project_name(sess, 3, name=params["project_name"])
    return { "statusCode": 200, "body": json.dumps(tasks) }


def expired_tasks(event, context):
    """
    expired tasks

    Args:
        event["queryStringParameters"]["project_name"]

    Returns:
        task list json
    """
    params = __get_parameters(event)
    sess = wunderlist.create_session()
    tasks = wunderlist.expired_tasks_by_project_name(sess, name=params["project_name"])
    return { "statusCode": 200, "body": json.dumps(tasks) }


def post_slack_expired_tasks(event, context):
    """
    post to slack expired tasks
        
    Args:
        event["queryStringParameters"]["project_name"]

    Returns:
        post task list
    """
    params = __get_parameters(event)
    tasks = json.loads(expired_tasks(event, "")["body"])

    message = "*期限切れタスク*```\n"

    for task in tasks:
        message += task["due_date"] + " " + task["title"] + "\n"
    message += "```"

    slack.post_slack(
        username = "wunderlist",
        channel = "#" + params["project_name"],
        message = message
    )
    return { "statusCode": 200, "body": "OK" }


def post_slack_will_expire_tasks(event, context):
    """
    post to slack it will be expire tasks
        
    Args:
        event["queryStringParameters"]["project_name"]

    Returns:
        post task list
    """
    params = __get_parameters(event)
    tasks = json.loads(will_expire_tasks(event, "")["body"])

    message = "*直近タスク*```\n"

    for task in tasks:
        message += task["due_date"] + " " + task["title"] + "\n"
    message += "```"

    slack.post_slack(
        username = "wunderlist",
        channel = "#" + params["project_name"],
        message = message
    )
    return { "statusCode": 200, "body": "OK" }


def notify_all_expire_tasks(event, context):
    for project_name in env.WUNDERLIST_PROJECTS:
        post_slack_expired_tasks({ "queryStringParameters": { "project_name": project_name } }, "")
        post_slack_will_expire_tasks({ "queryStringParameters": { "project_name": project_name } }, "")

    return { "statusCode": 200, "body": "OK" }


def __get_parameters(event):
    params = event["queryStringParameters"]
    return event["queryStringParameters"]
