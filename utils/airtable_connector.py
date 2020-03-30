# coding=utf-8
from airtable import Airtable

import config


def get_air_table_instance(table_name):
    return Airtable(config.AIRTABLE_BASE, table_name,
                    api_key=config.AIRTABLE_TOKEN)


def get_user_check_in(user_email, date):
    air_table = get_air_table_instance(config.AIRTABLE_TABLE_CHECKIN)
    is_checked = air_table.get_all(
        view="Raw",
        formula="AND({Email}=\"%s\",{Date}=\"%s\")" % (user_email, date)
    )
    return len(is_checked)


def check_in(user_email, channel):
    air_table = get_air_table_instance(config.AIRTABLE_TABLE_CHECKIN)
    air_table.insert({"Email": user_email, "Team": channel})
    return True
