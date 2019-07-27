#! /user/bin/env python
#coding:utf-8

'''
Created by piliang on 2019/7/9
'''

import pytest

#flask = pytest.importorskip("flask",reason='import skip')
pytestmark = pytest.mark.skipif(1==2,reason="no test")


def test():
    print('i am function')




class Test1:
    def test_1(self):
        print('test_1')
        print('continue')

    @pytest.mark.xfail(reason='xfail',run=True)
    def test_2(self):
        print('test_2')
        assert 1==2
        print('continue')
