from django.shortcuts import render_to_response
from django.template import RequestContext
from goodcode_nv.models import Post, Fortune
from django.views.generic import TemplateView


def frontpage(request):
    '''
    renders front page shows list of post,  categories,  
    '''
    ctx= {'posts': Post.objects.filter(active=True).order_by('-created'), 'fortune': Fortune.objects.all().order_by('?')[:1]}
    return render_to_response('front_page.html', ctx,
           context_instance=RequestContext(request))

class Render_Frontpage(TemplateView):
    template_name = 'front_page.html'

    def dispatch(self, *args, **kwargs):
        return super(Render_Frontpage, self).dispatch(*args, **kwargs)

    def get_context_data(self,  **kwargs):
	ctx= {'posts': Post.objects.filter(active=True).order_by('-created'),
              'fortune': Fortune.objects.all().order_by('?')[:1]}
	return ctx

class Render_Post(TemplateView):
    template_name = 'post.html'

    def dispatch(self, *args, **kwargs):
        return super(Render_Post, self).dispatch(*args, **kwargs)

    def get_context_data(self, sku,  **kwargs):
	ctx= {'post': Post.objects.get(sku=sku)}
	return ctx
