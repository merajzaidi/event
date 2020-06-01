from django.db import models ,transaction
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
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
    #author = models.ForeignKey(User,default=None, on_delete=models.SET_NULL,null=True)
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

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,full_name=None):
        if not email:
            raise ValueError("User must have a Email")
        if not password:
            raise ValueError("Password is Madatory")
        user = self.model(
            email=self.normalize_email(email),
            full_name=self.normalize_full_name(full_name),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,email,password,full_name):
        user = self.create_user(email,password=password,full_name=full_name)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, full_name):
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
        )
        user.staff = True
        user.superuser = True
        user.volunteer = True
        user.save(using=self._db)
        return user
    def create_volunteer(self,email,password,full_name):
        user= self.create_user(
            email,
            password=password,
            full_name=full_name,
        )
        user.staff = True
        user.superuser = False
        user.volunteer = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    full_name = models.CharField(verbose_name='Full Name',max_length=50)
    email = models.EmailField(unique=True,verbose_name='Email Address', max_length=255)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    volunteer = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def get_full_name(self):
        return self.full_name
    def get_short_name(self):
        return self.email
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser
    @property
    def is_active(self):
        return self.active
    @property
    def is_volunteer(self):
        return self.volunteer