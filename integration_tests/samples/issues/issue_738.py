# ------------------
# Only for running this script here
import logging
import sys
from os.path import dirname

sys.path.insert(1, f"{dirname(__file__)}/../../..")
logging.basicConfig(level=logging.DEBUG)
# ------------------

import asyncio
import aiohttp
import os
from slack import WebClient


async def main():
    proxy = os.environ["HTTPS_PROXY"]
    print(f"Using {proxy} ...")
    session = aiohttp.ClientSession(trust_env=True)
    client = WebClient(
        token=os.environ['SLACK_API_TOKEN'],
        run_async=True,
        session=session,
    )
    response = await client.chat_postMessage(channel="#random", text="Sent through a proxy server")
    print(response)
    await session.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# pip3 install proxy.py
# proxy --port 9000 --log-level d
# export HTTPS_PROXY=http://localhost:9000
# export SLACK_API_TOKEN=xoxb-***
# python integration_tests/samples/issues/issue_738.py
