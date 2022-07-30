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

# COMANDOS NECESSÁRIOS PARA INSTALAR JAVA e ZEPPELIN
commands_java = ['sudo yum clean all', 'sudo yum update -y', 'sudo yum install wget -y',
                 'sudo yum install java-1.8.0-openjdk -y', 'export JAVA_HOME=/usr/lib/java-1.8.0']

commands_zeppelin = ['wget https://ftp.unicamp.br/pub/apache/zeppelin/zeppelin-0.9.0/zeppelin-0.9.0-bin-all.tgz', 'sudo tar xf zeppelin-*-bin-all.tgz -C /opt', 'sudo mv /opt/zeppelin-*-bin-all /opt/zeppelin',
                     'sudo sed -i "s/<value>8080<\/value>/<value>8888<\/value>/g" /opt/zeppelin/conf/zeppelin-site.xml', 'sudo systemctl enable zeppelin', 'sudo systemctl start zeppelin']


# INSTALANDO JAVA
for comand in commands_java:
    print(f"{'#'*10} Excecuting the Command : {comand} {'#'*10}")
    stdin, stdout, stderr = ssh.exec_command(comand)
    time.sleep(.5)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)


# INSTALANDO ZEPPELIN
for comand in commands_zeppelin:
    print(f"{'#'*10} Excecuting the Command : {comand} {'#'*10}")
    stdin, stdout, stderr = ssh.exec_command(comand)
    time.sleep(.5)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

ssh.close()
