AlertColor = {
    "success": "#4CAF50",
    "error": "#FF0000",
    "info": "#008AFF",
    "nodata": "#616161",
    "warning": "#b0ad0b"
}
AlertIcon = {
    "success": ":done: ",
    "fail": ":fail: ",
    "running": ":inprogress: ",
    "waiting": ":ico_waiting: ",
    "cancel": ":cancel: "
}
MessageActions = [
    {
        "name": "ok",
        "text": "OK",
        "type": "button",
        "value": "ok"
    },
    {
        "name": "no",
        "text": "Cancel",
        "type": "button",
        "value": "no",
        "style": "danger",
        "confirm": {
            "title": "Are you sure?",
            "text": "If you break the work flow, I can't help rolling back previous steps",
            "ok_text": "Yes",
            "dismiss_text": "No"
        }
    }
]
