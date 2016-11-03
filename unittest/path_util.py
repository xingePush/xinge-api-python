#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2013-5-30

@author: stanleyzeng
'''

import os

def smart_path(path, self_path=__file__):
    if '/' == path[0]:
        # absolute path
        return path
    else:
        # relative path
        return os.path.abspath(os.path.join(os.path.dirname(self_path), path))
    
def append_sys_path(_sys, path):
    path = smart_path(path)
    if path not in _sys.path:
        _sys.path.append(path)