#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Tue Apr 17 23:39:14 2018
@author     : Sourabh
"""

# %%

import sys

# add modules path before importing them
sys.path.insert(0, '../../')
    
from pyutils.web import HttpRequest
from pyutils.web import HttpMethod
from pyutils.web import HttpRequestManager

class TestDriver:
    
    def __init__(self):
        pass
    
    def testWebRequest(self):
        req = HttpRequest()
        req.uri = 'http://date.jsontest.com/'
        
        reqMgr = HttpRequestManager()
        rsp = reqMgr.invoke(req, HttpMethod.GET)
        
        print(rsp.payload)
        pass
    
    pass

if __name__ == '__main__':
    td = TestDriver()
    td.testWebRequest()
    pass
