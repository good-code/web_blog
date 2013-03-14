from django.shortcuts import render_to_response
from django.template import RequestContext
from goodcode_nv.models import Post, Fortune
from photographs.models import Album
from django.views.generic import TemplateView
from settings import LATEST_ALBUMS_NR

class Render_Frontpage(TemplateView):
    template_name = 'front_page.html'

    def dispatch(self, *args, **kwargs):
        return super(Render_Frontpage, self).dispatch(*args, **kwargs)

    def get_context_data(self,  **kwargs):
	ctx = {'posts': Post.objects.filter(active=True).order_by('-created'),
              'fortune': Fortune.objects.all().order_by('?')[0],
	      'albums': Album.objects.filter(active=True).order_by('-id')[:LATEST_ALBUMS_NR],
	}
	return ctx

class Render_Post(TemplateView):
    template_name = 'post.html'

    def dispatch(self, *args, **kwargs):
        return super(Render_Post, self).dispatch(*args, **kwargs)

    def get_context_data(self, sku,  **kwargs):
	ctx= {'post': Post.objects.get(sku=sku)}
	return ctx
