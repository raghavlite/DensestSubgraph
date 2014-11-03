# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>



# <codecell>

import pylab as py

# <codecell>

from numpy import *

# <codecell>

from graph_tool.all import *





#################################################################Set the graph vertices n_g;;######################################################################################################################################
n_g=22;

# <codecell>

# g=Graph(directed=False)

# # <codecell>

# for i in range(0,5):
#     g.add_vertex() ;
#     print "added no",i;
# "End" 

# # <codecell>

# g.add_edge(g.vertex(0), g.vertex(1))
# g.add_edge(g.vertex(1), g.vertex(2))
# g.add_edge(g.vertex(2), g.vertex(3))
# g.add_edge(g.vertex(4), g.vertex(3))
# g.add_edge(g.vertex(1), g.vertex(4))
# g.add_edge(g.vertex(2), g.vertex(4))

# # <codecell>

# graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")

# # <codecell>

# g.add_edge(g.vertex(1), g.vertex(3))

# # <codecell>

# graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")

# # <codecell>


# g.add_vertex(5);

# # <codecell>

# graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")

# # <codecell>

# g.add_edge(g.vertex(7),g.vertex(4));

# # <codecell>

# g.add_edge(g.vertex(8),g.vertex(3));

# # <codecell>

# g.add_edge(g.vertex(2),g.vertex(5));

# # <codecell>

# g.add_edge(g.vertex(6),g.vertex(9));

# # <codecell>

# g.add_edge(g.vertex(5),g.vertex(6));

# # <codecell>

# graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")

# # <codecell>

def modifycap(g,s,t,go,gn,cap):
    
    for e in g.edges():
        if  e.target()==t:    
            cap[e]=cap[e]-2*go+2*gn
        "end"
    "end for"
    
    
"end func"
        
        

# <codecell>

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
            print "Density is equal to %0.9f"%(((g.num_edges()-g.num_vertices()+1)*0.5)/(g.num_vertices()-1);
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
        elif v==t:
            "blah";                       
        else :
            
            cap2[v]=True;
        "end if"
        
    "end for"
    
    #res = boykov_kolmogorov_max_flow(G, s, t, cap);
    #part = min_st_cut(G, s, cap, res);
    #G.set_vertex_filter(part,inverted=False);
    
    g.set_vertex_filter(cap2,inverted=False);
    
    graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=20,output_size=(500, 500), output="two-nodes.png");
    
    
    print "Density is equal to",g.num_edges()*1.0/g.num_vertices();
    return (g.num_edges()*1.0)/g.num_vertices();

"end def"

# <codecell>



# <codecell>


# <codecell>

from numpy.random import *

# <codecell>

def corr(a, b):
    if a == b:
        return 0.999
    else:
        return 0.001
    "End if"
"End def"

# <codecell>

g1, bm = random_graph(n_g, lambda: poisson(10), directed=False,model="blockmodel-traditional",block_membership=lambda: randint(1,10),vertex_corr=corr)

# <codecell>

# #####graph_draw(g1, vertex_fill_color=bm, edge_color="black", output="blockmodel.pdf")

# <codecell>







loci=0;

# <codecell>

def combi(g,p,n,fil) :

    if (n==p) :
        global loci;
        print loci;
        loci+=1;
        g.set_vertex_filter(fil,inverted=False);
        if (g.num_vertices()==0) :
            g.clear_filters();
            return 0;
        
        d=(g.num_edges()*1.0)/g.num_vertices();
        g.clear_filters();
        return d;
    "End if"


    fil[g.vertex(p)]=0;
    k=combi(g,p+1,n,fil);

    fil[g.vertex(p)]=1;
    l=combi(g,p+1,n,fil);


    if k>l :
        return k;
    else :
        return l; 
    "end if"
        
"end def"


# <codecell>

def checker(g) :
    
    m=g.num_edges();
    n=g.num_vertices();




    d=(m*1.0)/n;


    fil=g.new_vertex_property("bool");

    for i in range(0,n):
        fil[g.vertex(i)]=1;

    "end for"
    

    max2=combi(g,0,n,fil);
    
    print "Max Density found is",max2;



"end def"

# <codecell>


# max1=dsg(g1,g1.num_edges(),g1.num_vertices());

# g1.clear_filters();

# checker(g1);



# print "Algo Max",max1;
# <codecell>


# <codecell>


# <codecell>


# <codecell>


