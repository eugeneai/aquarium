import rdflib
#from rdflib.graph import ConjunctiveGraph as Graph
from rdflib import Graph

configString = "/tmp/rdfstore12"

graph = Graph(store="KyotoCabinet")
path = configString
rt = graph.open(path, create=True)

print "Triples in graph before add: ", len(graph)
graph.parse("http://130.88.198.11/co-ode-files/ontologies/pizza.owl", format="xml")
graph.parse("20140114.rdf", format="xml")
graph.commit()

print "Triples in graph after add: ", len(graph)
graph.close()
