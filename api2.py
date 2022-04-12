

import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
print("Page - Title: %s" % page_py.title)
print("Page - Summary: %s" % page_py.summary[0:60])
print(page_py.fullurl)
print(page_py.canonicalurl)
