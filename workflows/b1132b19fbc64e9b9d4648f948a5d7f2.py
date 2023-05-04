from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2023-05-04', 'schedule_interval': None, 'catchup': False, 'dag_id': 'b1132b19fbc64e9b9d4648f948a5d7f2'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    task_TextSummarizerPiece_0 = Task(
        dag, 
        task_id='task_TextSummarizerPiece_0',
        workflow_shared_storage={'source': 'None', 'base_folder': None, 'mode': 'Read/Write', 'provider_options': {}, 'storage_repository_id': None},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'TextSummarizerPiece', 'source_image': 'ghcr.io/tauffer-consulting/openai_domino_pieces:0.1.2-group0', 'repository_id': 2},
        piece_input_kwargs={'text': 'Patience and growth are two related words. These two words are about mental growth. Because a patient individual is a growing individual.  In my life, I am always faced with various problems. This problem is something that I never want to happen in my life.  Who also wants to have problems in his life? not there.  Of course, everyone has their problems. There is no one in this world, someone who doesn’t have problems.  The question is, how to solve the problem?  I have a solution that can help you to face every problem in your life.  This solution is not to take away your problem and then you don’t have the problem anymore. No. This is about how you can minimize your ego to be able to solve problems properly and wisely.  The trick is to be patient.  Patience is the best solution I do when I’m faced with a problem. Patience makes me calmer in controlling my ego when I have a problem. Patience keeps me from acting recklessly. Patience also makes me more mature in dealing with a problem.  the key is patience.  When you are patient in facing problems, I believe, God is present in your life at that time. God gives you encouragement and help so that you are strengthened to immediately be able to solve the problem properly and responsibly.  As I got older, I kept looking for answers on how I could achieve a good life. how can I become an individual who prioritizes morality over egoism  It’s about mental growth and now I’m doing it.  Whenever there is a problem, the first thing I do is control myself, control my ego, and be patient with it.  this is the best way I can do when there is a problem. This led me to change my life for the better. My life gets better when I can control myself. My mentality is growing, and I can enjoy my days more and more.  I suggest to you, whatever problems you have today in your life, which make you anxious and in a dilemma, that’s okay. Just be patient.  Patience is the key to maturity. This will make your life grow and make you a wise person in the future.  Trust me, patience is the best key you can do when there is a problem. and patient attitude will make you mentally grow into a better individual than before.  Thank you for reading my journaling, enjoy!', 'openai_model': 'gpt-3.5-turbo', 'chunk_size': 1000, 'chunk_overlap_rate': 0.2, 'max_tokens': 500, 'temperature': 0.2, 'containerResources': {'cpu': {'min': 100, 'max': 100}, 'memory': {'min': 128, 'max': 128}, 'useGpu': False}}
    )()

