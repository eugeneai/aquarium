import rdflib

def test():
    UNIVERSE=rdflib.Graph()
    CACHE_NAME='card.n3'

    def universe_setup(g):

        try:
            cf=open(CACHE_NAME)
            g.parse(cf, format='n3')
        except IOError:
            g.parse("http://www.w3.org/People/Berners-Lee/card")
            s = g.serialize(format='n3')
            cf=open(CACHE_NAME, 'w')
            cf.write(s)
            cf.close()

        print("graph has %s statements." % len(g))

    universe_setup(UNIVERSE)



if __name__=="__main__":
    test()
