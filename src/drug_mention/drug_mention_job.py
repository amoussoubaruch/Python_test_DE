# -*- coding: utf-8 -*-

# Created by Baruch AMOUSSOU-DJANGBAN 

import os # To manage data saving with shell commands
from datetime import datetime # Manipulate date
import re # regular expression
import logging # To get logging messages

from utils.functions import csv_reader, save_json_file


class DrugMentionJob:
    
    def __init__(self,
                 drug_filename,
                 clinical_trials_filename,
                 pubmed_filename,
                 output_name                
                 ):
            """ 
            Parameters
            ----------
            outputName : str 
                Name and Path where we wrote final Json               
            """
            self.drug_filename = drug_filename
            self.clinical_trials_filename = clinical_trials_filename
            self.pubmed_filename = pubmed_filename
            self.output_name = output_name
            
    def load_data(self):
        #Read file drugs
        data_drugs = csv_reader(self.drug_filename)
        # Read clinical_trials.csv
        data_clinical_trials = csv_reader(self.clinical_trials_filename)                  
        #Read file pubmed.csv
        data_pubmed = csv_reader(self.pubmed_filename)  
        logging.info("All files are loaded .....................")
        return data_drugs, data_pubmed, data_clinical_trials
    
    def ponctuation_cleaning(self, df, col):
        df[col] = df[col].str.replace(r'[^\w\s]+', '')               
        return df

    def drug_mention_analysis(self): 
        data_drugs, data_pubmed, data_clinical_trials= self.load_data()
        data_pubmed = self.ponctuation_cleaning(data_pubmed, "title")
        data_clinical_trials = self.ponctuation_cleaning(data_clinical_trials, "scientific_title")
                
        data_pubmed["transform_title"] = data_pubmed["title"].str.split()
        data_pubmed_explode = data_pubmed.explode('transform_title', ignore_index=True)
        data_pubmed_explode["drug"] = data_pubmed_explode["transform_title"].str.upper()
        data_pubmed_explode = data_pubmed_explode.rename(columns={"journal": "pubmed"})
                
        data_clinical_trials["transform_scientific_title"] = data_clinical_trials["scientific_title"].str.split()
        data_clinical_trials_explode = data_clinical_trials.explode('transform_scientific_title', ignore_index=True)
        data_clinical_trials_explode["drug"] = data_clinical_trials_explode["transform_scientific_title"].str.upper()
        data_clinical_trials_explode = data_clinical_trials_explode.rename(columns={"journal": "clinical_trials"})


        tmp_df = data_drugs.merge(data_pubmed_explode[["drug","pubmed"]], on="drug", how='left')
        final_data = tmp_df.merge(data_clinical_trials_explode[["drug","clinical_trials","date"]], on="drug", how='left')
                
        save_json_file(final_data, self.output_name)    
        logging.info("Output file had created.....................")

