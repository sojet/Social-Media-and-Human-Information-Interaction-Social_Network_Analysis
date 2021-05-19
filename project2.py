import networkx
import pandas as pd
from csv import reader

# obtain values from the csv file
df = pd.read_csv('Edges.csv')
sociomatrix = df.values
print(df)

# create a social matrix
directed_graph = networkx.DiGraph()
#print(directed_graph)

# add nodes to the social matrix
DIMENSION=88
directed_graph.add_nodes_from (range(1,DIMENSION+1))

# create social relation
with open('Edges.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)

    for row in csv_reader:
        for column in row:
            #print(column)
            x = column.split(',')
            #print(x[0])
            if len(x) == 2 :
               #print(x[0] + '/' + x[1] + '/')
               y = int(x[0])
               if x[1] != '':
                z = int(x[1])
                directed_graph.add_edge(y,z)
                
# answer the requirement
MY_ID = 61
indegree = directed_graph.in_degree(MY_ID)
outdegree = directed_graph.out_degree(MY_ID)
print('The vaolue of in-degree of the node representing me: ' + str(indegree))
print('The value of out-degree of the node representing me: ' + str(outdegree))

closeness = networkx.closeness_centrality(directed_graph,MY_ID)
print('The value of the closeness centrality of the node representing me: ' + str(closeness))

betweenness = networkx.betweenness_centrality(directed_graph,MY_ID)
#print(betweenness)
print('The value of the shortest-path betweenness of the node representing me: ' + str(betweenness[MY_ID]))

