from django.contrib import admin

# Register your models here.
from main.models import Blog, Tag, Category, Comment, Words
#admin.site.register([Category, Tag, Comment, Words])
admin.site.site_header = 'Kevin site 后台管理'
admin.site.site_title = 'Kevin admin'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'created', 'category', 'tags', 'summary']

    list_per_page = 50

    ordering = ('-created',)

    list_editable = ['category', ]

    search_fields = ('title', 'author', 'content')

    def tags(self, obj):
        tag = [x.name for x in obj.tag.all()]
        return tag

    tags.short_description = "标签"

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            'js/kindeditor/kindeditor-all.js',
            'js/kindeditor/lang/zh-CN.js',
            'js/kindeditor/config.js',
        )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)

    list_per_page = 50


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ('name',)

    list_per_page = 50

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'blog', 'email', 'created')

    list_per_page = 50

    ordering = ('-created',)

@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'created')

    list_per_page = 50

    ordering = ('-created',)