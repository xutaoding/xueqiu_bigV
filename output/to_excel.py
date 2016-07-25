from os.path import dirname, abspath, join
import pandas as pd
from pandas import ExcelWriter
from pymongo import MongoClient

path = dirname(abspath(__file__))

# df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['d', 'e', 'f'])
#
# ew = ExcelWriter(join(path, 'output.xlsx'), engine='xlsxwriter')
# df.to_excel(ew)
# ew.save()
# print df


def get_data():
    data = []
    db = MongoClient('192.168.100.20', 27017)
    coll_users = db['py_crawl']['bigv_user']
    coll_cubes = db['py_crawl']['bigv_cubes']

    users_id = [usr['usr_id'] for usr in coll_users.find({}, {'usr_id': 1})]

    for docs in coll_cubes.find():
        pass


    db.close()

