from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello %(name)s! \%(text)s\.' % request.matchdict)

def view_main(request):
    return Response('fred')

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}/{text}')
    config.add_route('index', '/')
    config.add_view(hello_world, route_name='hello')
    config.add_view(view_main, route_name='index')
    config.add_static_view(name='static', path='icc.www.peixe:/www/static')
    app = config.make_wsgi_app()
    print "Starting server."
    server = make_server('0.0.0.0', 8080, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print "KeyboardInterrupt, closed."
