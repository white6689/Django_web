"""config URL Configuration

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

import board.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # board
    path('board/', board.views.home), # 게시글 기본 페이지
    path('board/getPost', board.views.create_basic), # 게시글 작성 "제출"/POST
    path('board/getPostForm', board.views.create_form), # 게시글 작성, ModelForm 이용
    path('board/readOne/<int:bid>', board.views.readOne), # 게시글 한개 보기
    path('board/read', board.views.read), # 게시글 다 보기
    path('board/update/<int:bid>', board.views.update), # 게시글 수정
    path('board/delete/<int:bid>', board.views.delete), # 게시글 삭제
    # user
    path('user/signup', user.views.signup), # 회원가입
    path('user/login', user.views.login), # 로그인
    path('user/logout', user.views.logout), # 로그아웃
]
