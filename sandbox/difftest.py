from lxml import etree
import os.path


DATA_DIR="./data"
F1='index1.html'
F2='index2.html'

def xhtml_file(name):
    return open(os.path.join(DATA_DIR, name))


parser = etree.HTMLParser()
T1=etree.parse(xhtml_file(F1), parser)
#T2=etree.parse(xhtml_file(F2))

print etree.tostring(T1.getroot(), pretty_print=True, method="html")
