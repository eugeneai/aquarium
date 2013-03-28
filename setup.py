import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    #'pyramid_zcml',
    'WebError',
    #'Acquisition',
    #'zope.PageTemplate',
    #'gitpython',
    'zope.component',
    'lxml',
    'diff-match-patch',
    ]


setup(name='peixe',
      version='0.0',
      description='''Ontology based interactive inductive document data propagation engine.''',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Evgeny Cherkashin',
      author_email='eugeneai@irnok.net',
      url='',
      keywords='web wsgi pyramid text document',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="peixe",
#      entry_points = """\
#      [paste.app_factory]
#      app = semdoctree.run:app
#      """
      )
