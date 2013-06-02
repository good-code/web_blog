from models import Photograph, Album
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

class Render_Album(TemplateView):
    template_name = 'photographs/album.html'

    def dispatch(self, *args, **kwargs):
        return super(Render_Album, self).dispatch(*args, **kwargs)

    def get_context_data(self, slug,  **kwargs):
        album = get_object_or_404(Album, slug=slug)
	ctx= {'album': album, 'photographs': album.photograph_set.filter(active=True)}
	return ctx


class Render_Photograph(TemplateView):
    template_name = 'photographs/photograph.html'

    def dispatch(self, *args, **kwargs):
        return super(Render_Photograph, self).dispatch(*args, **kwargs)

    def get_context_data(self, slug,  **kwargs):
	ctx= {'photograph': get_object_or_404(Photograph, slug=slug)}
	return ctx

class List_Albums(TemplateView):
    template_name = 'photographs/album_list.html'

    def dispatch(self, *args, **kwargs):
        return super(List_Albums, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
	ctx= {'albums': Album.objects.filter(active=True).order_by('-id')}
	return ctx
