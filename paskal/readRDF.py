import rdflib
from rdflib.graph import ConjunctiveGraph as Graph
#from rdflib.graph import Graph

configString = "/tmp/rdfstore12"

graph = Graph(store="KyotoCabinet")
path = configString
rt = graph.open(path, create=False)

print "Triples in graph: ", len(graph)
print "first 20 are as follows:"
i=20
for subj, pred, obj in graph:
    print(subj, pred, obj)
    i-=1
    if i==0:
	break


graph.close()