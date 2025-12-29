'''
DAG do projeto final 1 de Ciência de Dados.
'''

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime
import pendulum
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

default_args = {
    'owner': 'Matheus',
    'on_failure_callback': lambda context: print('Houve um erro nessa tarefa. Acesse os logs para mais detalhes.'),
    'on_success_callback': lambda context: print('A tarefa foi executada com sucesso.'),
}

with DAG(
    dag_id = 'dag_ds_projeto_final_1',
    description = 'DAG do projeto final 1 de Ciência de Dados.',
    tags = ['ds_projeto_final_1'],
    doc_md = __doc__,
    default_args = default_args,
    start_date = datetime(2025, 10, 1, tzinfo = pendulum.timezone('America/Sao_Paulo')),
    end_date = None,
    schedule = '*/5 * * * 1-5',
    catchup = False,
    on_failure_callback = lambda context: print('Houve um erro nessa DAG. Acesse os logs para mais detalhes.'),
    on_success_callback = lambda context: print('A DAG foi executada com sucesso.'),
) as dag_1:

    start = EmptyOperator(task_id = 'start')

    data_sourcing = BashOperator(
        task_id = 'data_sourcing',
        bash_command = f'''python {BASE_DIR}/notebooks/01_pd_data_sourcing.ipynb'''
    )

    data_understanding = BashOperator(
        task_id = 'data_understanding',
        bash_command = f'''python {BASE_DIR}/notebooks/02_pd_data_understanding.ipynb'''
    )

    data_processing = BashOperator(
        task_id = 'data_processing',
        bash_command = f'''python {BASE_DIR}/notebooks/03_pd_data_processing.ipynb'''
    )

    exploratory_data_analysis = BashOperator(
        task_id = 'exploratory_data_analysis',
        bash_command = f'''python {BASE_DIR}/notebooks/04_pd_exploratory_data_analysis.ipynb'''
    )

    analytics = BashOperator(
        task_id = 'analytics',
        bash_command = f'''python {BASE_DIR}/notebooks/05_pd_analytics.ipynb'''
    )

    end = EmptyOperator(task_id = 'end')

start \
    >> data_sourcing \
    >> data_understanding \
    >> data_processing \
    >> exploratory_data_analysis \
    >> analytics \
    >> end