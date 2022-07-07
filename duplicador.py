import requests
import json
import base64
from time import sleep

#VARIAVEIS CONFIGURÁVEIS:
# 1 -  CONNECTOR_ID = ID do conector que irá ser replicado (mude para o id que você deseja replicar)
CONNECTOR_ID = 1960
# URL referente ao conector que será duplicado
URL = f"https://api.dev.telemetria.webhi.com.br/rest/v1/connectors/{CONNECTOR_ID}/duplicate/"

# 2 - NAME = Nome que será aplicado nos conectores duplicados, Exemplo: SIMULADOR MODBUS - TCP
NAME = 'teste conector duplicado'

# 3 - SERIAL_NUMBER = Número de série que serão aplicados ao conectores duplicados
SERIAL_NUMBER = 100

# 4 - E_TAG = E-TAG do conector
E_TAG = '\"c9c557dd05a44c6c60401a9a91ebda92\"'

# 5 - EMAIL e SENHA = Digite seu EMAIL e SENHA para criar a autorização da replicação
EMAIL = 'teste@teste.com.br'
SENHA = '17b17b17b'

email_senha = f'{EMAIL}:{SENHA}'
email_senha_encoded = (base64.b64encode(email_senha.encode('ascii')))
base64_encoded = email_senha_encoded.decode('ascii')

AUTHORIZATION = base64_encoded

# 6 - MIN = Define o valor onde as repetições irão começar //MAX = Define o valor onde as repetições irão parar
# Exemplo: MIN = 0 // MAX = 10, resultará em uma sequenência de 10 conectores (1,2,3...10)
MIN = 0
MAX = 1

# Criando a repetição de requests
for c in range( MIN , MAX + 1 ):
    payload = json.dumps({
    "name": f"{NAME} - {'%03d' % c}",
    "serial_number": f"XXX.{SERIAL_NUMBER + c}",
    })
    headers = {
    'Content-Type': 'application/json',
    'If-Match': E_TAG,
    'Authorization': f'Basic {AUTHORIZATION}'
    }

    response = requests.request("POST", URL, headers=headers, data=payload)

    print(response.text)

    sleep(4)
