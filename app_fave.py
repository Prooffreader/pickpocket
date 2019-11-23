import argparse
import logging
import os

from dotenv import load_dotenv

from pickpocket import pocketapi

load_dotenv()

PARAMS = {"consumer_key": os.getenv('POCKET_CONSUMER_KEY'),
          "access_token": os.getenv('POCKET_ACCESS_TOKEN')}


logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s||%(module)s||%(lineno)s||%(levelname)s||%(message)s',
    filename='app_fave.log')
logger = logging.getLogger(__name__)

def get_url_clarg():
    parser = argparse.ArgumentParser(description='(Re)save to pocket and favorite')
    parser.add_argument('url')
    args = parser.parse_args()
    return args.url

def main():
    url = get_url_clarg()
    pocketapi.add_and_fave(url)



if __name__ == '__main__':
    main()
