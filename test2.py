import mwclient
from pprint import pprint


wikiMo = mwclient.Site(('https', 'wiki.mozilla.org'), path='/' )
pages = wikiMo.Pages['Category:Special']

for page in pages:
    pprint(pages.name)
