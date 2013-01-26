from models import Album, Photograph
import datetime
import os

def import_album(album_name, album_dir):
   album_files = os.listdir('/home/goodcode/image-server/photos/%s' % album_dir)
   album = Album(name=album_name, created=datetime.datetime.now(), slug=album_name).save()
   for photo in album_files:
      print photo
      Photograph(album=album, name=photo, path=photo, created=datetime.datetime.now(), description='',active=True, slug=photo).save()

