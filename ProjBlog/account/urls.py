#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : haolv

from django.conf.urls import url
from account import views

from django.contrib.auth import views as auth_views

from account.forms import PasswordResetForm

urlpatterns = [
    url(r'own_login/$',views.user_login,name='user_login'),   # 自定义登录
    url(r'login/$',auth_views.login,{"template_name":"account/login.html"},name='user_login'),   # django内置登录，p56
    url(r'login_out/$',auth_views.logout,{'template_name':'account/logout.html'},name='user_logout'),
    url(r'register/$',views.register,name='user_register'),   # django的注册没有内置方法，因为注册过程，网站需求不同
    # 密码修改
    url(r'password_change/$',auth_views.password_change,{'post_change_redirect':'/account/password_change_done'},name='password_change'),  # 这里是将源码重写，当然你也可以自定义模板，下面的密码重置就是自定义模板和上面的login&&login_out
    url(r'password_change_done/$',auth_views.password_change_done,name='password_change_done'),
    # 密码重置
    url(r'password_reset/$',auth_views.password_reset,{'password_reset_form':PasswordResetForm,'template_name':'account/password_reset_form.html','email_template_name':'account/password_reset_email.html','subject_template_name':'account/password_reset_subject.txt','post_reset_redirect':'account/password_reset_done'},name='password_reset'),
    url(r'password_reset_done/$',auth_views.password_reset_done,{'template_name':'account/password_reset_done.html'},name='password_reset_done'),
    #url(r'password_reset_email/$',auth_views.password_reset_email,{'template_name':'account/password_reset_email.html'},name='password_reset_email'),
    url(r'password_reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,{'template_name':'account/password_reset_confirm.html','post_reset_redirect':'account/password_reset_complete'},name='password_reset_confirm'),
    url(r'password_reset_complete',auth_views.password_reset_complete,{'template_name':'account/password_reset_complete.html'},name='password_reset_complete'),
]

