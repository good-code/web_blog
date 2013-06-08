from django.db import models
from goodcode_nv import settings
from django.template.defaultfilters import slugify

class Post(models.Model):
   """ Blog Post """
   title    = models.CharField(max_length=255)
   sku    = models.CharField(max_length=255, blank=True)
   meta = models.CharField(max_length=255, blank=True)
   content = models.TextField()
   active = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now=True)

   class Meta:
      verbose_name = 'Blog post'
      verbose_name_plural = 'Blog posts'

   def __unicode__(self):
      return u"%s - %s" % (self.title, self.sku)

   def get_absolute_url(self):
      return u"%s/post/%s/" % (settings.SITE_URL , self.sku)

   def url(self):
      return u"/post/%s" % self.sku
    
   def save(self, force_insert=False, force_update=False, **kwargs):
      '''Overwrite save method to send message_from_visitor signal,
         only when confirm was ticked on'''
      if not self.pk:
          pass
      if not self.sku:
          self.sku = slugify(self.title)
      super(Post, self).save(force_insert=force_insert, force_update=force_update)

class Fortune(models.Model):
   """ quotes in header """
   name  = models.CharField(max_length=255)
   slug    = models.CharField(max_length=255)
   content = models.TextField()
   active = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)

   class Meta:
      verbose_name = 'fortune'
      verbose_name_plural = 'fortunes'

   def __unicode__(self):
      return u"%s - %s" % (self.name, self.slug)

   def get_absolute_url(self):
      return u"%s/fortune/%s/" % (settings.SITE_URL , self.slug)

   def url(self):
      return u"/post/%s" % self.slug
    
   def save(self, force_insert=False, force_update=False, **kwargs):
      '''Overwrite save method to send message_from_visitor signal,
         only when confirm was ticked on'''
      if not self.pk:
          pass
      super(Fortune, self).save(force_insert=force_insert, force_update=force_update)



