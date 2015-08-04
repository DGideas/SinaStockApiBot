#!/usr/bin/env python3
__author__='DGideas';
import sys;
import codecs;
import os;
import subprocess;
subprocess.call('rm -f stocklist.csv',shell=True);

try:
	os.chdir(os.path.dirname(sys.argv[0]));
except FileNotFoundError:
	pass;
except OSError:
	pass;

f=codecs.open('runtimesh.csv','r','utf8');
for line in f.readlines():
	stock=line[11:19];
	out=codecs.open('stocklist.csv','a','utf8');
	out.write(stock+'\n');
	print('Fetch '+str(stock));
f=codecs.open('runtimesz.csv','r','utf8');
for line in f.readlines():
	stock=line[11:19];
	out=codecs.open('stocklist.csv','a','utf8');
	out.write(stock+'\n');
	print('Fetch '+str(stock));
f=codecs.open('runtimecyb.csv','r','utf8');
for line in f.readlines():
	stock=line[11:19];
	out=codecs.open('stocklist.csv','a','utf8');
	out.write(stock+'\n');
	print('Fetch '+str(stock));
