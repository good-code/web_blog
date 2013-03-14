from django import template
register = template.Library()

def gen_album_thumbs(album, img_count=4):
    "shows thumbnails for album"
    return { 'photographs' : album.photograph_set.filter(active=True).order_by('?')[:img_count] }
register.inclusion_tag('gen_album_thumbs.html')(gen_album_thumbs)
