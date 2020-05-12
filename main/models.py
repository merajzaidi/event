from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class slider(models.Model):
    slider_image = models.ImageField(upload_to='main/slider')

class city(models.Model):
    #id = models.UUIDField(primary_key=True,default = uuid.uuid4())
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

class postrequest(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=70, default="")
    place = models.ForeignKey('city', on_delete=models.SET_NULL,null=True)
    #city = models.CharField(max_length=30)
    date = models.DateField(max_length=70, default="")
    time = models.TimeField(max_length=70, default="")
    poster = models.ImageField(upload_to='main/slider')
    desc = models.CharField(max_length=300)
    verification = models.BooleanField()
    author = models.ForeignKey(User,default=None, on_delete=models.SET_NULL,null=True)
    cat_choice = (
        ('mehfil', "Mehfil"),
        ('majlis', "Majlis"),
        ('others',"Others"),
    )
    category = models.CharField(max_length=50, default='others',choices=cat_choice)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.verification:
            try:
                temp = postrequest.objects.get(verification=True)
                if self != temp:
                    temp.verification = False
                    temp.save()
            except postrequest.DoesNotExist:
                pass
        super(postrequest, self).save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.post_id} ({self.title})'

