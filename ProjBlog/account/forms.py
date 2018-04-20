#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : haolv
from django.contrib.auth import authenticate,login

from  django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

from  django import forms

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密码',widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password do not match')
        return cd['password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth','phone')

from django.contrib.auth import forms as auth_forms
class PasswordResetForm(auth_forms.PasswordResetForm):
    email = forms.EmailField(label="邮箱", max_length=254)

