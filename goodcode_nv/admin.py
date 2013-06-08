from reversion.admin import VersionAdmin
from models import Post, Fortune
from django.contrib import admin

#TODO  REMOVE THESE!!!
#class PostOptions(admin.ModelAdmin):
#   pass
#
#class FortuneOptions(admin.ModelAdmin):
#   pass
#

class VersionedPostAdmin(VersionAdmin, PostOptions):
   """ configure admin Post features here """
   ordering = ('-created','title','sku')
   list_display = ('title', 'sku', 'active', 'created', 'modified')
   list_filter = ('active',)
   search_fields = ['sku', 'name']
   fieldsets = (
        (None, {
            'fields' : ('title', 'sku', 'meta', 'content', 'active'),
	    'classes': ('wide', 'extrapretty'),
        }),
   #     ('Advanced options', {
   #         'classes': ('collapse',),
   #         'fields': ('enable_comments', 'registration_required', 'template_name')
   #     }),
   )
   class Media:
      """ custom js and css for admin form """
      css = {
        "post": ("goodcode_admin/css/blog_post_admin.css",)
      }
      js = ("goodcode_admin/js/blog_post_admin.js",)


class VersionedFortuneAdmin(VersionAdmin, FortuneOptions):
   """ configure admin fortunes features here """
   ordering = ('name','slug')
   list_display = ('name', 'slug', 'active', 'created',)
   list_filter = ('active',)
   search_fields = ['slug', 'name']

admin.site.register(Post, VersionedPostAdmin)
admin.site.register(Fortune, VersionedFortuneAdmin)
