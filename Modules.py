
# coding: utf-8

# In[ ]:


import json
from os.path import expanduser
import itertools
from collections import defaultdict
import math
import networkx as nx
import heapq
import matplotlib.pyplot as plt


# In[ ]:


def pubblicationDictionary(json):
    pubb_dict = {}
    for pubblication in json:
        for author in pubblication["authors"]:
            if "&" in author["author"]:
                pass
            else:
                try:
                    pubb_dict[(author["author"],author["author_id"])] += [(pubblication["id_publication_int"],pubblication["id_publication"])]
                except:
                    pubb_dict[(author["author"],author["author_id"])] = [(pubblication["id_publication_int"],pubblication["id_publication"])]
    return(pubb_dict)


# In[ ]:


def Jaccard(a,b):
    jaccard = (abs(len(list(set(a)|set(b))))-abs(len(list(set(a)&set(b)))))/abs(len(list(set(a)|set(b))))
    return jaccard


# In[ ]:


#hop distance number of edjes between two nodes
def hop_distance(G,start,end):
    p = nx.shortest_path(G,source=start, target=end)
    return (len(p)-1)


# In[ ]:


def graphConference(json, int_conference):
    conf_sublist = []
    for publ in json:
        if publ['id_conference_int'] == int_conference:
            for aut in publ['authors']:
                conf_sublist.append(aut['author_id'])
    set(conf_sublist)
    newG = G.subgraph(conf_sublist)
    return newG


# In[ ]:


def get_id_author(authorName):
    autID = {}
    for pubblication in database:
        for author in pubblication["authors"]:
            try:
                autID[author["author"]].append(author["author_id"])
            except:
                autID[author["author"]] = author["author_id"]
    return autID[authorName]


# In[ ]:


def author_dist(author, d):
    a = get_id_author(author)
    nodelist = nx.single_source_shortest_path_length(G, source=a, cutoff=d)
    subg = G.subgraph([k for k,v in nodelist.items()])
    return subg


# In[ ]:


def Dijkstra(G, start,end):
    dist={}
    dist[start]=0
   
    for node in nx.nodes(G):
        if node!= start:
            dist[node]=math.inf
        else:
            dist[node]=0
    visited={}
    queue=[(value, key) for key,value in dist.items()]
    heapq.heapify(queue)
    while len(queue) != 0:
        u= heapq.heappop(queue) ##[1]min node #[0]current weight
        visited[u[1]]=u[0]
        for node in  G.neighbors(u[1]):
            weight=u[0]+ G.get_edge_data(u[1],node)['weight']
            if node not in visited or weight < visited[node]:
                visited[node] = weight
                heapq.heappush(queue, (weight, node))
                
                
        if u[1]== end : 
            return (visited[end])    


# In[ ]:


def distance_to_aris(authorid):
    end=get_id_author("aris anagnostopoulos")
    distance=Dijkstra(G, authorid,end)
    if distance != math.inf:
        return  (distance)
    else:
        print("There is no path between the nodes")


# In[ ]:


##too slow
def Group_number(list_nodes):
    G_n={}
    
    for node in  nx.nodes(G):
        gr=[]
        for i in list_nodes:
            if node!=i:
                gr.append( Dijkstra(G, node,i))
                    
        G_n[node]=min(gr)
            
    return(G_n)


# In[ ]:


#Load the data
db = expanduser("reduced_dblp.json")
database = json.loads(open(db, 'r').read())


# In[ ]:


# DAATABASE = List of PUBBLICATION
# PUBBLICATION -> 6 DICT= authors, id_conference, id_conference_int, id_publication, id_publication_int, title
# AUTHORS -> List of DICT (About 10500 in reduced json) -> {(author:Name , author_id:ID)}


# In[ ]:


G = nx.Graph() 
dictAutor = pubblicationDictionary(database)
for j in dictAutor.keys():
    G.add_node(j[1], id = j[1], author=j[0])


# In[ ]:


dict_publ = {}
for elem in range(len(database)):
    d = database[elem]['authors']
    for author in range(len(d)):
        if "&" in d[author]['author']:
            pass
        else:
            try:
                dict_publ[database[elem]['id_publication']].append((d[author]['author'], d[author]['author_id']))
            except:
                dict_publ[database[elem]['id_publication']] = [(d[author]['author'], d[author]['author_id'])]

dew = defaultdict(list)
for keys in dictAutor.keys():
    for i in range(len(dictAutor[keys])):
        try:
            dew[keys].append(dictAutor[keys][i][0])
        except:
            dew[keys]=dictAutor[keys][i][0]


# In[ ]:


# ADD EDGES           
for k,v in dict_publ.items():
    for i in itertools.combinations(v,2):
        G.add_edge(i[0][1],i[1][1], pubblication=k[0], pubblication_int = k[1], weight=Jaccard(dew[i[0]],dew[i[1]]))


# In[ ]:


#2(a)
h = graphConference(database, 3345)
betweness = nx.betweenness_centrality(h)
closeness = nx.closeness_centrality(h)
degree = nx.degree(h)


# In[ ]:


#2(b)
G_sub=author_dist("nicola barbieri",2)


# In[ ]:


#3(a)
distance_to_aris(18262)


# In[ ]:


#3(b)
Group_number([18262,256176,141492,256125])

