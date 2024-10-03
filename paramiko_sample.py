import paramiko


class SSH_Manager:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    def connect(self,hostname):
        self.ssh.connect(hostname=hostname,username=self.username,password=self.password)

    def execute_command(self,commands):
        stdin, stdout, stderr = self.ssh.exec_command(commands)
        output = stdout.read().decode('utf-8') + stderr.read().decode('utf-8')
        exit_code = stdout.channel.recv_exit_status()
        return exit_code,output

    def copy_file_to_remote(self,localfile,remotefile):
        sftp = self.ssh.open_sftp()
        sftp.put(localfile,remotefile)
        sftp.close()

    def copy_file_from_remote(self,remotefile,localfile):
        sftp = self.ssh.open_sftp()
        sftp.get(remotefile, localfile)
        sftp.close()


    def close(self):
        self.ssh.close()



if __name__ == "__main__":
    username = ""
    password = ""
    hostname = ""
    sshmanager = SSH_Manager(username,password)

    try:
        sshmanager.connect(hostname)
        cmds = ["whoami"]
        errcode, output = sshmanager.execute_command(cmds)
        if errcode:
            print("Executed")
        else:
            print("Unsuccessful")

        print(output)
    except Exception as err:
        print("Error: " + err)
    finally:
        sshmanager.close()