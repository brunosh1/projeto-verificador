import requests
import json
from datetime import datetime

# Função que lê os sites do arquivo sites.txt
def ler_sites():
    with open("sites.txt", "r") as arquivo:
        return [linha.strip() for linha in arquivo.readlines()]
    
# Função principal que verifica o status dos sites
def verificar_sites():
    sites = ler_sites()      
    resultados = [] 

    for site in sites:
        try:
            # Tenta fazer uma requisição GET ao site
            resposta = requests.get(site, timeout=5)
            status = f"{resposta.status_code} (OK)"
            ok = True
        except requests.exceptions.RequestException:
            status = "ERRO"
            ok = False

        # Cria um dicionário com os dados do site
        resultado = {
            "site": site,
            "status": status,
            "ok": ok,
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        resultados.append(resultado)  # Adiciona na lista

    # Salva os resultados em um arquivo JSON
    with open("resultados.json", "w") as json_file:
        json.dump(resultados, json_file, indent=4)

# Executa a função principal se o script for rodado diretamente
if __name__ == "__main__":
    verificar_sites()