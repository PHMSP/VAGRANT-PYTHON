# DevOps - Vagrant/Python 

# Teste 1

Subir uma VM com Vagrantfile 

(CentOS 7.x com 2 CPUs (2 cores de processador), 4 GB de memória RAM e 50gb de HD chamada “teste-zeppelin”)

```bash
Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.box_download_insecure = true
  
  config.disksize.size = "50GB"

  config.vm.network "forwarded_port", guest: 8888, host: 8888 

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 4096
    vb.cpus = 2
    vb.name = "teste_zeppelin"
  end

end
```

![vagarant vm](https://user-images.githubusercontent.com/100800875/181829634-32a0a0ec-ce63-4195-b093-084dcf57b589.PNG)


OBS: Para alterar o HD foi necessário instalar o plugin "vagrant plugin install vagrant-disksize"

Documentação: https://www.vagrantup.com/docs

Fazendo as configuraçoes da VM com Python.

Python Script (Conectar SSH, instalar JAVA e Apache Zeppelin, subir o webserver Zeppelin na porta:8888)

OBS: Utilizado o módulo Paramiko,para fazer conexões via SSH. (pip install paramiko)

Conectando-se a VM

```python 
from paramiko import SSHClient
import paramiko

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
```

Declarando os comandos necessário para a instalação do Java e Zeppelin

```python
commands_java = ['sudo yum clean all', 'sudo yum update -y', 'sudo yum install wget -y',
                 'sudo yum install java-1.8.0-openjdk -y', 'export JAVA_HOME=/usr/lib/java-1.8.0']

commands_zeppelin = ['wget https://ftp.unicamp.br/pub/apache/zeppelin/zeppelin-0.9.0/zeppelin-0.9.0-bin-all.tgz', 'sudo tar xf zeppelin-*-bin-all.tgz -C /opt', 'sudo mv /opt/zeppelin-*-bin-all /opt/zeppelin','sudo sed -i "s/<value>8080<\/value>/<value>8888<\/value>/g" /opt/zeppelin/conf/zeppelin-site.xml', 'sudo systemctl enable zeppelin', 'sudo systemctl start zeppelin']
```

Executando o comando na VM e vendo os valores de retorno.

```python
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
```

Quando o comando é executado, esse método retorna uma tupla com 3 valores:

Standard Input (Entrada padrão, normalmente uma entrada do teclado) = stdin

Standard Output (Saída padrão, o que aparece na tela) = stdout

Stander Error (Saída de Error, mensagem de erro mostrada na tela) = stderr

Depois de recebidos os valores retornados pelo "exec_command", precisamos saber se o comando deu erro ou não, para isso foi feito esse if.

Então, se for retornado um erro, a condição entra no primeiro bloco de instruções fazendo um print do erro do comando, caso contrário a saída padrão do comando será retornada na tela.

![teste1ruun](https://user-images.githubusercontent.com/100800875/181859616-a5ce8c8e-d811-4f51-b772-d7de310fd9c0.jpg)

Documentação: https://docs.paramiko.org/en/stable/api/client.html

Documentação: https://zeppelin.apache.org/docs/latest/quickstart/install.html

Referência: https://www.vultr.com/pt/docs/how-to-install-apache-zeppelin-on-centos-7/

Referência: https://www.vivaolinux.com.br/artigo/paramiko-Python-SSH

Referência: https://www.youtube.com/watch?v=add-89Jlt9E

# Teste 2
Utilizar a mesma VM anterior e criar um Script Python para instalar Phython 3.6 e Apache Superset, suba o webserver do Superset.

Declarando os comandos necessário para a instalação do Java e Zeppelin

```python
commands_python = ['sudo yum update -y', 'sudo yum install -y python3','sudo yum install gcc openssl-devel bzip2-devel libffi-devel -y']

commands_superset = ['pip install superset', 'sudo yum install mlocate', 'sudo updatedb', 'sudo yum install gcc', 'sudo yum install gcc-c++', 'pip install superset',
'superset db upgrade', 'export FLASK_APP=superset', 'flask fab create-admin', 'superset init', 'superset run -p 8080 –with-threads –reload –debugger']

commands_mysql = ['sudo yum update', 'sudo yum install wget -y', 'sudo wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm', 'sudo rpm -Uvh mysql80-community-release-el7-3.noarch.rpm', 'sudo yum install -y mysql-server']

commands_redis = ['sudo yum install epel-release yum-utils', 'sudo yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm', 'sudo yum-config-manager --enable remi', 'sudo yum install redis', 'sudo systemctl start redis', 'sudo systemctl enable redis']
```

Executando o comando na VM e vendo os valores de retorno.

```python
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
```

Referência: https://www.liquidweb.com/kb/how-to-install-python-3-on-centos-7/

Referência: https://aichamp.wordpress.com/2019/11/20/installing-apache-superset-into-centos-7-with-python-3-7/

Referência: https://www.hostinger.com.br/tutoriais/como-instalar-mysql-no-centos-7

Referência: https://linuxize.com/post/how-to-install-and-configure-redis-on-centos-7/

Documentos: https://superset.apache.org/docs/databases/mysql
