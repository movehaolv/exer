from django.contrib import admin

from .models import BlogArticles
#admin.site.register(BlogArticles)   # 将该类注册到admin中
# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish')
    list_filter = ('publish','author')
    search_fields = ('title','body','publish')   # 不能写author，因为foreigenKey
    raw_id_fields = ('author',)   # 在admin后台类中加入raw_id_fields（只适用于外键）后，会显示外键的详细信息
    date_hierarchy = 'publish'
    ordering = ['publish','author']
    # pass
admin.site.register(BlogArticles,BlogArticlesAdmin)

