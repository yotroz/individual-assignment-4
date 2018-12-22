#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 23:22:03 2018

@author: yotroz
"""

#%%


graph10 =  {
            "a": ["b","c","d"],
            "b": ["c"],
            "c" : ["b", "d"],
            "d" : ["b"],
            }

import requests

url = 'http://127.0.0.1:5000/{}'

def upload_graph(graph): 
    data = graph
    request = requests.post(url .format('upload-graph'), json=data)
    
    return request.json()
 
def get_degrees_of_separation(graph, origin, destination): 
    data = graph
    request = requests.post('http://127.0.0.1:5000/degrees_of_separation/<origin>/<destination>', json=data)
    
    return request.json()
    