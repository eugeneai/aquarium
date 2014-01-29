import rdflib
from rdflib.graph import ConjunctiveGraph as Graph
from rdflib import plugin
from rdflib.store import Store

configString = "/tmp/rdfstore"

store = plugin.get('KyotoCabinet', Store)('rdfstore')

graph = Graph(store="KyotoCabinet")
path = configString
rt = graph.open(path, create=False)

print "Triples in graph: ", len(graph)
print graph.serialize()

graph.close()