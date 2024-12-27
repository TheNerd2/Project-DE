import requests
from colorama import Style, init, Fore

# Inicia a BOSTA do colorama no windows
init(autoreset=True)

def scanner(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # se der erro no GET fudeu tendeu?

        infodoip = response.json()
        print(Fore.GREEN + f"Endereço IP: {infodoip.get('ip', 'N/A')}")
        print(Fore.GREEN + f"Hostname: {infodoip.get('hostname', 'N/A')}")
        print(Fore.GREEN + f"Cidade: {infodoip.get('city', 'N/A')}")
        print(Fore.GREEN + f"Região: {infodoip.get('region', 'N/A')}")
        print(Fore.GREEN + f"Pais: {infodoip.get('country', 'N/A')}")
        print(Fore.GREEN + f"Localização: {infodoip.get('loc', 'N/A')}")
        print(Fore.GREEN + f"Organização: {infodoip.get('org', 'N/A')}")
        print(Fore.GREEN + f"Timezone: {infodoip.get('timezone', 'N/A')}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error retrieving information for IP {ip}: {e}")

def receberip():
    ip = input("Enter the IP address to scan: ")
    scanner(ip)

if __name__ == "__main__":
    receberip()
