#! /user/bin/env python
#coding:utf-8

'''
Created by piliang on 2019/7/9
'''

import pytest
from provider import data_provider


@pytest.fixture(scope='session')
def login():
    print('login')
    return 'success'