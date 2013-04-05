from models import Album, Photograph
import datetime
import os

def import_album(album, album_dir):
   album_files = os.listdir('/home/fireant/goodcode_nv/static/photographs/%s' % album_dir)
   for photo in album_files:
      print photo
      Photograph(name=photo, slug=photo, description='', active=True, album=album,
                 image='/photographs/%s/%s'% (album_dir, photo)).save()

