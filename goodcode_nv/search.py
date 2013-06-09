from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from django.views.decorators.cache import never_cache
from django.db import connection
from models import Post
import logging
import re
log = logging.getLogger('goodcode_nv.search')

def search(query):
    """ wrapper around postgres full text search """

    #escape user input, query is passed as %s and it will be escaped by database api
    # so it is not nessesary to escape it here!
    #query=re.escape(query)
    #TODO:  for keyword in keywords create query in form key & key | key ! key
    log.info('quering db for: %s' % query)
    try:
        results = Post.objects.filter(active=True).extra(select={'snippet': "ts_headline(content, to_tsquery(%s))",
                                                                 'rank': "ts_rank_cd(search_tsv, %s, 32 /* rank/(rank+1) */ )"},
                                                         where =["search_tsv @@ to_tsquery(%s)"],
        select_params=[query, query], params=[query,], order_by=['-rank',])
    except:
        results = None

    return results

def get_keywords(id):
    """get_keywords: return set of keywords for given post"""
    try:
        cursor = connection.cursor()
        cursor.execute('select search_tsv as vector FROM goodcode_nv_post where id=%s;', [id])
        results = cursor.fetchall()
    except:
        results = None

    return results


def search_view(request, page=0, count=0, template="search.html"):
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
        keywords = str(data.get('q', ''))
        keywords = filter(None, keywords)
        for word in keywords.split():
            query = '|'.join(word)
    except:
        query = ""

    log.info('keywords where set to : %s' % keywords)

    paginator = None
    try:
        results = search(query)
    except:
        results = []

    log.info('results : %s' % results)
    try:
        paginator = Paginator(results, 10)
    except:
        paginator = None
    try:
        pagen =paginator.page(currpage)
        #log.debug('found something for keyword: %s' % keywords)
    except:
        #log.debug('no search resoults for keyword %s:' % keywords)
        pagen = None
    if len(results) > 10:
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
