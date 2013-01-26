from django.conf.urls import patterns, include, url
from views import List_Albums, Render_Album, Render_Photograph

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

     url(r'^photographs/', List_Albums.as_view()), 
     url(r'^photographs/album/(?P<sku>.*)', Render_Album.as_view()), 
     url(r'^photographs/photographs/(?P<sku>.*)', Render_Photograph.as_view()), 


)
