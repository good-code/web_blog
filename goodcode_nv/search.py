from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from django.views.decorators.cache import never_cache
from models import Post
import logging
import re
log = logging.getLogger('goodcode_nv.search')

def search(query):
    query=re.escape(query)
    try:
        results = Post.objects.filter(active=True).extra(select={'snippet': "headline(description, to_tsquery(%s))",
                                                                 'rank': "RANK(search_tsv, to_tsquery(%s))"},
        where=["search_tsv @@ to_tsquery(%s)"],
        select_params=[query, query], params=[query,],order_by=['-rank',])
    except:
        pass
    return results


def search_view(request, page=0, count=0, template="shop/paginated_search.html"):
    """Perform a search based on keywords and categories in the form submission"""
    if request.method=="GET":
        data = request.GET
    else:
        data = request.POST

    is_paged = False
    if request.method == "GET":
        currpage = request.GET.get('page', 1)
    else:
        currpage = 1
    if page == 0:
        if request.method == 'GET':
            page = request.GET.get('page', 1)
        else:
            page = 1

    try:
        keywords = str(data.get('keywords', ''))
        keywords = filter(None, keywords)
    except:
        keywords = ""

    paginator = None
    log.debug('keywords: %s' % keywords)

    # returns dictionary of products maching given keywords.
    # needs to be chached with memcache just like latest designs are.i
    # I think the method can be made more universal and moved to seperate module.  
    #results = Product.objects.extra(select={'snippet': "headline(description, to_tsquery(%s))", 'rank': "RANK(search_tsv, to_tsquery(%s))"},
    #                                where=["search_tsv @@ to_tsquery(%s)"], select_params=[keywords, keywords,], params=[keywords,])
    results=[]
    #for p in Product.objects.raw("SELECT *, RANK(search_tsv, q) AS rank FROM product_product, to_tsquery(%s) AS q WHERE search_tsv @@ q ORDER BY rank DESC;" % "'"+keywords[0]+"'"):
    #    results.append(p)
    try:
        results = search("'|"+keywords+"'")
    except:
        pass
    try:
        paginator = Paginator(results, 10)
    except:
        pass
    try:
        pagen =paginator.page(currpage)
        log.debug('found something for keyword: %s' % keywords)
    except:
        log.debug('no search resoults for keyword %s:' % keywords)
        pagen = None
    if results > 10:
        is_paged = True
    context = RequestContext(request, 
           {
            'results': results,
            'page' : pagen,
            'paginator' : paginator,
            'is_paginated' : is_paged,
            'keywords' : keywords,
           })
    return render_to_response(template, context)
search_view = never_cache(search_view)
