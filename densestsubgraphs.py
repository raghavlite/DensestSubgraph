








from graph_tool.all import *;



g=Graph();


for i in range(0,5):
    g.add_vertex() ;
    print "added no",i;
"End"  




g.add_edge(g.vertex(0), g.vertex(1));
g.add_edge(g.vertex(1), g.vertex(2));
g.add_edge(g.vertex(2), g.vertex(3));
g.add_edge(g.vertex(4), g.vertex(3));
g.add_edge(g.vertex(1), g.vertex(4));
g.add_edge(g.vertex(2), g.vertex(4));




graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png");


g.add_edge(g.vertex(1), g.vertex(3));



graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png");




for v in g.vertices():
    print(v);
for e in g.edges():
    print(e);





def modifycap(g,s,t,go,gn,cap):
    
    for e in g.edges():
        if  e.target()==t:    
            cap[e]=cap[e]-2*go+2*gn
        "end"
    "end for"
"end func"
        
        
    




def maxdsubgraph(g,n,m,cap):
  
    
    go=0;
    l=0;
    u=m;
    b=1/(n*(n-1));
    res=-123;

    print "Inside MaxdSubgraph";
    
    """
    while (u-l)>b :
        
        gn=(u+l)/2;
        
        modifycap(g,g.vertex(m),g.vertex(m+1),go,gn,cap)
        
        #get cut
        s=g.vertex(m);
        t=g.vertex(m+1);
        res = boykov_kolmogorov_max_flow(g, s, t, cap)
        part = min_st_cut(g, s, cap, res)
        #
        g.set_vertex_filter(part, inverted=False);
        
        
        if g.num_vertices()==1:
            print "min cut 1 obtained";
            u=gn;
            
        else :
            l=gn;
            res=part;
        "end if"
        go=gn;
        g.clear_filters();
        
    "end while"
    if(res!=-123):
        g.set_vertex_filter(res,inverted=false);
    "end if"
    """

"end func"






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
    
    maxdsubgraph(G,n,m,cap);
    
    graph_draw(G, vertex_text=G.vertex_index, vertex_font_size=20,output_size=(1500, 1500), output="two-nodes.png");

"end def"




dsg(g,g.num_edges(),g.num_vertices());





















