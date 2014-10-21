
# coding: utf-8

# In[242]:

get_ipython().magic(u'matplotlib inline')


# In[243]:

import pylab as py


# In[244]:

import numpy as np


# In[245]:

from graph_tool.all import *


### Creating a random Undirected Graph for evaluation

# In[246]:

g=Graph(directed=False)


# In[247]:

for i in range(0,5):
    g.add_vertex() ;
    print "added no",i;
"End" 


# In[248]:

g.add_edge(g.vertex(0), g.vertex(1))
g.add_edge(g.vertex(1), g.vertex(2))
g.add_edge(g.vertex(2), g.vertex(3))
g.add_edge(g.vertex(4), g.vertex(3))
g.add_edge(g.vertex(1), g.vertex(4))
g.add_edge(g.vertex(2), g.vertex(4))


# In[249]:

graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")


# In[250]:

g.add_edge(g.vertex(1), g.vertex(3))


# In[251]:

graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")


# In[252]:


g.add_vertex(5);


# In[253]:

graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")


# In[254]:

g.add_edge(g.vertex(7),g.vertex(4));


# In[255]:

g.add_edge(g.vertex(8),g.vertex(3));


# In[256]:

g.add_edge(g.vertex(2),g.vertex(5));


# In[257]:

g.add_edge(g.vertex(6),g.vertex(9));


# In[258]:

g.add_edge(g.vertex(5),g.vertex(6));


# In[259]:

graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")


### Subroutine used by maxdsubgraph for modification of flow capacities

# In[260]:

def modifycap(g,s,t,go,gn,cap):
    
    for e in g.edges():
        if  e.target()==t:    
            cap[e]=cap[e]-2*go+2*gn
        "end"
    "end for"
    
    
"end func"
        
        


### Subroutine which filters off unwanted nodes using the Maxflow min cut theoram

# In[266]:

def maxdsubgraph(g,s,t,m,n,cap):
    go=0.0;
    l=0.0;
    u=m;
    b=1.0/(n*(n-1));
    res=-123;

    print "Inside MaxdSubgraph";
    
    
    for e in g.edges():
        print cap[e],e.source(),e.target();
    "end for"
    
    
    
    
    
    while (u-l)>b :
        
        print "value of l",l,"value of u",u,"value of b",b;
        
        gn=(u+l)/2;
        
        modifycap(g,s,t,go,gn,cap);
        
        print "yeah done with while";
        
        #"""
        
        
        #get cut
        #s=g.vertex(m);
        #t=g.vertex(m+1);
        
        
        res23 = push_relabel_max_flow(g, s, t, cap);
        
        #"""
        part = min_st_cut(g, s, cap, res23);
        #
        
        g.set_vertex_filter(part, inverted=False);
        
        
        
        
        if g.num_vertices()==1:
            print "u reduced";
            u=gn;
            
        else :
            print "l increased";
            l=gn;
            res=part;
        "end if"
        go=gn;
        g.clear_filters();
        #"""
    "end while"
    if(res!=-123):
        g.set_vertex_filter(res,inverted=False);
    "end if"
    

"end func"


### Worker Function : Sets up thr priliminary G graph with dual edges and capacity 1

# In[262]:

def dsg(g,m,n):
    
    print "m ",m,"n",n,"\n\n\n";
    
    G=Graph();
    
    G.add_vertex(n);
    
    for e in g.edges():
        G.add_edge(e.source(),e.target());
        G.add_edge(e.target(),e.source());
    "End for"
    
    s=G.add_vertex();
    t=G.add_vertex();
    
    
  
    
    for i in range(0,n):
        G.add_edge(s,G.vertex(i));
        G.add_edge(G.vertex(i),t);
    "End For"
    
    
    cap = G.new_edge_property("float")                

    
    
    
    for e in G.edges():
        print "Source",e.source(),"target",e.target();
        
        if e.source()==s:
 #           print "found source";
            cap[e]=m;
        elif e.target()==t:
 #           print "found target";
            cap[e]=m-(e.source().in_degree()-1);
        else :
#            print "else mei";
            cap[e]=1;
        "end if"
    "end for"
    
    
    
    for e in G.edges():
        print cap[e],e.source(),e.target();
    "end for"    
    
    maxdsubgraph(G,s,t,m,n,cap);
    
    
    cap2=g.new_vertex_property("bool");
    
    
    for v in g.vertices():
        cap2[v]=False;
    "end"
    
    for v in G.vertices():
        
        if v==s:
            "blah";
                       
        else :
            
            cap2[v]=True;
        "end if"
        
    "end for"
    
    #res = boykov_kolmogorov_max_flow(G, s, t, cap);
    #part = min_st_cut(G, s, cap, res);
    #G.set_vertex_filter(part,inverted=False);
    
    g.set_vertex_filter(cap2,inverted=False);
    
    print "\n\n\n\nDensest Subgraph is ::";
    
    graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=20,output_size=(500, 500), output="two-nodes.png");
    
    
    print "Density is equal to",(g.num_edges()*1.0)/g.num_vertices();
    

"end def"


### Densest Subgraph Function used on the graph created

# In[263]:

dsg(g,g.num_edges(),g.num_vertices());


# In[263]:




# In[122]:




# In[ ]:



