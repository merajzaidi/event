from django.db import models ,transaction
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
    attendences = models.CharField(max_length=50, default="")
    date = models.DateField(max_length=70, default="")
    time = models.TimeField(max_length=70, default="")
    poster = models.ImageField(upload_to='main/slider',default='')
    desc = models.CharField(max_length=300)
    verification = models.BooleanField(default=False)
    author = models.ForeignKey(User,default=None, on_delete=models.SET_NULL,null=True)
    phone_no = models.CharField(default='',max_length=10)
    organiser = models.CharField(max_length=50,default="")
    taam = models.BooleanField(default=False)
    cat_choice = (
        ('mehfil', "Mehfil"),
        ('majlis', "Majlis"),
        ('others',"Others"),
    )
    category = models.CharField(max_length=50, default='others',choices=cat_choice)

    def __str__(self):
        return self.title

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.post_id} ({self.title})'

class Shaiyar(models.Model):
    Shaiyarname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='main/slider', default='')
    post = models.ForeignKey(postrequest, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

class mehfildetail(models.Model):
    nizamat = models.CharField(max_length=50)
    nizamimage = models.ImageField(upload_to='main/slider',default = '')
    sadarat = models.CharField(max_length=50)
    sadaratimag = models.ImageField(upload_to='main/slider',default = '')
    mehfil  = models.OneToOneField(postrequest, on_delete=models.CASCADE)

    def __str__(self):
        return self.mehfil.title

class contact(models.Model):
    contacter = models.CharField(max_length=30)

class Mehfil(models.Model):
    pass