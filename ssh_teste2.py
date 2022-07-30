from paramiko import SSHClient
import paramiko
import time

# VARIÁVEIS
address = '127.0.0.1'
port = '2222'
key = "D:/ambiente_dev/centos7/.vagrant/machines/default/virtualbox/private_key"

# INSTÂNCIA DA CLASSE SSHCLIENT QUE FOI IMPORTADA
ssh = SSHClient()

# PARAMIKO VAI LER TODAS AS CHAVES KNOWN_HOSTS
ssh.load_system_host_keys()

# ACEITAR A CHAVE AUTOMATICAMENTE
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# DEFININDO O SERVIDOR ONDE VAMOS CONECTAR
ssh.connect(hostname=address, port=port, username='vagrant', key_filename=key)

# COMANDOS NECESSÁRIOS PARA INSTALAR PYTHON, SUPERSET, MYSQL, REDIS

commands_python = ['sudo yum update -y', 'sudo yum install -y python3',
                   'sudo yum install gcc openssl-devel bzip2-devel libffi-devel -y']

commands_superset = ['pip install superset', 'sudo yum install mlocate', 'sudo updatedb', 'sudo yum install gcc', 'sudo yum install gcc-c++', 'pip install superset',
                     'superset db upgrade', 'export FLASK_APP=superset', 'flask fab create-admin', 'superset init', 'superset run -p 8080 –with-threads –reload –debugger']

commands_mysql = ['sudo yum update', 'sudo yum install wget -y', 'sudo wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm', 'sudo rpm -Uvh mysql80-community-release-el7-3.noarch.rpm',
                  'sudo yum install -y mysql-server']

commands_redis = ['sudo yum install epel-release yum-utils', 'sudo yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm', 'sudo yum-config-manager --enable remi', 'sudo yum install redis',
                  'sudo systemctl start redis', 'sudo systemctl enable redis']

# INSTALANDO PYTHON 3

for comand in commands_python:
    print(f"{'#'*10} Excecuting the Command : {comand} {'#'*10}")
    stdin, stdout, stderr = ssh.exec_command(comand)
    time.sleep(.5)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

# INSTALANDO SUPERSET

for comand in commands_superset:
    print(f"{'#'*10} Excecuting the Command : {comand} {'#'*10}")
    stdin, stdout, stderr = ssh.exec_command(comand)
    time.sleep(.5)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

# INSTALANDO MYSQL

for comand in commands_mysql:
    print(f"{'#'*10} Excecuting the Command : {comand} {'#'*10}")
    stdin, stdout, stderr = ssh.exec_command(comand)
    time.sleep(.5)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

# INSTALANDO JAVA

for comand in commands_redis:
    print(f"{'#'*10} Excecuting the Command : {comand} {'#'*10}")
    stdin, stdout, stderr = ssh.exec_command(comand)
    time.sleep(.5)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

ssh.close()
