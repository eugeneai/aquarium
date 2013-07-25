import rdflib
import rdflib.store as store

def test(store='default'):
    ident = rdflib.URIRef("rdflib_test")
    g=UNIVERSE=rdflib.Graph(store=store, identifier=ident)
    g.open("/home/aqua/aquarium/DATA/test.kch", create=True)

    if len(g)==0:
        g.parse("http://www.w3.org/People/Berners-Lee/card")
        print "A graph has been obtained and loaded."

    print("graph has %s statements." % len(g))
    g.close()


if __name__=="__main__":
    test('KyotoCabinet')
