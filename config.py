# coding=utf-8
import os


# Slack
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_DEFAULT_CHANNEL = os.environ.get("SLACK_DEFAULT_CHANNEL", "#test_bot")
SLACK_PATTERN = {
    "daily": ["[daily]"],
    "morning": ["good", "morning"],
    "chao_buoi_sang": ["chao", "buoi", "sang"]
}
SLACK_REACTION_EMOJI = os.environ.get("SLACK_REACTION_EMOJI", "+1")

# AirTable
AIRTABLE_TOKEN = os.environ.get("AIRTABLE_TOKEN")
AIRTABLE_BASE = os.environ.get("AIRTABLE_BASE")
AIRTABLE_TABLE_CHECKIN = os.environ.get("AIRTABLE_TABLE_CHECKIN", "Checkin")
AIRTABLE_TABLE_ABSENT = os.environ.get("AIRTABLE_TABLE_ABSENT", "Absent")
