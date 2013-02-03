from django import template
register = template.Library()

def gen_album_thumbs(album):
    "shows thumbnails for album"
    return { 'photographs' : album.photograph_set.all().order_by('?')[:5] }
register.inclusion_tag('gen_album_thumbs.html')(gen_album_thumbs)
