#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'


program = {"loc":1.0
            ,"v(g)":1.0
            ,"ev(g)":1.0
            ,"iv(g)":1.0
            ,"n":1.0
            ,"v":1.0
            ,"l":1.0
            ,"d":1.0
            ,"i":1.0
            ,"e":1.0
            ,"b":1.0
            ,"t":1.0
            ,"lOCode":1.0
            ,"lOComment":1.0
            ,"lOBlank":1.0
            ,"locCodeAndComment":1.0
            ,"uniq_Op":1.0
            ,"uniq_Opnd":1.0
            ,"total_Op":1.0
            ,"total_Opnd":1.0
            ,"branchCount":1.0
            ,"target":1.0}

response = requests.post(url, json=program).json()
print( f' Bugs probability:  {response['bugs_probability']}')