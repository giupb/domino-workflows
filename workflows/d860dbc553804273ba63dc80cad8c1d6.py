from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2023-05-04', 'schedule_interval': None, 'catchup': False, 'dag_id': 'd860dbc553804273ba63dc80cad8c1d6'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    task_TextSummarizerPiece_0 = Task(
        dag, 
        task_id='task_TextSummarizerPiece_0',
        workflow_shared_storage={'source': 'None', 'base_folder': None, 'mode': 'Read/Write', 'provider_options': {}, 'storage_repository_id': None},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'TextSummarizerPiece', 'source_image': 'ghcr.io/tauffer-consulting/openai_domino_pieces:0.1.2-group0', 'repository_id': 5},
        piece_input_kwargs={'text': 'á não é mais eu, é algo me apossando. penetra disfarçado, sem alarmar, sem ser convidado, provavelmente pelas minhas costas (conveniente para covardes) e se instala na parte central do peito. vai me sugando, me puxando. às vezes quando estou trabalhando no computador, me dou de conta que estou numa posição corcunda, peito afundado, escondido, como se estivesse com vergonha e medo de olhar pra isso que dói.  é como se um dementador estivesse sempre por perto  você sabe como se espanta um dementador? é preciso relembra de uma memória feliz, se concentrar nela, encontrar talvez a única centelha de energia que lhe resta para conduzir a lembrança pra um movimento expansivo, até conjurar um patrono magnífico através da sua varinha.  EXPECTO PATRONUM doido né. como Harry Potter já falava sobre depressão e eu nunca percebi até começar a escrever esse texto.  mas somos trouxas, não podemos conjurar um patrono, nunca saberemos sua forma. mas a fagulha de energia, de alegria, ela talvez exista aí dentro. pode ser desafiador encontrá-la, eu sei. existem formas — trouxas — que podem nos ajudar nessa busca, como a psicoterapia e/ou medicamentos psiquiátricos, pessoas que amamos, animais, música…  já tive épocas onde a fagulha de alegria se escondia muito bem. já tinha aceitado a escuridão, já tava indo pra Azkaban. mas eu a encontrei pq a minha realidade, as condições de temperatura e pressão em que eu me encontrava, estimularam (mesmo eu sem energia) continuar a busca. os estímulos: privilégio social, pessoas que amo reciprocamente e um medo de me afundar mais ainda — o medo da piora da depressão e ansiedade era mais forte que os próprios sintomas delas. assim, as memórias, as lembranças alegres surgiam de repente, raramente, como ondas corporais, me inundando de alguma aleatória sensação, sentimento e pensamento gostosos, já familiares, mas ainda vagos e distantes. taí, as minhas fagulhas. agora o processo é de aprendizado: como conjurar meu patrono, e qual sua forma? acho que podem ser formas. afinal somos trouxas, mas inteligentes o suficiente pra elaborarmos simples e mirabolantes ideias de nos preenchermos com alegria, acolhermos as dores e expulsarmos qualquer dementador que esteja por perto.  o movimento expansivo que estou fazendo para conseguir conjurar meu patrono não é só um: . ouvir e trazer pra consciência minhas dores através da meditação. . falar e falar e falar sobre essas dores e angústias na minha terapia e com seletas pessoas que eu amo. . participar de roda de homens que partilham suas dores, alegrias e desafios através da escuta e da fala.  esses movimentos expandem minha coragem de olhar mais profunda e amorosamente para as dores e tristezas. permitem eu tomar posse da minha vida pra eu mesma conduzi-la. simbolicamente é o movimento que preci', 'openai_model': 'gpt-3.5-turbo', 'chunk_size': 1000, 'chunk_overlap_rate': 0.2, 'max_tokens': 500, 'temperature': 0.2, 'containerResources': {'cpu': {'min': 100, 'max': 100}, 'memory': {'min': 128, 'max': 128}, 'useGpu': False}}
    )()

