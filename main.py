import os
from config import *
from parser import Parser
from api_handler import APIHandler
from data_updater import DataUpdater
from table_creator import TableCreator


def main():
    if not os.path.exists('./data.json'):
        Parser('./Students.xlsx').parse()
    liked = APIHandler(access_token, user_id).get_result()
    DataUpdater(liked).update()
    TableCreator("data.json").create()


if __name__ == '__main__':
    main()
