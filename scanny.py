from crypt import methods
import os
import sys
import typing as t
import json

from datetime import datetime
from flask import Flask, jsonify, request

a = "{"
b = "}"
LISTENING_PORT = int(sys.argv[1])
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

def get_user(username: str) -> t.Optional[str]:
    command = 'scannycheck %s 1' % username
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def cont_online(username: str) -> t.Optional[str]:
    command = 'scannycheck %s 2' % username
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def limiter_user(username: str) -> t.Optional[str]:
    command = 'scannycheck %s 3' % username
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def check_data(username: str) -> t.Optional[str]:
    command = 'scannycheck %s 4' % username
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def check_dias(username: str) -> t.Optional[str]:
    command = 'scannycheck %s 5' % username
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final
    
diretorio = '/etc/v2ray/config.json'  # Substitua pelo caminho correto do arquivo JSON

# Verifique se o arquivo JSON existe
if os.path.exists(diretorio):
    with open(diretorio, 'r') as arquivo_config:
        config = json.load(arquivo_config)

    # Acesse o UUID no arquivo de configuração
    try:
        uuid = config.get('inbounds')[0].get('settings').get('clients')[0].get('id')
        uuid2=(f"{uuid}")
    except (KeyError, IndexError):
        uuid2=("null")
else:
    uuid2=("null")

@app.route('/checkUser', methods=['POST', 'GET'])
def check_user():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            user_get = req_data.get("user")
            uuid = uuid2
            username = get_user(user_get)
            
            if username == "Not exist":
                # Se o usuário não for encontrado na primeira verificação, execute este código
                def extrair_informacoes(username, linha):
                    partes = linha.strip().split(" | ")
                    if len(partes) == 3 and partes[1] == username:
                        return partes[0], partes[2]
                    else:
                        return None, None

                # Abrir o arquivo de texto
                with open("/etc/SSHPlus/RegV2ray", "r") as arquivo:
                    # Nome de usuário que você deseja pesquisar
                    username_procurado = user_get

                    # Loop pelas linhas do arquivo
                    encontrado = False
                    for linha in arquivo:
                        uuid, data = extrair_informacoes(username_procurado, linha)
                        if uuid is not None:
                            return jsonify({
                                "username": username_procurado,
                                "count_connection": cont_online(username_procurado),
                                "expiration_date": data,
                                "expiration_days": check_dias(username_procurado),
                                "limiter_user": limiter_user(username_procurado),
                                "uuid": uuid
                            })
                            encontrado = True
                            break

                    # Se o nome de usuário não foi encontrado no segundo arquivo, imprime "null"
                    if not encontrado:
                        return jsonify({'error': str(e)})
            else:
                return jsonify({
                    "username": username,
                    "count_connection": cont_online(username),
                    "expiration_date": check_data(username),
                    "expiration_days": check_dias(username),
                    "limiter_user": limiter_user(username),
                    "uuid": uuid2
                })
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        try:
            return 'Não autorizado!'
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(sys.argv[1]) if len(sys.argv) > 1 else LISTENING_PORT,
    )
