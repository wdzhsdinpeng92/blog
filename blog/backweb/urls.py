
from django.conf.urls import url
from django.conf.urls.static import static

from backweb import views
from blog.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    # 博客首页
    # 127.0.0.1:8090/backweb/index/
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^article/',views.article,name='article'),
    url(r'^category/',views.category,name='category'),
    url(r'^del_category/(\d+)/',views.del_category,name='del_category'),
    url(r'^update_category/(\d+)/', views.update_category, name='update_category'),
    url(r'^add_article/',views.add_article,name='add_article'),
    url(r'^del_article/(\d+)/',views.del_article,name='del_article'),
    url(r'^edit_article/(\d+)/',views.edit_article,name='edit_article'),
]

urlpatterns +=static(MEDIA_URL,document_root=MEDIA_ROOT)