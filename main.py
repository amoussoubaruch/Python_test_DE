# -*- coding: utf-8 -*-

# Created by Baruch AMOUSSOU-DJANGBAN 

from src.drug_mention.drug_mention_job import DrugMentionJob

def main(drug_filename, clinical_trials_filename, pubmed_filename, output_name  ): 
    
    job = DrugMentionJob(drug_filename, clinical_trials_filename, 
                         pubmed_filename, output_name
                         )
    job.drug_mention_analysis()
    

# Run job 
from config import conf as cfg

if __name__ == "__main__":
    main(cfg.drug_filename,
         cfg.clinical_trials_filename,
         cfg.pubmed_filename,
         cfg.output_name
         )

