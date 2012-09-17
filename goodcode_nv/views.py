from django.shortcuts import render_to_response
from django.template import RequestContext
from goodcode_nv.models import Post

def frontpage(request):
    '''
    renders front page shows list of post,  categories,  
    '''
    ctx= {'posts': Post.objects.filter(active=True).order_by('-created')}
    return render_to_response('front_page.html', ctx,
           context_instance=RequestContext(request))

def render_post(request, sku):
    '''
    renders post page
    '''
    ctx= {'post': Post.objects.get(sku=sku)}
    return render_to_response('post.html', ctx,
           context_instance=RequestContext(request))


