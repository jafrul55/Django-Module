from django.db import models
from django.utils import timezone
from.utils import create_shortened_url

class Shortener(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(null=True,blank=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15,unique=True,blank=True)
    
    class Meta:
        ordering = ["-created"]
    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
    
    def save(self,*args,**kwargs):
        #Check if the short url wasn't specified
        if not self.short_url:
            #Generate a new short url
            self.short_url = create_shortened_url(self)
            
        #Check if the last accessed time is older than 365 days
        if self.last_accessed and (timezone.now() - self.last_accessed).days >= 365:
            #Expire the URL by clearing the short_url field
            self.short_url = ''
        
        #Update the last accessed time to the current time
        self.last_accessed = timezone.now()
        
        super().save(*args,**kwargs)
        
            
