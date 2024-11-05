import nmap
import os
from datetime import datetime
import platform

def scan_rede(network):
    
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sP')
    lista_hosts = []

    for ativos in nm.all_hosts():
        status = nm[ativos]['status']['state']
        lista_hosts.append((ativos,status))

    return lista_hosts

hosts = scan_rede('10.1.1.0/24')

data_atual = datetime.now().strftime('%d%m%Y-%H%M%S')
caminho_completo = r'c:\Users\joao.fonseca\Documents\Backup scan rede'
pasta_registro = f'{caminho_completo} / Backup - {data_atual}'

if not os.path.exists(pasta_registro):
    os.mkdir(f'{pasta_registro}')

log_salvo = os.path.join(pasta_registro, 'logs.txt')
with open(log_salvo,'a') as arquivo:
    for host, status in hosts:
        arquivo.write(f'Host: {host} ---> Status: {status} ---> Info: {platform.system()}\n')
        