import rdflib
import rdflib.store as store

def test(store='default'):
    ident = rdflib.URIRef("rdflib_test")
    g=rdflib.Graph(store=store, identifier=ident)
    g.open("/home/aqua/aquarium/DATA/test.kch", create=True)

    if len(g)==0:
        g.parse("http://www.w3.org/People/Berners-Lee/card")
        print "A graph has been obtained and loaded."

    print("graph has %s statements." % len(g))
    return g

def count(g, obj=None, rel=None):
    for subject, predicate, obj_ in g:
        if not (subject,predicate,obj_) in g:
            raise Exception("Iterator / Container Protocols are Broken!!")
        # print "---", subject, predicate, obj, type(subject)
        # print "---", type(subject), type(predicate), type(obj)
        if obj==obj_ and rel==predicate:
            print subject, predicate, obj_

def get_by_type(g, type_id):
    Type=rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
    count(g, obj=type_id, rel=Type)

if __name__=="__main__":
    g=test('KyotoCabinet')
    count(g)
    PersonType=rdflib.URIRef('http://xmlns.com/foaf/0.1/Person')
    print type(PersonType)
    get_by_type(g, PersonType)
    g.close()
