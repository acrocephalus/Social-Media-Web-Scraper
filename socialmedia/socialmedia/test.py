import difflib
keywords = ['social media','social business','social networking','social marketing','online marketing','social selling',
    'social customer experience management','social cxm','social cem','social crm','google analytics','seo','sem',
    'digital marketing','social media manager','community manager']

metakeywords = ['top 10', 'social media blog', 'social media blog nomination']

if any(key in metakey for key in keywords for metakey in metakeywords):
    print 'ok'
