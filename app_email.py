import json
import logging
import os
from pathlib import Path
from random import choice
from urllib.parse import quote

from dotenv import load_dotenv

from pickpocket import pocketapi, sendemail

load_dotenv()

DOWNLOAD_ED = True

PARAMS = {"consumer_key": os.getenv('POCKET_CONSUMER_KEY'),
          "access_token": os.getenv('POCKET_ACCESS_TOKEN'),
          'detailType': 'complete'}

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s||%(module)s||%(lineno)s||%(levelname)s||%(message)s',
    filename='app_email.log')
logger = logging.getLogger(__name__)

def read_write_data():
    if not DOWNLOAD_ED or not os.path.isfile('.sample-data.json'):
        data = pocketapi.read_from_pocket(PARAMS)
    else:
        print('using saved data')
        with open('../.sample-data.json', 'r') as f:
            data = json.load(f)

    if DOWNLOAD_ED:
        with open('.sample-data.json', 'w') as f:
            f.write(json.dumps(data, indent=4))

    return data

def choose_one_entry(entries):
    """Goes through dict of id: dict and chooses one id: dict pair"""
    pocket_ids = list(entries.keys())
    chosen_id = choice(pocket_ids)
    result = {chosen_id: entries[chosen_id]}
    return result

def email_entry(entry):
    pass

def delete_entry(entry):
    pass


def main():
    data = read_write_data()
    entry = choose_one_entry()
    email_entry(entry)
    delete_entry(entry)


if __name__ == '__main__':
    main()




