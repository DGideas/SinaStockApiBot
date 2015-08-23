#!/usr/bin/env python3
__author__='DGideas';
import os;
import sys;
import codecs;
import urllib.request;
import subprocess;

try:
	os.chdir(os.path.dirname(sys.argv[0]));
except FileNotFoundError:
	pass;
except OSError:
	pass;

f=codecs.open('stocklist.csv','r','utf8');
for line in f.readlines():
	stock=line[0:-1]
	try:
		urllib.request.urlopen('http://203.90.242.126/list='+stock); #equal to hq.sinajs.cn
	except:
		print('Fetch an error, pass');
	else:
		info=urllib.request.urlopen('http://203.90.242.126/list='+stock); #equal to hq.sinajs.cn
		print(stock);
		strinfo=info.read();
		strinfo=strinfo.decode('gb2312')[0:-1];
		f=codecs.open('runtime.tmp','a','utf8');
		f.write(strinfo+'\n');
		f.close();
subprocess.call('rm -f runtime.csv',shell=True);
subprocess.call('mv runtime.tmp runtime.csv',shell=True);
