#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Flynn on 2018-02-25 14:31
from django.db import models
from .blog import Blog


class Comment(models.Model):
	"""
	评论
	"""
	blog = models.ForeignKey(Blog, verbose_name='博客', on_delete=models.CASCADE)

	# 用户信息
	name = models.CharField('称呼', max_length=16)
	email = models.EmailField('邮箱')
	content = models.CharField('内容', max_length=140)
	# 评论时间
	created = models.DateTimeField('发表时间', auto_now_add=True)
