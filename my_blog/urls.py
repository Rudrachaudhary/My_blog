"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from blog.views import Home,HomeBlog,TestPage,ThanksPage
from posts.views import (CreatePost,
                         ViewPost,
                         UpdatePost,
                         DeletePost)
from categories.views import (CreateCategory,
                         UpdateCategory,
                         DeleteCategory,
                         ViewCategories)
from tags.views import (ViewTag,
                         CreateTag,
                         UpdateTag,
                         DeleteTag)
from settings.views import (UpdateSetting,
                            ViewSetting,
                            CreateSetting,
                            DeleteSetting)
urlpatterns = [
    path('admin/', admin.site.urls),
    #accounts
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('test/',TestPage.as_view(), name='test'),
    path('thanks/',ThanksPage.as_view(), name='thanks'),
    #posts
    path('post/create/',CreatePost.as_view(), name='create_post'),
    path('view/posts',ViewPost.as_view(), name='view_post'),
    path('post/update/(?P<pk>\d+)/$/',UpdatePost.as_view(), name='update_post'),
    path('post/delete/(?P<pk>\d+)/$/',DeletePost.as_view(), name='delete_post'),
    #category
    path('category/create/',CreateCategory.as_view(), name='create_category'),
    path('category/update/(?P<pk>\d+)/$/',UpdateCategory.as_view(), name='update_category'),
    path('category/delete/(?P<pk>\d+)/$/',DeleteCategory.as_view(), name='delete_category'),
    path('categories/',ViewCategories.as_view(), name='view_categories'),
    #Tags
    path('view/tags',ViewTag.as_view(), name='view_tag'),
    path('tag/create/',CreateTag.as_view(), name='create_tag'),
    path('tag/update/(?P<pk>\d+)/$/',UpdateTag.as_view(), name='update_tag'),
    path('tag/delete/(?P<pk>\d+)/$/',DeleteTag.as_view(), name='delete_tag'),
    #Setting
    path('create/setting/',CreateSetting.as_view(), name='create_setting'),
    path('view/setting',ViewSetting.as_view(), name='view_setting'),
    path('edit/setting/(?P<pk>\d+)/$/',UpdateSetting.as_view(),name='update_setting'),
    path('setting/delete/(?P<pk>\d+)/$/',DeleteSetting.as_view(), name='delete_setting'),
    #HOME
    path('',Home.as_view(),name='home'),
    path('home/blog',HomeBlog.as_view(),name='home_blog'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
