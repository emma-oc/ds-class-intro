# -*- coding: utf-8 -*-
import json

import pandas as pd

def check_path(path):



def read_csv(file):
    tbl = pd.read_csv(file)
    print(len(tbl.index)+1)


def write_csv(data_list, output_file):
    obj = pd.DataFrame(data_list)
    obj.to_csv('data/',output_file,'.csv',index=False,columns = None, header=False)


def read_json(file):
    with open(file) as myjs:
        js = json.load(myjs)
    print(js)


if __name__=="__main__":
    pass