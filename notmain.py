import re


def validate_email(email):
    if username := re.search(r"^([a-zA-Z0-9_]+)@(gmail|hotmail|yahoo)\.com$", email):
        return username
    else:
        return False
