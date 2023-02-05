# -*- coding: utf-8 -*-

# Created by Baruch AMOUSSOU-DJANGBAN 

import sys 
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from fastapi import FastAPI
import uvicorn
from http import HTTPStatus
from src.first_journal.first_journal_analysis import FindFirstJournal
from config import conf as cfg

app = FastAPI(title="KPI API FOR DATA DRUG",
              description="This API help to extract some kpi from drug data analysis."#,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/drugs/first_journal/v1")
async def extract_from_json():
    job = FindFirstJournal(fileName= cfg.output_name)
    first = job.extract()
    return {"status" : HTTPStatus.OK, 
            "first_journal" : first} 

###
if __name__ == "__main__":
    uvicorn.run("main_api:app", host="0.0.0.0", port=5000, log_level="info")