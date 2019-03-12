from django.db import models

# Create your models here.


class Albums(models.Model):
    name = models.CharField(max_length=60,default='')
    source = models.CharField(max_length=50,null=True)  
    description = models.CharField(max_length=100,null=True)
    group_id = models.CharField(max_length=10,default='')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Pics(models.Model):
    name = models.CharField(max_length=100,default='',null=True)
    url  = models.CharField(max_length=100,null=True)
    album = models.ForeignKey(Albums,default='')
    pixs = models.CharField(max_length=30,null=True)
    sortkey = models.CharField(max_length=20,null=True)
    text    = models.TextField(default='',null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class ONE(models.Model):
    url     = models.CharField(max_length=100,default='')
    img     = models.CharField(max_length=100,default='')
    local_img = models.CharField(max_length=100,default='')   
    text    = models.TextField(default='')
    dom     = models.IntegerField(default='')
    may     = models.CharField(max_length=20,default='')
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url 

class Category(models.Model):
    cid = models.IntegerField(unique=True)
    cname = models.CharField(max_length=32)
    cgroup = models.CharField(max_length=32,default='')
    def __str__(self):
        return self.cname

class Article(models.Model):
    
    title       = models.CharField(max_length=100,null=True)
    category    = models.ForeignKey(Category)
    image       = models.ImageField(upload_to='photos',default='') 
    text        = models.CharField(max_length=100,null=True)
    content     = models.TextField(default='',null=True)
    span        = models.CharField(max_length=64,null=True)
    source      = models.CharField(max_length=20,null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    url         = models.CharField(max_length=100)
    author      = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.title