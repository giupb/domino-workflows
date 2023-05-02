from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2023-05-02', 'schedule_interval': None, 'catchup': False, 'dag_id': 'ba24e1493c89414096964b9fa8b3d274'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    task_YoutubeDownloadPiece_0 = Task(
        dag, 
        task_id='task_YoutubeDownloadPiece_0',
        workflow_shared_storage={'source': 'None', 'base_folder': None, 'mode': 'Read/Write', 'provider_options': {}, 'storage_repository_id': None},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'YoutubeDownloadPiece', 'source_image': 'ghcr.io/tauffer-consulting/social_media_domino_pieces:0.1.0-group0', 'repository_id': 5},
        piece_input_kwargs={'output_type': 'audio', 'containerResources': {'cpu': {'min': 100, 'max': 100}, 'memory': {'min': 128, 'max': 128}, 'useGpu': False}, 'url': 'https://www.youtube.com/watch?v=zhWDdy_5v2w&ab_channel=AsapSCIENCE'}
    )()

