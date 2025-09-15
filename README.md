
# ⚙️ MyLittleAnsible 

## 📌 Description

**MyLittleAnsible** est un outil d’Infrastructure as Code (IaC) développé en **Python**, inspiré d’Ansible.  
Il permet de configurer des hôtes distants via **SSH** à l’aide de fichiers **YAML** (inventory + playbooks).  

L’objectif est d’automatiser des tâches système (installation de paquets, gestion de services, copie de fichiers, exécution de commandes, etc.) sur un ou plusieurs serveurs, tout en respectant les principes d’idempotence.

---

## 🛠️ Fonctionnalités principales

- Connexion à un ou plusieurs hôtes via **SSH** (clé, mot de passe ou configuration par défaut).
- Exécution de **playbooks YAML** définissant une suite de tâches (*todos*).
- Modules intégrés :
  - `apt` : gestion des paquets APT  
  - `copy` : copie de fichiers/dossiers vers les hôtes distants  
  - `template` : gestion de templates Jinja2  
  - `service` : administration des services systemd  
  - `command` : exécution de commandes arbitraires  
  - `sysctl` : modification de paramètres kernel  
- Gestion des **logs horodatés** et exploitables (sans `print`, via `logging`).
- Support de l’**idempotence** (ne pas réappliquer une action inutile).
- Options avancées :
  - `--debug` : affichage des stack traces  
  - `--dry-run` : simulation sans appliquer de modifications  

---

## 📂 Structure d’un projet

### Inventory (hosts à configurer)

```yaml
hosts:
  webserver:
    ssh_address: 192.168.1.22
    ssh_port: 22
  bastion:
    ssh_address: 192.168.1.24
    ssh_port: 2222
````

### Playbook (tâches à exécuter)

```yaml
- module: apt
  params:
    name: nginx-common
    state: present

- module: copy
  params:
    src: ./public
    dest: /var/www/public
    backup: true

- module: service
  params:
    name: nginx
    state: started
```

---

## 🚀 Utilisation

### Lancer un playbook

```bash
mla -f todos.yml -i inventory.yml
```

Exemple de sortie :

```
2022-01-06 21:49:16,432 - root - INFO - processing 6 tasks on hosts: 192.168.1.22, 192.168.1.24
2022-01-06 21:49:16,432 - root - INFO - [1] host=192.168.1.22 op=apt name=nginx-common state=present status=OK
2022-01-06 21:49:16,432 - root - INFO - [1] host=192.168.1.24 op=apt name=nginx-common state=present status=CHANGED
...
```

---

## 📦 Installation

### 1️⃣ Cloner le projet

```bash
git clone https://rendu-git.etna-alternance.net/module-9747/activity-52457/group-1041231
cd MyLittleAnsible
```

### 2️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3️⃣ Lancer le programme

```bash
python mla.py -f todos.yml -i inventory.yml
```

---

## 👥 Auteurs

Projet réalisé en binôme dans le cadre du module **TIC-NUX4** (ETNA).
Durée : **3 runs** · Environnement : **Debian**

---

## 📚 Ressources

* [Documentation Ansible](https://docs.ansible.com/)
* [YAML Syntax](https://yaml.org/)
* [Python Logging](https://docs.python.org/3/library/logging.html)
