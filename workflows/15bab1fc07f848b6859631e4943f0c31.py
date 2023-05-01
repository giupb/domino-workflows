from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2023-05-01', 'schedule_interval': None, 'catchup': False, 'dag_id': '15bab1fc07f848b6859631e4943f0c31'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    task_YoutubeDownloadPiece_0 = Task(
        dag, 
        task_id='task_YoutubeDownloadPiece_0',
        workflow_shared_storage={'source': 'AWS S3', 'base_folder': 'flowui-shared-storage', 'mode': 'Read/Write', 'provider_options': {'bucket': 'storage'}, 'storage_repository_id': 1},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'YoutubeDownloadPiece', 'source_image': 'ghcr.io/tauffer-consulting/social_media_domino_pieces:0.1.0-group0', 'repository_id': 3},
        piece_input_kwargs={'output_type': 'audio', 'containerResources': {'cpu': {'min': 100, 'max': 100}, 'memory': {'min': 128, 'max': 128}, 'useGpu': False}, 'url': 'https://www.youtube.com/watch?v=zhWDdy_5v2w&ab_channel=AsapSCIENCE', 'output_file_name': 'audio_output'}
    )()
    task_AudioTranscriptionPiece_0 = Task(
        dag, 
        task_id='task_AudioTranscriptionPiece_0',
        workflow_shared_storage={'source': 'AWS S3', 'base_folder': 'flowui-shared-storage', 'mode': 'Read/Write', 'provider_options': {'bucket': 'storage'}, 'storage_repository_id': 1},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'AudioTranscriptionPiece', 'source_image': 'ghcr.io/tauffer-consulting/openai_domino_pieces:0.1.1-group0', 'repository_id': 2},
        piece_input_kwargs={'output_type': 'file', 'temperature': None, 'containerResources': {'cpu': {'min': 100, 'max': 100}, 'memory': {'min': 128, 'max': 128}, 'useGpu': False}, 'file_path': {'type': 'fromUpstream', 'upstream_task_id': 'task_YoutubeDownloadPiece_0', 'output_arg': 'file_path'}, 'prompt': 'transcript this audio'}
    )()
    task_TextSummarizerPiece_0 = Task(
        dag, 
        task_id='task_TextSummarizerPiece_0',
        workflow_shared_storage={'source': 'AWS S3', 'base_folder': 'flowui-shared-storage', 'mode': 'Read/Write', 'provider_options': {'bucket': 'storage'}, 'storage_repository_id': 1},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'TextSummarizerPiece', 'source_image': 'ghcr.io/tauffer-consulting/openai_domino_pieces:0.1.1-group0', 'repository_id': 2},
        piece_input_kwargs={'text': {'type': 'fromUpstream', 'upstream_task_id': 'task_AudioTranscriptionPiece_0', 'output_arg': 'transcription_result'}, 'chunk_size': 1000, 'chunk_overlap_rate': 0.2, 'openai_model': ['gpt-3.5-turbo', 4000], 'max_tokens': 500, 'temperature': 0.3, 'containerResources': {'cpu': {'min': 100, 'max': 100}, 'memory': {'min': 128, 'max': 128}, 'useGpu': False}}
    )()

    task_AudioTranscriptionPiece_0.set_upstream([globals()[t] for t in ['task_YoutubeDownloadPiece_0']])
    task_TextSummarizerPiece_0.set_upstream([globals()[t] for t in ['task_AudioTranscriptionPiece_0']])
