from models import Photograph, Album
from django.views.generic import TemplateView

class Render_Album(TemplateView):
    template_name = 'photographs/album.html'

    def dispatch(self, *args, **kwargs):
        return super(Render_Album, self).dispatch(*args, **kwargs)

    def get_context_data(self, slug,  **kwargs):
	ctx= {'post': Album.objects.get(slug=slug)}
	return ctx


class Render_Photograph(TemplateView):
    template_name = 'photographs/photograph.html'

    def dispatch(self, *args, **kwargs):
        return super(Render_Photograph, self).dispatch(*args, **kwargs)

    def get_context_data(self, slug,  **kwargs):
	ctx= {'post': Photograph.objects.get(slug=slug)}
	return ctx

class List_Albums(TemplateView):
    template_name = 'photographs/album_list.html'

    def dispatch(self, *args, **kwargs):
        return super(List_Albums, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
	ctx= {'post': Album.objects.filter(active=True)}
	return ctx
