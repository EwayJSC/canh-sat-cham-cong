# coding=utf-8
from datetime import datetime

from slackclient import SlackClient

import config
from utils.airtable_connector import get_user_check_in, check_in


slack_cli = SlackClient(config.SLACK_BOT_TOKEN)


def get_user(user_id):
    info = slack_cli.api_call("users.info", user=user_id)

    if info["ok"]:
        return info["user"]["profile"]["email"]
    return None


def get_channel(channel_id):
    """
    Ref: https://api.slack.com/methods/conversations.info
    :param channel_id: channel id
    :return: channel readable name
    """
    info = slack_cli.api_call("conversations.info", channel=channel_id)

    if info["ok"]:
        return info["channel"]["name"]
    print(info)
    return None


def morning(user_id, channel_id, ts):
    email = get_user(user_id)
    if not email:
        print("Invalid email! Do nothing")
        return None, None

    to_day = datetime.today().strftime("%-d/%-m/%Y")
    if not get_user_check_in(email, to_day):
        print("checkin for this user: ", email)
        channel_name = get_channel(channel_id)
        check_in(email, channel_name)
        slack_cli.api_call("reactions.add",
                           channel=channel_id,
                           name=config.SLACK_REACTION_EMOJI,
                           timestamp=ts)
    else:
        slack_cli.api_call("reactions.add",
                           channel=channel_id,
                           name="+1",
                           timestamp=ts)
    print("added reaction")
    return
