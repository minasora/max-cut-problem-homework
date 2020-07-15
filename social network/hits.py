import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('g2.xlsx')
edge_data = pd.read_excel('edge.xlsx')
DG = nx.DiGraph()
nstart = []
for i, node_data in data.iterrows():
    DG.add_node(node_data['id'])
    nstart.append(node_data['stars'])
for i, edge in edge_data.iterrows():
    DG.add_edge(edge['Source'], edge['Target'])

end_data = nx.hits(DG, nstart = nstart,max_iter=50)
print(end_data)
j = 0
for i in end_data:
    if j == 0:
        ser = pd.Series(i)
    else:
        ser_1 = pd.Series(i)
    j = j+1
df = pd.concat([ser, ser_1], axis=1)
df.to_csv('excel_output1.csv')