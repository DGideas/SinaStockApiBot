#!/usr/bin/env python3
__author__='DGideas';
import os;
import sys;
import codecs;
import urllib.request;

try:
	os.chdir(os.path.dirname(sys.argv[0]));
except FileNotFoundError:
	pass;
except OSError:
	pass;

f=codecs.open('runtime.csv','a','utf8');
i=1;
stri='';
while i<=2000:
	p=6-int(len(str(i)));
	stri=str(i);
	while p>0:
		stri='0'+str(stri);
		p=p-1;
	print(stri);
	info=urllib.request.urlopen('http://hq.sinajs.cn/list=sz'+str(stri));
	f.write(str(info.read())+'\n');
	i=i+1;
