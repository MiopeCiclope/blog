from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField

def get_image_filename(instance, filename):
    title = instance.title
    slug = slugify(title)
    return "media/%s-%s" % (slug, filename)
    
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = MarkdownField(default=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    summary = models.TextField()
    image = models.ImageField(upload_to=get_image_filename,verbose_name='Image', null=True)
    caption = models.CharField(max_length=200, default="You should add a caption")
    love = models.IntegerField(default=0)
    garbage = models.IntegerField(default=0)
    drunk = models.BooleanField(default=False)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title