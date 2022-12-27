# -*- coding: utf-8 -*-
__all__ = ['TableCreator']
import json
import pandas


class TableCreator:
    def __init__(self, file_name):
        self.file_name = file_name

    def create(self):
        with open(self.file_name, encoding='utf-8', errors='ignore') as json_data:
            data = json.load(json_data, strict=False)
        df = pandas.DataFrame(data)
        df.to_excel('./new.xlsx')
