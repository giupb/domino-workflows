from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2023-05-04', 'schedule_interval': None, 'catchup': False, 'dag_id': '0acce48650b0458da4a2d446d5d02f42'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    task_TextSummarizerPiece_0 = Task(
        dag, 
        task_id='task_TextSummarizerPiece_0',
        workflow_shared_storage={'source': 'AWS S3', 'base_folder': 'folder-02', 'mode': 'Read/Write', 'provider_options': {'bucket': 'domino-shared-storage'}, 'storage_repository_id': 1},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'TextSummarizerPiece', 'source_image': 'ghcr.io/tauffer-consulting/openai_domino_pieces:0.1.2-group0', 'repository_id': 2},
        piece_input_kwargs={'text': None, 'openai_model': ['gpt-3.5-turbo', 4000], 'chunk_size': 1000, 'chunk_overlap_rate': 0.2, 'max_tokens': 500, 'temperature': 0.2}
    )()

