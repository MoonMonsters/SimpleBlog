#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Flynn on 2018-02-25 14:27
from django.db import models


class Category(models.Model):
	"""
	分类
	"""
	name = models.CharField('名称', max_length=16)
