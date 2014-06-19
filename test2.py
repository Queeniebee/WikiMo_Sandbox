import mwclient
from pprint import pprint


wikiMo = mwclient.Site(('https', 'wiki.mozilla.org'), path='/' )
# pages = wikiMo.Pages['Special:SpecialPages']

"""
for page in pages:
    pprint(pages.name)
"""
# pprint(wikiMo.namespaces)


special = wikiMo.api('query', meta='siteinfo', siprop='specialpagealiases')
pprint(special)

"""
nsindexes = dict((v,k) for k,v in wikiMo.namespaces.iteritems())
for page in wikiMo.allpages(namespace=nsindexes['Template']):
    print page.name
"""
