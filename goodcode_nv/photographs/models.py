from django.db import models
class Album(models.Model):
   name  = models.CharField(max_length=255)
   slug    = models.CharField(max_length=255)
   description = models.TextField()
   active = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)


   class Meta:
      verbose_name = 'Album'
      verbose_name_plural = 'Albums'

   def __unicode__(self):
      return u"%s - %s" % (self.name, self.slug)

   def get_absolute_url(self):
      return u"%s/photographs/alubums/%s/" % (settings.SITE_URL , self.slug)

   def url(self):
      return u"/photographs/albums/%s" % self.slug
    
   def save(self, force_insert=False, force_update=False, **kwargs):
      '''Overwrite save method to send message_from_visitor signal,
         only when confirm was ticked on'''
      if not self.pk:
          pass
      super(Album, self).save(force_insert=force_insert, force_update=force_update)

from sorl.thumbnail import ImageField
class Photograph(models.Model):
   name  = models.CharField(max_length=255)
   slug    = models.CharField(max_length=255)
   description = models.TextField()
   active = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)
   album = models.ForeignKey(Album)
   image = ImageField(upload_to='photographs_uplad')


   class Meta:
      verbose_name = 'Photograph'
      verbose_name_plural = 'Photographs'

   def __unicode__(self):
      return u"%s - %s" % (self.name, self.slug)

   def get_absolute_url(self):
      return u"%s/photographs/photograph/%s/" % (settings.SITE_URL , self.slug)

   def url(self):
      return u"/photographs/photograph/%s" % self.slug
    
   def save(self, force_insert=False, force_update=False, **kwargs):
      '''Overwrite save method to send message_from_visitor signal,
         only when confirm was ticked on'''
      if not self.pk:
          pass
      super(Photograph, self).save(force_insert=force_insert, force_update=force_update)

# Create your models here.
