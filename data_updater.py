# -*- coding: utf-8 -*-
__all__ = ['DataUpdater']
import datetime
import json


class DataUpdater:
    def __init__(self, liked: list):
        self.liked = liked

    def update(self):
        date = datetime.datetime.now().strftime("%d %b")
        with open("data.json", encoding='utf-8', errors='ignore') as json_data:
            data = json.load(json_data, strict=False)
        for item in data:
            if item['Name'] in self.liked:
                item[date] = 'П'
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
