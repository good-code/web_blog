from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from goodcode_nv.feeds import LatestPosts

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'', include('feincms.urls')),
     url(r'^$', 'goodcode_nv.views.frontpage'),
     url(r'^post/(?P<sku>.*)$', 'goodcode_nv.views.render_post'),
     url(r'^about/', direct_to_template, {'template': 'about.html'}),
     url(r'^contact/', direct_to_template, {'template': 'contact.html'}),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^comments/', include('django.contrib.comments.urls')),
     url(r'^latest.rss', LatestPosts()),

)
#static folder to serve fonts from the same domain
urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/goodcode/image-server/'}),
            )

