# -*- coding: utf-8 -*-

# Created by Baruch AMOUSSOU-DJANGBAN

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import main


with DAG(
    'python_test_de_job',
    default_args={
        'depends_on_past': False,
        'email': ['amoussoubaruch@yahoo.fr'],
        'email_on_failure': False,
        'email_on_retry': False,
        'max_active_run':1,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    },
    description="Dags",
    schedule_interval=None,
    start_date=datetime(2023, 1, 12, 6, 0, 0),
    catchup=False, 
    tags=['TEST'],
) as dag:
    
    starter = DummyOperator(task_id='starter')

    drug_mention_analysis_task = PythonOperator(
        task_id='python_test_de',
        provide_context=True,
        python_callable=main,
        dag=dag,
    )
    
    end = DummyOperator(task_id='end')


    starter >> drug_mention_analysis_task >> end

