from django.contrib.syndication.views import Feed
from goodcode_nv.models import Post

class LatestPosts(Feed):
    title = "What's new at Goodcode.co.uk"
    link = "/latest.rss"
    description = "Updates on changes and additions to Goodcode.co.uk"

    def items(self):
        how_many    = 10
        all_of_them = Post.objects.all()
        if how_many > all_of_them:
            how_many = all_of_them
        return Post.objects.order_by('-created')[:how_many]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
    def item_link(self, item):
	return 'http://goodcode.co.uk/post/%s'% item.sku
