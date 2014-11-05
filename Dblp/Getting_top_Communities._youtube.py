


import pandas as pd;
from numpy import *;
from graph_tool.all import *
import heapq




m=2987624;
max1=0;



egs=pd.read_csv('./com-youtube.ungraph.txt',delim_whitespace=True);



edgep=egs.values;


for i in range(0,m):
    if (edgep[i,0]>max1) :
        max1=edgep[i,0];
    "end if"
     
    if (edgep[i,1]>max1) : 
        max1=edgep[i,1];
    "end if"
    print "compting max vretex",i; 

"end for"
n=max1+1;