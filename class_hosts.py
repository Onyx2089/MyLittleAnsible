
import paramiko

class Host:

    def __init__(self, name, data):
        data = data[name]

        self.id = None
        self.client = None
        self.name = name
        self.ssh_address = data['ssh_address']
        self.ssh_port = data['ssh_port']

        if "ssh_user" in data:
            self.ssh_user = data['ssh_user']
        else:
            self.ssh_user = None

        if "ssh_password" in data:
            self.ssh_password = data['ssh_password']
        else:
            self.ssh_password = None

        self.get_client()


    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Adress: {self.ssh_address}, Port: {self.ssh_port}, User: {self.ssh_user}, Pwd: {self.ssh_password}"

    def connexionMethod(self):
        if self.userPwd() : 
            return 1
        else:
            return -1

    def userPwd(self):
        if self.ssh_user is not None and self.ssh_password is not None:
            return True
        else:
            return False

    def connexionOk(self):
        if self.ssh_user is not None and self.ssh_password is not None:
            return True
        else:
            return False
        
    def get_client(self):
        client = paramiko.SSHClient()

        # Chargement des clés par défaut (si nécessaire)
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Autorise les connexions à des hôtes inconnus

        try:

            client.connect(self.ssh_address, port=self.ssh_port, username=self.ssh_user, password=self.ssh_password)
            # print("Connexion SSH réussie!")
            self.client = client

        except Exception as e:
            print(f"Erreur de connexion SSH: {e}")
            self.client = None   

    
