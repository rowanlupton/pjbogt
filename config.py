import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
HANDLE = 'pjbogt'

listenFor = [
    '@'+HANDLE
]
follow = [
    '836283571'
]
responses = [
    'weird flex but ok'
]
