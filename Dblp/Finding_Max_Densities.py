


m=1049866;


import pandas as pd;
from numpy import *;
from graph_tool.all import *

def modifycap(g,s,t,go,gn,cap):
    
    i=0;

    for e in g.edges():
        if  e.target()==t:    
            cap[e]=cap[e]-2*go+2*gn
        "end"
        # print "modifying cap",i;
        i+=1;
    "end for"
    
    
"end func"
        
        

# <codecell>

def maxdsubgraph(g,s,t,m,n,cap):
    go=0.0;
    l=0.0;
    u=m*1.0;
    b=1.0/(n*(n-1));
    res=-123;
    
    # print "Inside MaxdSubgraph";
    
    
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
        
        print "into maxflow";
        res23 = push_relabel_max_flow(g, s, t, cap);
        
        #"""
        part = min_st_cut(g, s, cap, res23);
        #
        
        g.set_vertex_filter(part, inverted=False);
        print "out of maxflow ";
        
        
        
        if g.num_vertices()==1:
            print "u reduced";
            u=gn;
            
        else :
            print "l increased";
            l=gn;
            res=part;
            print "Density is equal to %0.9f"%(((g.num_edges()-g.num_vertices()+1)*0.5)/(g.num_vertices()-1));
        "end if"
        go=gn;

        
        g.clear_filters();
        #"""
    "end while"
    if(res!=-123):
        g.set_vertex_filter(res,inverted=False);
    "end if"
    

"end func"

# <codecell>

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
        elif v==t :
        	"blah";
                       
        else :
            
            cap2[v]=True;
        "end if"
        
    "end for"
    
    #res = boykov_kolmogorov_max_flow(G, s, t, cap);
    #part = min_st_cut(G, s, cap, res);
    #G.set_vertex_filter(part,inverted=False);
    
    g.set_vertex_filter(cap2,inverted=False);
    
    #graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=20,output_size=(500, 500), output="two-nodes.png");
    
    
    print "Density is equal to",g.num_edges()*1.0/g.num_vertices();
    return (g.num_edges()*1.0)/g.num_vertices();

"end def"



egs=pd.read_csv('./com-dblp.ungraph.txt',delim_whitespace=True);




edgep=egs.values;


max1=0;


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



g=Graph(directed=False);
n=max1+1;

g.add_vertex(max1+1);







for i in range(0,m):
    g.add_edge(g.vertex(edgep[i,0]),g.vertex(edgep[i,1]));
    print "adding edge v",i;
"end for"




dsg(g,g.num_edges(),g.num_vertices());