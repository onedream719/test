#! /user/bin/env python
#coding:utf-8

'''
Created by piliang on 2019/7/12
'''
import os
from globals import g_path,g_data
import json
import yaml


def data_provider(path):
    yaml_path = os.path.join(g_path['yaml_basepath'], g_path['yaml_path'])
    with open(yaml_path, 'r', encoding='utf-8') as f:
        g_data['yaml_path'] = yaml.load(f)

    json_path = os.path.join(g_path['json_basepath'], path)
    with open(json_path, 'r', encoding='utf-8') as f:
         json_data = json.load(f)

    return g_data['yaml_path'],json_data