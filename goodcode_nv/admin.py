from reversion.admin import VersionAdmin
from models import Post
from django.contrib import admin

class PostOptions(admin.ModelAdmin):
   pass

# admin.site.register(Post, PostOptions)

#class VersionedPageAdmin(PageAdmin, VersionAdmin):
#        pass


#admin.site.unregister(Post)
class VersionedPostAdmin(VersionAdmin, PostOptions):
    pass


#admin.site.register(Page, VersionedPageAdmin)
#admin.site.unregister(PostOptions)
admin.site.register(Post, VersionedPostAdmin)
