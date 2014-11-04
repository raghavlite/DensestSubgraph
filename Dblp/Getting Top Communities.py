
# coding: utf-8

## This code reads Data from Dblp data set and gives the best n_d densities

# In[59]:

import pandas as pd;
from numpy import *;
from graph_tool.all import *
import heapq


# In[1]:




# In[2]:

n_d=10;
m=1049866;


# In[2]:




# In[3]:

pwd


# In[4]:

cd ../../../Desktop/Arnab/


# In[5]:

pwd


# In[6]:

ls


# In[6]:




### Creating the graph

# In[7]:

egs=pd.read_csv('./com-dblp.ungraph.txt',delim_whitespace=True);


# In[8]:

edgep=egs.values;


# In[9]:

edgep


# In[ ]:


print edgep;

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

n;
g=Graph(directed=False);


g.add_vertex(max1+1);







for i in range(0,m):
    g.add_edge(g.vertex(edgep[i,0]),g.vertex(edgep[i,1]));
    print "adding edge v",i;
"end for"


# In[ ]:




# In[13]:

g


# In[14]:

g.num_edges()


# In[24]:

cap2=g.new_vertex_property("bool");


# In[24]:




# In[25]:

for v in g.vertices():
    cap2[v]=False;
"end"


# In[25]:




# In[84]:

g.clear_filters()


# In[85]:

g.num_vertices()


# In[85]:




# In[85]:




# In[85]:




# In[85]:




# In[86]:

dens=[0,1,2,3,4,5,6,7,8,9];


# In[87]:

f=open('com-dblp.all.cmty.txt')


# In[87]:




# In[88]:


for j in range(0,10):
    line=f.readline();
    int_list = [int(i) for i in line.split()];
    
    for k in int_list:
        cap2[g.vertex(k)]=True;
    "end for"    
    
    g.set_vertex_filter(cap2,inverted=False);
    
    dens[j]=(g.num_edges()*1.0)/g.num_vertices();
#     dens[j]=g.num_vertices();
    for k in int_list:
        cap2[g.vertex(k)]=False;
    "end for" 
    g.clear_filters();
"End For"
    


# In[88]:




# In[89]:

j=0;
for line in f:
    int_list = [int(i) for i in line.split()];
    
    for k in int_list:
        cap2[g.vertex(k)]=True;
    "end for"    
    
    g.set_vertex_filter(cap2,inverted=False);
    
    densk=(g.num_edges()*1.0)/g.num_vertices();
    heapq.heappush(dens, densk);
    heapq.heappop(dens)
#     dens[j]=g.num_vertices();
    for k in int_list:
        cap2[g.vertex(k)]=False;
    "end for" 
    g.clear_filters();
    print j;
    j++;
"end for"


# In[82]:

dens


# In[90]:


dens



# In[82]:




# In[82]:




# In[83]:

g.num_vertices()


# In[ ]:



