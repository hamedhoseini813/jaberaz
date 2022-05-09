from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# class postManger(models.Manager):
#     def Y (self, year):
#         return self.filter(publish__year = year)

# class publishManager(models.Manager):
#     def get_queryset(self):
#         return super(publishManager).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOOSE = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOOSE, default='draft' )
    objects = models.Manager()
    # objects = postManger()
    # published = publishManager()



    class Meta:
        ordering =('-publish',)


    def __str__(self):
        return self.title


    