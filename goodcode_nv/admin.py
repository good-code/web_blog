from reversion.admin import VersionAdmin
from models import Post, Fortune
from django.contrib import admin

class PostOptions(admin.ModelAdmin):
   pass

class FortuneOptions(admin.ModelAdmin):
   pass


class VersionedPostAdmin(VersionAdmin, PostOptions):
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
      css = {
        "post": ("admin/goodcode/css/blog_post_admin.css",)
      }
      js = ("admin/goodcode/js/blog_post_admin.js",)


class VersionedFortuneAdmin(VersionAdmin, FortuneOptions):
   ordering = ('name','slug')
   list_display = ('name', 'slug', 'active', 'created',)
   list_filter = ('active',)
   search_fields = ['slug', 'name']

admin.site.register(Post, VersionedPostAdmin)
admin.site.register(Fortune, VersionedFortuneAdmin)
