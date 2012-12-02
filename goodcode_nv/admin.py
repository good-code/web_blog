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

class VersionedFortuneAdmin(VersionAdmin, FortuneOptions):
   ordering = ('name','slug')
   list_display = ('name', 'slug', 'active', 'created',)
   list_filter = ('active',)
   search_fields = ['slug', 'name']

admin.site.register(Post, VersionedPostAdmin)
admin.site.register(Fortune, VersionedFortuneAdmin)
