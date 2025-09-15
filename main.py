import click
import os
import yaml

import logging
from getpass import getuser

from class_hosts import Host
from executor import Executor

def load_yaml(file_path):
    """Charge un fichier YAML s'il existe."""
    if not os.path.isfile(file_path):
        print(f"Erreur : Le fichier {file_path} n'existe pas.")
        exit(1)
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
    

def get_hosts(inventory):

    inventory_data = load_yaml(inventory) 

    list_host = []

    if "hosts" in inventory_data:
        inventory_data = inventory_data['hosts']

        for index, data in enumerate(inventory_data):
            machine = Host(data, inventory_data)
            machine.id = index + 1

            list_host.append(machine)

        return list_host
    else:
        return False

def get_todos(todos):
    todos_data = load_yaml(todos)

    for todo in todos_data:
        if "module" not in todo or "params" not in todo:
            return False

    return todos_data

def mainLogging(list_host, list_todos):
    FORMAT = '%(asctime)s - %(user)s - %(levelname)s - processing %(numberProcess)s on hosts: %(hostList)s'

    logging.basicConfig(format=FORMAT)

    logger = logging.getLogger('tcpserver')
    logger.setLevel(logging.DEBUG)

    nbr = len(list_host) * len(list_todos)

    strHosts = ""

    for index, host in enumerate(list_host):

        strHosts += host.ssh_address 

        if index + 1 != len(list_host):
            strHosts += ', '

    d = {'user': 'root', 'numberProcess': nbr, 'hostList': strHosts}

    logger_adapter = logging.LoggerAdapter(logger, d)
    logger_adapter.info('')



@click.command()
@click.option('-f', '--todos', required=True, type=click.Path(exists=True), help="Fichier todos.yml")
@click.option('-i', '--inventory', required=True, type=click.Path(exists=True), help="Fichier inventory.yml")
@click.option('--debug', is_flag=True, help="Debug du code")
@click.option('--dry-run', is_flag=True, help="Ne pas éxécuter le code")
def main(todos, inventory, dry_run, debug):

    list_host = get_hosts(inventory) 
    list_todos = get_todos(todos)

    # mainLogging(list_host, list_todos)



    for host in list_host:
        if host.client == None:
            print("Erreur connexion")
            return

    Exec = Executor



    for host in list_host:

        for todo in list_todos:

            module = todo['module']

            if module == "apt":
                Exec.aptModule(todo, host, debug, dry_run)

            elif module == "copy":
                print('module copy 1')

            elif module == "template":
                print('module template 2')

            elif module == "service":
                Exec.serviceModule(todo, host, debug, dry_run)

            elif module == "command":
                Exec.cmdModule(todo, host, debug, dry_run)

            elif module == "sysctl":
                print('module sysctl 5')

if __name__ == "__main__":
    main()
