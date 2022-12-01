from django.db import models  # import한 models라는 클래스
from django.contrib.auth.models import User
import os
from markdownx.models import MarkdownxField
from markdownx.utils import markdown


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # 카테고리는 중복되지 않아야 하므로, 동일한 카테고리명이 등록되지 않도록 한다(unique)
    slug = models.SlugField(max_length=200, unique=True,
                            allow_unicode=True)  # SlugField : 숫자 pk 대신, 읽을 수 있는 텍스트로 url 만들고 싶을 때 사용. unique, allow_unicode(한글도 사용 가능)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)  # 꼭 작성할 필요는 없어서 blank=True(me)
    content = MarkdownxField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)  # _media 아래에 생성된다
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # myInternetPrj-settings.py -Line110,116 바꿔주었음(me)
    updated_at = models.DateTimeField(auto_now=True)

    # author #작성자에 대한 부분은 테이블을 따로 만들어서 id로 연결했었다(7-4). 추후 작성(me)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):  # 이 함수가 p 그 자체였던 듯. {{ p }} 했는데 [1] 첫번째 포스트. 이게 나왔다(me)
        return f'[{self.pk}]{self.title} :: {self.author}'  # self = Post Object. 0001_initial.py에 자동생성되었던 id 필드의 primary_key(me)

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):  # 파일 앱이 저장된 모든 path(경로) 중 확장자 포함한 파일 이름만 가져오는 함수(me)
        return os.path.basename(self.file_upload.name)  # 파일 관련 함수는 import os 필요(me)

    def get_file_ext(self):  # 확장자만 가져오는 함수(me)
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'https://doitdjango.com/avatar/id/379/9ff1a6a6bc11ac6f/svg/{self.author.email}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'https://doitdjango.com/avatar/id/379/9ff1a6a6bc11ac6f/svg/{self.author.email}'
