"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from blogapp import views
from accounts import views as accounts_views  #다른이름으로 쓰겠다(as)
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.first,name='first'),

    path('home/',views.home,name='home'),
    
    #html form을 이용해 블로그 객체 만들기
    path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),
    
    #django form을 이용해 블로그 객체 만들기
    path('formcreate/',views.formcreate,name='formcreate'), 
    
     #django modelform을 이용해 블로그 객체 만들기
    path('modelformcreate/',views.modelformcreate,name='modelformcreate'), 
    
    # 127.0.0.1:8000/detail/1
    # 127.0.0.1:8000/detail/2
    # 127.0.0.1:8000/detail/3
    path('detail/<int:blog_id>', views.detail, name='detail'),
    
    path('create_comment/<int:blog_id>', views.create_comment,name='create_comment'),
    
    path('login/',accounts_views.login,name='login'),
    
    path('logout/',accounts_views.logout,name='logout'),
    
    path('signup/',accounts_views.signup, name='signup'),

    path('again_signup/',accounts_views.again_signup, name='again_signup'),

    path('mbti/', accounts_views.mbti, name='mbti'),

    path('delete/<int:blog_id>', views.delete_blog, name='delete'),

    path('update/<int:blog_id>', views.update, name='update'),
    
    path('delete_comment/<int:blog_id>/<int:comment_id>', views.delete_comment, name='delete_comment'),

    path('update_comment/<int:blog_id>/<int:comment_id>', views.update_comment, name='update_comment'),

    # path('edit/<int:blog_id>', views.edit_blog, name='edit'),

    # path('create_post/<str:username>', views.create_post, name='create_post'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  

 # media 파일에 접근할 수 있는 url도 추가해주어야함
