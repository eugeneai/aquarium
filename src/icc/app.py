from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import rdflib

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


def view_subject(request):
    subj=request.matchdict['subject']
    return Response('Subject is %s' % subj)

def view_triple(request):
    subj=request.matchdict['subject']
    rel=request.matchdict['relation']
    ob=request.matchdict['object']
    return Response('Triple(%s,%s,%s)' % (subj, rel, ob))

if __name__ == '__main__':
    config = Configurator()

    config.add_route('subject', '/q/{subject}')
    config.add_view(view_subject, route_name='subject')

    config.add_route('triple', '/q/{subject}/{relation}/{object}')
    config.add_view(view_triple, route_name='triple')

    config.add_static_view(name='static', path='icc.www.peixe:/www/static')
    app = config.make_wsgi_app()
    print "Starting server."
    server = make_server('0.0.0.0', 8080, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print "KeyboardInterrupt, closed."
