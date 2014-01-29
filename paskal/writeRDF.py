import rdflib
from rdflib.graph import ConjunctiveGraph as Graph
from rdflib import plugin
from rdflib.store import Store

configString = "/tmp/rdfstore"

store = plugin.get('KyotoCabinet', Store)('rdfstore')

graph = Graph(store="KyotoCabinet")
path = configString
rt = graph.open(path, create=True)

print "Triples in graph before add: ", len(graph)
graph.parse("http://130.88.198.11/co-ode-files/ontologies/pizza.owl", format="xml")
for subj, pred, obj in graph:
    if (subj, pred, obj) not in graph:
        raise Exception("It better be!")
    graph.add((subj, pred, obj))
graph.commit()

print "Triples in graph after add: ", len(graph)
graph.close()