#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:13:14 2019

@author: abhijeet
"""

import os
os.chdir('/home/abhijeet/abhijeet/tutorial/Kaggle/ashrae-energy-prediction/')

import pandas as pd, numpy as np
import matplotlib.pyplot as plt

print('step 0')
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
weatherTest = pd.read_csv('data/weather_test.csv')
weatherTrain = pd.read_csv('data/weather_train.csv')
buildingMetadata = pd.read_csv('data/building_metadata.csv')

print( 'step 1 ')
train = train.join(buildingMetadata.set_index('building_id'), on='building_id')
test = test.join(buildingMetadata.set_index('building_id'), on='building_id')

print('step 2' )
train = train.join(weatherTrain.set_index(['site_id', 'timestamp']), on= ['site_id', 'timestamp'])
test = test.join(weatherTest.set_index(['site_id', 'timestamp']), on = ['site_id', 'timestamp'])

print('step 3')