# -*- coding: utf-8 -*-


from pytest_schema import schema
import pandas as pd
import json
from src.drug_mention.drug_mention_job import DrugMentionJob
from src.first_journal.first_journal_analysis import FindFirstJournal

output_schema = {
    "atccode": str,
    "drug": str,
    "pubmed": str,
    "clinical_trials" : str,
    "date": str
}

def test_drug_analysis():
    
    task = DrugMentionJob("tests/data_test/raw/drugs.csv", "tests/data_test/raw/clinical_trials.csv", 
                         "tests/data_test/raw/pubmed.csv",  "tests/data_test/output/test_output.json"
                         )
    data_drugs, data_pubmed, data_clinical_trials = task.load_data()
    
    task.drug_mention_analysis()
    
    f = open("tests/data_test/output/test_output.json")
    data = json.load(f)
    f.close()
      
    assert isinstance(data_drugs, pd.DataFrame)
    assert isinstance(data_pubmed, pd.DataFrame)    
    assert isinstance(data_clinical_trials, pd.DataFrame)  
    assert schema(output_schema) == data[0]
    
    
def test_count_journal():
    
    task_test = FindFirstJournal(fileName= "tests/data_test/output/test_output.json")
    journal= task_test.extract()
    
    assert isinstance(journal, str)
