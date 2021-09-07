import os
from datetime import datetime


def get_timestamp(date=datetime.now(), date_format="%Y%m%d_%H%M%S_%f"):
    return date.strftime(date_format)


def get_root_dir():
    return os.path.dirname(__file__) + os.sep
