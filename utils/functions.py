# -*- coding: utf-8 -*-


# Created by Baruch AMOUSSOU-DJANGBAN 

import pandas as pd 
import pathlib as pl
import os 


def csv_reader(fileName):
    path_csv = pl.Path(os.getcwd()) / fileName
    with open(path_csv, 'rb') as file:
        data = pd.read_csv(file)
    return data


def save_json_file(df, fileName):  
    
    with open(fileName, "w") as outfile:
        outfile.write(df.to_json(orient="records"))
        
        
def load_json_file(fileName):  
    path_json = pl.Path(os.getcwd()) / fileName
    with open(path_json, 'rb') as file:
        data = pd.read_json(file)    
    return data
    
