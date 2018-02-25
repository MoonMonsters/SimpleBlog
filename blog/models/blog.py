#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Flynn on 2018-02-25 14:28
from django.db import models
from .category import Category
from .tag import Tag


class Blog(models.Model):
	"""
	博客
	"""
	title = models.CharField('标题', max_length=32)
	author = models.CharField('作者', max_length=16)
	content = models.TextField('正文')
	created = models.DateTimeField('发布时间', auto_now_add=True)

	category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
	tags = models.ForeignKey(Tag, verbose_name='标签', on_delete=models.CASCADE)
