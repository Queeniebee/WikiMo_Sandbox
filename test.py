""" Using MWClient with WikiMo different that Wikipedia. Pages within the Special Namespace not registering. Will need to go on IRC channel to understand
how to interact with WikiMo Api """

import mwclient
from pprint import pprint

wikiMo = mwclient.Site(('https', 'wiki.mozilla.org'), path='/' )
# page = wikiMo.Pages['Contribute']
page = wikiMo.Pages['Special:UnusedTemplates']
links = page.links(namespace=-1|10, generator=False)
prop = page.extlinks()
# links = page.iwlinks()

rev = page.revisions(prop='timestamp')
pprint(rev)
 
for item in links:
    print item

# pprint(wikiMo.namespaces)
