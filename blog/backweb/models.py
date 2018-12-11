from django.db import models


class MyUser(models.Model):
    truename = models.CharField(max_length=10,null=True)
    usertel = models.CharField(max_length=13,null=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'

class Column(models.Model):
    name = models.CharField(max_length=20)
    alias = models.CharField(max_length=20)
    keywords = models.CharField(max_length=30, null=True)
    describe = models.CharField(max_length=150)
    father = models.ForeignKey('self',null=True)
    class Meta:
        db_table = 'column'

class Article(models.Model):
    title = models.CharField(max_length=100)
    describe = models.CharField(max_length=150)
    # category = models.CharField(max_length=10)
    tags = models.CharField(max_length=30,null=True)
    visibility = models.BooleanField(default=True)
    keywords = models.CharField(max_length=30,null=True)
    content = models.TextField()
    titlepic = models.ImageField(upload_to='article',null=True)
    time = models.DateTimeField(auto_now_add=True)
    column = models.ForeignKey(Column,null=True)

    class Meta:
        db_table = 'article'



