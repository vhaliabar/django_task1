from django.db import models
from django.contrib.auth.models import User


class Ownable (models.Model):
    user = models.ForeignKey( 'auth.User' , verbose_name='Author',
    related_name='author', on_delete=models.CASCADE )

    class Meta :
        abstract = True
        
        
class RegisteredUser (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    tracking = models.ManyToManyField( User ,
        related_name= 'tracked_by' ,
        blank= True , symmetrical= False )
    def __str__(self):
        return str(self.tracking)

class FeedItem (Ownable):
    content = models.CharField( "Content" , max_length= 1000 ,
                blank= True , null= True )
    created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, related_name='feed_likes', null=True)
    
    def total_likes(self):
        return self.liked.count()
    def __str__(self):
        return self.content
    class Meta:
        ordering = ["-created"]
