#! /user/bin/env python
#coding:utf-8

'''
Created by piliang on 2019/7/9
'''

import os

project_path = os.path.dirname(os.path.abspath(__file__))
g_path ={
         'yaml_basepath':os.path.join(project_path, 'config'),
         'json_basepath':os.path.join(project_path, 'data'),
         'testcase_basePath':os.path.join(project_path, 'testcases'),
         'yaml_path':None
}

g_data={}