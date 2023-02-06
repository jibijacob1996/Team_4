#!/usr/bin/env python
# coding: utf-8

# In[36]:


import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


# In[37]:


df = pd.read_table("author_label.dat",sep='\t', header=None)
df1 = pd.read_table("author_map_id.dat",sep='\t',header=None)
df2 = pd.read_table("paper_author.dat", sep="\t",header=None)
df3 = pd.read_table("paper_conference.dat", sep="\t",header=None)
df4 = pd.read_table("paper_type.dat", sep="\t",header=None)


# In[38]:


df.columns=['Unique_id','label']
df1.columns=['Author_id','Unique_id']
df2.columns=['Paper_id','Author_id','wt']
df3.columns=['Paper_id','Conference_id','wt']
df4.columns=['Paper_id','Paper_type','wt']


# In[6]:


df.head


# In[39]:


df['Unique_id'] = df['Unique_id'].apply(lambda x: f"U_{x}")
df['label'] = df['label'].apply(lambda x: f"L_{x}")

df1['Author_id'] = df1['Author_id'].apply(lambda x: f"A_{x}")
df1['Unique_id'] = df1['Unique_id'].apply(lambda x: f"U_{x}")

df2['Paper_id'] = df2['Paper_id'].apply(lambda x: f"P_{x}")
df2['Author_id'] = df2['Author_id'].apply(lambda x: f"A_{x}")

df3['Paper_id'] = df3['Paper_id'].apply(lambda x: f"P_{x}")
df3['Conference_id'] = df3['Conference_id'].apply(lambda x: f"C_{x}")

df4['Paper_id'] = df4['Paper_id'].apply(lambda x: f"P_{x}")
df4['Paper_type'] = df4['Paper_type'].apply(lambda x: f"T_{x}")


# In[40]:


G = nx.from_pandas_edgelist(df.head(15), 'Unique_id', 'label')
G1 = nx.from_pandas_edgelist(df1.head(15), 'Author_id', 'Unique_id')
G2 = nx.from_pandas_edgelist(df2.head(15), 'Paper_id', 'Author_id',edge_attr = None)
G3 = nx.from_pandas_edgelist(df3.head(15), 'Paper_id', 'Conference_id', edge_attr = None)
G4 = nx.from_pandas_edgelist(df4.head(15), 'Paper_id', 'Paper_type', edge_attr = None)


# In[56]:


G.add_edges_from(G1.edges)
G.add_edges_from(G2.edges)
G.add_edges_from(G3.edges)
G.add_edges_from(G4.edges)


# In[58]:


A=list(set(G.nodes))


# In[62]:


auth_id=[]
un_id=[]
pap_id=[]
conf_id=[]
typ=[]
lab=[]


# In[67]:


for node in A:
    if "P_" in node:
        pap_id.append(node)
    elif "C_" in node:
        conf_id.append(node)
    elif "T_" in node:
        typ.append(node)
    elif "L_" in node:
        lab.append(node)
    elif "A_" in node:
        auth_id.append(node)
    else:
        un_id.append(node)


# In[76]:




color_map = []

for node in G:
    if node in pap_id:
        color_map.append('yellow')
    elif node in conf_id:
        color_map.append('red')
    elif node in typ:
        color_map.append('blue')
    elif node in lab:
        color_map.append('pink')
    elif node in auth_id:
        color_map.append('violet')
    elif node in un_id:
        color_map.append('indigo')    

from matplotlib.pyplot import figure
figure(figsize=(20, 15))
nx.draw_kamada_kawai(G, with_labels=True, node_color = color_map, font_color = 'black', node_size=700)
    


# In[35]:


G.nodes()

