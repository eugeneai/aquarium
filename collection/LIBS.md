Useful libraries
================

Diffutils
---------

diff-match-patch
https://code.google.com/p/google-diff-match-patch/


X[HT]ML processing
------------------

lxml
http://lxml.de/tutorial.html

RDF processing
--------------

RDFLib
https://rdflib.readthedocs.org/en/latest/ and on Wikipedia http://en.wikipedia.org/wiki/RDFLib

Divergence from rdflib 3.0 https://code.google.com/p/python-dlp/wiki/LayerCakePythonDivergence

Redland RDF Libraries http://librdf.org/ (Implemented in C with Python
bindings). Does it have a server?

SPARQL Query language [lib](http://sparql-wrapper.sourceforge.net/).

Notation 3 format, i.e., [N3](http://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D1%82%D0%B0%D1%86%D0%B8%D1%8F_3).

JavaScript [HTML embedded RDFa processing](https://code.google.com/p/rdfquery/).

JavaScript library of linkeddata project & TimBL https://github.com/linkeddata/rdflib.js

Ontologies and OWL processing
-----------------------------

Wikipedia http://ru.wikipedia.org/wiki/Web_Ontology_Language

fuxi https://code.google.com/p/fuxi/

Lectures in Russian on Ontology basics [Онтологии и тезаурусы: модели, инструменты, приложения](http://www.intuit.ru/department/expert/ontoth/1/).

An introductory paper about Description Logic (DL) http://arxiv.org/pdf/1201.4089v2.pdf

Protege 4.x
[tutorial](http://protegewiki.stanford.edu/wiki/Protege4GettingStarted)
and a 10 min introduction of
[a pizza ontology construction](http://protegewiki.stanford.edu/wiki/Protege4Pizzas10Minutes). Pay
great attention on inferences qualities of pizzas according their
properties definitions and constraints.

jOWL - semantic javascript library http://jowl.ontologyonline.org/

Python OWL and its execution environment
[merge](http://seth-scripting.sourceforge.net/). Very interesting
agile approach. Allows DL in classes.


LIST OF USEFUL ONTOLOGY BASED (SOFTWARE)[http://techwiki.openstructs.org/index.php/Ontology_Tools]

OntoWiki


is a tool providing support for agile, distributed knowledge engineering scenarios.

[OntoWiki](http://ontowiki.net/Projects/OntoWiki) facilitates the
visual presentation of a knowledge base as an information map, with
different views on instance data. It enables intuitive authoring of
semantic content, with an inline editing mode for editing RDF content,
similar to WYSIWIG for text documents. Now it is on [Github](https://github.com/AKSW/OntoWiki/).

An ontology set review http://syntheticbiology.org/Semantic_web_ontology/Examples.html Here we can find most commonly used ontologies, such as Dublin Core.

Virtuoso triple storage with fulltext search DEMO http://demo.openlinksw.com/tutorial/

On-line HTML editors
--------------------

WISYWIG editor for HTML http://elrte.org/ It uses jquery and jquery-ui.

Xinha http://trac.xinha.org/

RDFaCE an ontology markup extension of TinyMCE  http://wiki.aksw.org/Projects/RDFaCE.

Pyramid framework
-----------------

Wikipedia http://ru.wikipedia.org/wiki/Pyramid_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D1%8B%D0%B9_%D0%BA%D0%B0%D1%80%D0%BA%D0%B0%D1%81)

Web site http://www.pylonsproject.org/

Single file application tutorial http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/single_file_tasks/single_file_tasks.html

Installation http://docs.pylonsproject.org/en/latest/docs/pyramid_install.html

Russian national standards
--------------------------

В 2010 г., Национальный стандарт ГОСТ Р 3898-2010
«Системы электронного документооборота. Взаимодействие систем управления доку-
ментами. Требования к электронному сообщению»

Другие стандарты: ГОСТ Р 51141-98 «Делопроизводство и архивное дело. Термины и определения», закона РФ N
24-ФЗ от 20.02.1995 «Об информации, информатизации и защите информации», зако-
на РФ от 10.01.2002 N 1-ФЗ «Об электронно-цифровой подписи» и ГОСТа Р ИСО
9000-2001: «Системы менеджмента качества. Основные положения и словарь».

Automatic text processing, stemming, lemmatization
--------------------------------------------------

АОТ (Автоматическая Обработка Текста) [сайт](http://aot.ru/) разработки программного обеспечения для обработки текстов на русском языке.

Introduction into snowball algorithm is [here](http://snowball.tartarus.org/texts/introduction.html)

Libstemmer, which is based the snowball algorithm is [here](http://snowball.tartarus.org/download.php).

Lemmatization for European languages, including Russian http://lemmatizer.org/

RESTful Architecture
--------------------

IBM's [Introduction](http://www.ibm.com/developerworks/webservices/library/ws-restful/).

Key-Value storages
------------------

Kyoto Cabinet (supports REST) is [here](http://fallabs.com/kyotocabinet/). I thik best fit the idea.

Goole's [LevelDB](https://code.google.com/p/leveldb/), but it does not support any server features.

Question - ? How to utilize the storage with distributed revision control system?

Compressing
-----------
Google's Snappy [library](https://pypi.python.org/pypi/python-snappy). See a link to Google web site on the page.


Ontologies
----------

GOLD GOLD Community: General Ontology for Linguistic Description
http://www.linguistics-ontology.org/gold/ - It seems it is enough for us.

ISOCat set of ontologies to represent lexical and other phenomena
http://www.isocat.org/files/TDGs.html.

Lemon is a proposed model for modeling lexicon and machine-readable
dictionaries and linked to the Semantic Web and the Linked Data
cloud. http://www.lemon-model.net/

Multilingual Ontologies for Networked Knowledge http://www.monnet-project.eu/Monnet/Monnet/English?init=true.

AtomOwl is an ontology whose aim is to capture the semantics of
rfc4287. RFC4287 is a format to syndicate online content, such as
weblogs, podcasts, videocasts, etc. Syndication is a helpful way to
alert interested readers to changes to a web site, be it to new
content or changed content. (Can be used to describe pushed content)
http://bblfish.net/work/atom-owl/2006-06-06/AtomOwl.html

The SIOC initiative (Semantically-Interlinked Online Communities) aims
to enable the integration of online community information. SIOC
provides a Semantic Web ontology for representing rich data from the
Social Web in RDF (Can be used to describe syndication of WEB-sites).
http://www.sioc-project.org/

DOLCE: a Descriptive Ontology for Linguistic and Cognitive Engineering (an Upper ontology)
http://www.loa.istc.cnr.it/DOLCE.html

ROCore (Mereological ontology related to biology, but intended to be
independent of it)
https://code.google.com/p/obo-relations/wiki/ROCore

Standard Upper Ontology Working Group (SUO WG)
http://suo.ieee.org/

Simple part-whole relations in OWL Ontologies
http://www.w3.org/2001/sw/BestPractices/OEP/SimplePartWhole/

Ontologies that definitely to be used in the project
----------------------------------------------------

RDF Vocabulary Description Language 1.0: RDF Schema (METADATA, e.g., notions of properties)
http://www.w3.org/TR/2004/REC-rdf-schema-20040210/

The Friend of a Friend (FOAF) project (Useful in presentation of a Person)
http://www.foaf-project.org/ Vcard (is it necessary?) http://www.w3.org/TR/vcard-rdf/

Describing Copyright in RDF
http://creativecommons.org/ns

SKOS Core provides a model for expressing the basic structure and
content of concept schemes such as thesauri, classification schemes,
subject heading lists, taxonomies, 'folksonomies', other types of
controlled vocabulary, and also concept schemes embedded in glossaries
and terminologies. (It is useful in Concept definition and its labeling)
http://www.w3.org/TR/2005/WD-swbp-skos-core-guide-20051102/

DCMI Home: Dublin Core&reg; Metadata Initiative (DCMI) (Used to
describe metadata about a document, e.g., creator, validity time period)
http://dublincore.org/
Also OpenSource Metadata Framework (OMF) Specification (based on DC)
http://www.ibiblio.org/osrt/omf/omf_elements

RDF Site Summary 1.0 Modules: Content (Used to introduce html pages
as objects)
http://web.resource.org/rss/1.0/modules/content/

The Organization Ontology (to describe organizations)
http://www.w3.org/TR/2014/REC-vocab-org-20140116/
