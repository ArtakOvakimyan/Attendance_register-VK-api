__all__ = ['Parser']
import pandas
import json


class Parser:
    def __init__(self, path):
        self.path = path

    def parse(self):
        excel_data = pandas.read_excel(self.path)
        json_data = excel_data.to_json(orient='records', force_ascii=False)
        print(json_data)
        json_dict = json.loads(json_data)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(json_dict, json_file, ensure_ascii=False)
