#! /user/bin/env python
#coding:utf-8

'''
Created by piliang on 2019/7/9
'''

import pytest
from globals import g_path

if __name__ == '__main__':
    pytest.main(['-sqr',g_path['testcase_basePath']])