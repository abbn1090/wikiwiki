from django.conf.urls import patterns, include, url
from . import views
from models import Article

urlpatterns = patterns('',
 
        
        url(r'^$', views.ArticleIndex.as_view(), name='wiki_article_index'),#as_view():Returns a callable view that takes a request and returns a response
url(r'^article/(?P<slug>[-\w]+)$', views.ArticleDetail.as_view(), name='wiki_article_detail'),
    url(r'^history/(?P<slug>[-\w]+)$',
        'wiki.views.article_history',
        name='wiki_article_history'),
    url(r'^add/article$',
        'wiki.views.add_article',
        name='wiki_article_add'),
    url(r'^edit/article/(?P<slug>[-\w]+)$',
        'wiki.views.edit_article',
        name='wiki_article_edit'),
)
