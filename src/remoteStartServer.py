#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect
import os

print os.getcwd()


def ssh_cmd(ip, passwd, cmd):
	ret = -1
	ssh = pexpect.spawn('ssh gwac@%s "%s"'%(ip, cmd))
	try:
		  i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)
		  if i == 0:
		  	ssh.sendline(passwd)
		  elif i == 1:
		  	ssh.sendline('yes\n')
		  	ssh.expect('password: ')
		  	ssh.sendline(passwd)
		        ssh.sendline(cmd)
		        r = ssh.read()
		        print r
		        ret = 0
	except pexpect.EOF:
		print "EOF"
		ssh.close()
		ret = -1
	except pexpect.TIMEOUT:
		print "TIMEOUT"
		ssh.close()
		ret = -2
		
	return ret


if __name__=='__main__':
	ssh_cmd("190.168.1.11", "123456", "ls")
