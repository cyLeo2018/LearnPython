#! /usr/bin/env python3

#20180423-cy


import ast
import paramiko
import subprocess
import pipes
import sys

def sshclient_execmd(hostname, port, username, password, execmd):
    '''
    使用python模拟SSH客户端登录远程服务器
    登录后执行命令execmd
    '''
    paramiko.util.log_to_file("../Log/paramiko.log") #日志
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command(execmd)
    stdin.write("Y")
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()
    #print(str_out)
    with open('../Data/'+hostname+'.dat','w') as f:
        f.write(str_out)
    s.close()

def monitorScriptUpload(hostname, port, username, password):
    '''
    检查脚本上传至远程服务器
    无论是否存在脚本，都重新上传
    '''
    try:
        ssh = paramiko.Transport((hostname, port))
        ssh.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(ssh)
        #files = ("CPU_check.sh","Memory_check.sh","Disk_check.sh",)
        file = "check.sh"
        sftp.put('check.sh', 'check.sh')
        print('检查脚本',file,'上传成功!')
    except Exception as e:
        print(e)



if __name__ == '__main__':

    host_list = []
    #读取配置文件Config/SSHConfig 获取主机列表信息
    with open('../Config/SSHConfig', 'r') as f:
        d = f.readlines()
        for i in d:
            host_list.append(ast.literal_eval(i.replace('\n', '')))
    f.close()
    for host in host_list:
        print(host['company'], host['ip'])
        monitorScriptUpload(host['ip'], host['port'], host['username'], host['password']) #上传脚本
        sshclient_execmd(host['ip'], host['port'], host['username'], host['password'], 'chmod u+x check.sh') #增加权限
        sshclient_execmd(host['ip'], host['port'], host['username'], host['password'], './check.sh')