# -*- coding: utf-8 -*-

# Created by Baruch AMOUSSOU-DJANGBAN 

import os # To manage data saving with shell commands
from datetime import datetime # Manipulate date
import re # regular expression
import logging # To get logging messages

from utils.functions import load_json_file


class FindFirstJournal:
    
    def __init__(self,
                 fileName):
        self.fileName = fileName
     
    def extract(self):
        #Read file drugs
        data = load_json_file(self.fileName)             
        data_count = data.groupby(['clinical_trials'])['drug'].count()               
        print ("Journal Name with most of drugs are : ", data_count.idxmax())
        return data_count.idxmax()

