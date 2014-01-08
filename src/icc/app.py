#!/usr/bin/env python
# encoding: utf-8

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from pyramid.renderers import render_to_response

MAIN_PT='icc.www.aquarium:/www/static/main.pt'

def view_subject(request):
    subj=request.matchdict['subject']
    model=None
    # return Response('Subject is %s' % subj)
    #d={"a":1, "b":2}
    #print d.__getitem__(u'a')
    return render_to_response(MAIN_PT,
                              {'context':subj, 'model':model, 'view':None,
                               'subject':subj,
                               'title':u'Супер-пупер программа',},
                              request=request)

def view_home_page(request):
    # subj=request.matchdict['subject']
    # model=None
    # return Response('Subject is %s' % subj)
    #d={"a":1, "b":2}
    #print d.__getitem__(u'a')
    return render_to_response(MAIN_PT,
                              {'title':u'Aquarium',},
                              request=request)

def view_triple(request):
    subj=request.matchdict['subject']
    rel=request.matchdict['relation']
    ob=request.matchdict['object']
    return Response('Triple(%s,%s,%s)' % (subj, rel, ob))


def main(global_config=None, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    #config.add_static_view('static', ')
    #config.add_route('home', '/')
    #config.scan()

    config.include('pyramid_chameleon')
    config.add_route('home_page', '/')
    config.add_view(view_home_page, route_name='home_page')

    config.add_route('subject', '/q/{subject}')
    config.add_view(view_subject, route_name='subject')

    config.add_route('triple', '/q/{subject}/{relation}/{object}')
    config.add_view(view_triple, route_name='triple')

    config.add_static_view(name='static',
                           path='icc.www.aquarium:/www/static',
                           cache_max_age=3600)
    return config.make_wsgi_app()

if __name__=="__main__":
    print "Starting server at 0.0.0.0:8080."
    server = make_server('0.0.0.0', 8080, main())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print "KeyboardInterrupt, closed."


"""
On 27 November 2012 07:58, Chris Withers <ch...@simplistix.co.uk> wrote:
> How can I get back the old ZPT style of path expression?
>
> eg:
>
> <html metal:use-macro="view/macros/page">
>
> ...would unpack and do the view.macros['page'] for me?

I have adapted this code from the path implementation in `z3c.pt`:

    https://gist.github.com/4153332

You would have to add the expression type to the existing dict:

from chameleon.zpt.template import PageTemplate
from chameleon.zpt.loader import TemplateLoader

expression_types = PageTemplate.expression_types.copy()
expression_types['path'] = PathExpr()

loader = TemplateLoader(
   "path/to/templates",
   expression_types=expression_types,
   default_expression="path"
)

Please don't hesitate to ask if you need more than this.

\malthe
"""
