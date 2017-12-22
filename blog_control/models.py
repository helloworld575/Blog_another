from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from slugify import slugify

class ArticleColumn(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='article_column')
    column = models.CharField(max_length=200)
    pub = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.column

class ArticleTag(models.Model):
    user = models.ForeignKey(User,related_name='article_tag',on_delete=models.CASCADE)
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.tag

class ArticleModel(models.Model):
    user = models.ForeignKey(User,related_name='article',on_delete=models.CASCADE)
    tag = models.ManyToManyField(ArticleTag,related_name='article_tag',blank=True)
    column = models.ForeignKey(ArticleColumn,related_name='article_column',blank=True,on_delete=models.CASCADE)
    like = models.ManyToManyField(User,related_name='like_users',blank=True)

    create_pub = models.DateTimeField(default=timezone.now)
    update_pub=models.DateTimeField(auto_now=True)
    body = models.TextField()
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering=("title",)
        index_together=(('id','slug'))

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(ArticleModel,self).save(*args,**kwargs)
    '''
    def get_absolute_url();
    def get_path_url();
    '''

class Comment(models.Model):
    article = models.ForeignKey(ArticleModel,related_name='comments',on_delete=models.CASCADE)
    commenter = models.OneToOneField(User,related_name='commenter',on_delete=models.CASCADE)
    text = models.TextField()
    pub = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=("-pub",)

    def __str__(self):
        return "comment by {0} on {1}".format(self.commenter,self.article)
