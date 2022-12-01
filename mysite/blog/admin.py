from django.contrib import admin  # admin 클래스(me)
from .models import Post, Category, Tag, Comment  # 클래스로 선언된 Post를 인식시키기 위해 import함. 온점은 현재 있는 곳에서.(me)
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin)  # site에 Post 모델을 register 하겠다(me)
admin.site.register(Comment)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  #


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)  # post와 달리 카테고리는 name 필드를 넣어주면 slug라고 하는 코드 값이 자동으로 만들어지도록
# 만들어 주어야 한다. 그래서 CategoryAdmin을 전달하고 그 클래스를 만들었다.
admin.site.register(Tag, TagAdmin)
