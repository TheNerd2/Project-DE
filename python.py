import requests

def obter_info_ip(ip):
    try:
        # Fazendo uma requisição para a API ipinfo.io
        resposta = requests.get(f'http://ipinfo.io/{ip}/json')
        
        if resposta.status_code == 200:
            # Se a resposta for bem-sucedida, exibe as informações
            dados_ip = resposta.json()
            return dados_ip
        else:
            return f"Erro ao obter informações do IP: {resposta.status_code}"
    
    except Exception as e:
        return f"Erro: {str(e)}"

# Captura o IP que o usuário deseja verificar
ip = input("Digite o endereço IP para obter as informações: ")

# Obtém as informações do IP
informacoes = obter_info_ip(ip)

# Exibe as informações
if isinstance(informacoes, dict):
    print("\nInformações sobre o IP:")
    for chave, valor in informacoes.items():
        print(f"{chave.capitalize()}: {valor}")
else:
    print(informacoes)
input("press any key to close CMD:")