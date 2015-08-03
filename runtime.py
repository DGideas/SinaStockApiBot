#!/usr/bin/env python3
__author__='DGideas';
try:
	os.chdir(os.path.dirname(sys.argv[0]));
except FileNotFoundError:
	pass;
except OSError:
	pass;

import sys;
import codecs;
import urllib.request;

f=codecs.open('runtime.csv','a','utf8');
i=1
while i<=2000:
    info=urllib.request.urlopen('http://hq.sinajs.cn/list=sz'+str(i)).read();
    f.write(info+'\n');
    i=i+1;
