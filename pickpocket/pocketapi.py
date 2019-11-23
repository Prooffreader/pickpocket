"""Handles all communications with the Pocket API, reading and writing
"""

import json
import os
from urllib.parse import quote

import requests


def read_from_pocket(params):
    """Reads all bookmarks from Pocket (or local json temporarily during development)
    and returns dict from JSON"""
    print('downloading from pocket')
    result = requests.post("https://getpocket.com/v3/get", params=params)
    if not result.status_code == 200:
        raise IOError(f'Status code is {result.status_code} instead of 200')
    result = json.loads(result.text)
    assert result['status'] == '1'
    assert result['complete'] == '1'
    return result['list']

def add_entry(url, params):
    pass


def favorite_entry(item_id, params):
    if not isinstance(item_id, str):  # TODO: is this necessary?
        item_id = str(item_id)
    blob = [{"action":"favorite","item_id":item_id}]
    txt = quote(json.dumps(blob))
    url = ('https://getpocket.com/v3/send?actions='
           f'{txt}&access_token={params["access_token"]}&consumer_key={params["consumer_key"]}')
    r = requests.get(url)
    # TODO: handle this
    raise NotImplementedError
    do_something_with(json.loads(r.text))

# def write_to_pocket(item_id, action, **kwargs):
#     """item_id, action = str"""
#     actions = {'item_id': item_id,
#                'action': action}
#     for k, v in kwargs.items():
#         actions[k] = v
#     actions = quote(json.dumps([actions]))
#     url = f'https://getpocket.com/v3/send?actions={actions}&access_token={PARAMS["access_token"]}&consumer_key={PARAMS["consumer_key"]}'
#     r = requests.get(url)
#     result = json.loads(r.text)
#     assert result['status'] == 1

#write_to_pocket("172725677", "favorite")

# class Pocketwriter:
#     def __init__(self, item_id):
#         self.item_id = item_id

#     def make_url(self, action, *kwargs)
#         a
#         url = f'https://getpocket.com/v3/send?actions=[{\{{actions}\}]&access_token=[ACCESS_TOKEN]&consumer_key=[CONSUMER_KEY]


#https://getpocket.com/v3/send?actions=%5B%7B%22action%22%3A%22archive%22%2C%22time%22%3A1348853312%2C%22item_id%22%3A229279689%7D%5D&access_token=[ACCESS_TOKEN]&consumer_key=[CONSUMER_KEY]
# decoded:
#https://getpocket.com/v3/send?actions=[{"action":"archive","time":1348853312,"item_id":229279689}]&access_token=[ACCESS_TOKEN]&consumer_key=[CONSUMER_KEY]


# def change_pocket_attribute():

#     def make_bookmark(d):
#         """Turns dictionary d into Bookmark dataclass
#         """
#         def get_image_url(images, image):
#             if images:
#                 for k, v in images.items():
#                     if v['src']:
#                         return v['src']
#             elif image:
#                 if image['src']:
#                     return image['src']
#             return DEFAULT_IMAGE_URL

#         def get_tags(d):
#             if d.get('tags', None):
#                 return list(d['tags'].keys())
#             else:
#                 return []

#         if d['status'] != '0':
#             return None

#     return Bookmark(item_id=int(d['item_id']),
#                     title=d['resolved_title'],
#                     image_url=get_image_url(d.get('images', None), d.get('image')),
#                     link_url=d['given_url'],
#                     excerpt=d['excerpt'],
#                     tags=get_tags(d),
#                     _timestamp_added=int(d['time_added']),
#                     _timestamp_updated=int(d['time_updated']),
#                     _timestamp_favorited=int(d['time_favorited'])
#                    )


# def make_all_bookmarks():
#     bookmarks = []
#     d = dict_request_from_pocket()
#     for __, v in d['list'].items():
#         bkmrk = make_bookmark(v)
#         if v:
#             bookmarks.append(bkmrk)
#     return bookmarks
