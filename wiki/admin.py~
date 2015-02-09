from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


class ArticleAdmin(MarkdownModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
# Next line is a workaround for Python 2.x
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
admin.site.register(models.Article, ArticleAdmin)

