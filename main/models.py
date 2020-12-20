from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.URLField("Original Url", max_length=5000)
    url_code = models.CharField("Url Code", max_length=200, null=True, blank=True)
    date_created = models.DateTimeField("Date Created", auto_now_add=True)
    
    # Object properties declaration
    class Meta:
        verbose_name_plural = "Urls"

    # Object str representation
    def __str__(self):
        return self.long_url

