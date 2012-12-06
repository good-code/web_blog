from django.conf.urls import patterns, include, url
from goodcode_nv.feeds import LatestPosts
from goodcode_nv.views import Render_Post, Render_Frontpage
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'', include('feincms.urls')),
     url(r'^$', Render_Frontpage.as_view()),
     url(r'^post/(?P<sku>.*)$', Render_Post.as_view()), 
     url(r'^about/', TemplateView.as_view(template_name='about.html')),
     url(r'^contact/', TemplateView.as_view(template_name='contact.html')),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^comments/', include('django.contrib.comments.urls')),
     url(r'^latest.rss', LatestPosts()),

)
#static folder to serve fonts from the same domain
urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/goodcode/image-server/'}),
            )

