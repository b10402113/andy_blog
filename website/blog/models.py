from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name="文章分類")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '文章分類'
        verbose_name_plural = '文章分類'
class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name="文章分類")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '標籤'
        verbose_name_plural = '標籤'
class Entry(models.Model):
    entry_title = models.CharField(max_length=128, verbose_name="文章標題")

    entry_img = models.ImageField(upload_to='blog_images',null=True,blank=True,verbose_name="文章圖片")

    entry_body = models.TextField(verbose_name='文章正文')

    entry_abstract = models.TextField(max_length=256,null=True,blank=True,verbose_name='文章摘要')

    entry_visiting = models.PositiveIntegerField(default=0, verbose_name="觀看次數")

    category = models.ManyToManyField('Category',verbose_name="文章類別")

    tags = models.ManyToManyField('Tag',verbose_name="文章標籤")

    entry_author = models.ForeignKey(User, verbose_name="文章作者",on_delete=models.CASCADE)

    created_time = models.DateTimeField(auto_now_add=True,verbose_name='創建時間')

    modified_time = models.DateTimeField(auto_now_add=True,verbose_name='修改時間')

    isFeatured = models.BooleanField(default=None,verbose_name='特色文章')

    def __str__(self):
        return self.entry_title

    def get_absolute_url(self):
        return reverse('blog:blog_detail',kwargs={'blog_id':self.id})

    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章'
        verbose_name_plural = '文章'