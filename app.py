# coding=utf-8
from flask import Flask, make_response, jsonify, request

import autobot
import config
from utils.convert_vnm import convert

app = Flask(__name__)


@app.route("/", methods=["GET"])
def ok():
    return "Successfully installed!"


@app.route("/slackbot", methods=["POST"])
def slack_bot():
    """
    This is URL to accept Slack mention message
    {
        "token": "ZZZZZZWSxiZZZ2yIvs3peJ",
        "team_id": "T061EG9R6",
        "api_app_id": "A0MDYCDME",
        "event": {
            "type": "app_mention",
            "user": "U061F7AUR",
            "text": "What is the hour of the pearl, <@U0LAN0Z89>?",
            "ts": "1515449522.000016",
            "channel": "C0LAN2Q65",
            "event_ts": "1515449522000016"
        },
        "type": "event_callback",
        "event_id": "Ev0LAN670R",
        "event_time": 1515449522000016,
        "authed_users": [
            "U0LAN0Z89"
        ]
    }
    """
    data = request.json
    print(data)

    if data.get("challenge"):
        return make_response(jsonify(challenge=data["challenge"]), 200)

    if data["event"].get("text"):
        _processing_message(
            data["event"]["text"],
            data["event"]["user"],
            data["event"]["channel"],
            data["event"]["ts"])

    return make_response(jsonify(message="ok"), 200)


def _processing_message(message, user, channel=None, ts=None):
    message = convert(message.lower())

    if all(x in message for x in config.SLACK_PATTERN["morning"]):
        autobot.morning(user, channel, ts)
    elif all(x in message for x in config.SLACK_PATTERN["chao_buoi_sang"]):
        autobot.morning(user, channel, ts)
    elif all(x in message for x in config.SLACK_PATTERN["daily"]):
        autobot.morning(user, channel, ts)

    return


if __name__ == '__main__':
    app.run()
