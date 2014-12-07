#-*- coding: utf-8 -*-
#!/usr/bin/python 
import paramiko
import threading

def ssh2(ip,username,passwd,cmd):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip,22,username,passwd,timeout=5)
		for m in cmd:
			stdin, stdout, stderr = ssh.exec_command(m)
#        stdin.write("Y")   #简单交互，输入 ‘Y’ 
			out = stdout.readlines()
            #屏幕输出
		for o in out:
			print o,
		print '%s\tOK\n'%(ip)
		ssh.close()
	except :
		print '%s\tError\n'%(ip)

if __name__=='__main__':
	
	username = "root"  #用户名
	passwd = "123456"    #密码
	threads = [12]   #多线程	print "Begin......"
	
	cmd_start_service = ['service u9000usbpermit stop','nohup service u9000usbpermit start &'] #shell 指令
	cmd_reboot = ['reboot']
	cmd_cp_file = ['scp /opt/apogee/scripts/tele_init.tcl root@190.168.1.:/opt/apogee/scripts/tele_init.tcl']
	cmd_rm_fits_files = ['rm -rf /data/*140317']
	cmd_shutdown = ['init 0']
	
	cmd_to_run = "ls"
	
	
	for i in range(11, 23):
		ip = '190.168.1.'+str(i)
		#cmd_edit_fits_files = ['ls /data/m{:0>2d}_*.fits'.format(i-10)]
		#cmd_cp_file = ['cp /opt/apogee/scripts/apogeeserver.tcl root@190.168.1.{}:/opt/apogee/scripts/apogeeserver.tcl'.format(i)]
		a=threading.Thread(target=ssh2, args=(ip,username,passwd,cmd_to_run))
		a.start() 
	