# ------------------
# Only for running this script here
import logging
import sys
from os.path import dirname

sys.path.insert(1, f"{dirname(__file__)}/../../..")
logging.basicConfig(level=logging.DEBUG)
# ------------------

# export SLACK_API_TOKEN=xoxb-***
# python3 integration_tests/samples/issues/issue_735.py

import os
from slack import RTMClient

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
)
logger = logging.getLogger('bot')
c_handler = logging.FileHandler('logs/bot.log')
c_handler.setLevel(logging.DEBUG)
logger.addHandler(c_handler)


# wait for a message event
@RTMClient.run_on(event="message")
def react_to_message(**payload):
    data = payload['data']
    web_client = payload['web_client']

    text = data['text']
    user_id = data['user']
    channel_id = data['channel']
    logger.info(f'text: {text}')  # doesn't show anything
    print(text)  # also doesn't show anything
    logging.info(text)  # neither this

    logger.debug(f'Sending text to Slack: "{text}"')  # doesn't show anything
    web_client.chat_postMessage(
        channel=channel_id,
        text=text
    )


if __name__ == "__main__":
    logger.info('Starting BOT')  # only this message is correctly displayed
    slack_token = os.environ["SLACK_API_TOKEN"]
    rtm_client = RTMClient(token=slack_token)
    rtm_client.start()  # after this, no print() message, no logger() message is displayed.
