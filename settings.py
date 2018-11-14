# coding: UTF-8

import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# LINE
YOUR_CHANNEL_SECRET = os.environ.get("YOUR_CHANNEL_SECRET")
YOUR_CHANNEL_ACCESS_TOKEN = os.environ.get("YOUR_CHANNEL_ACCESS_TOKEN")

#azure
KEY1 = os.environ.get("KEY1")
