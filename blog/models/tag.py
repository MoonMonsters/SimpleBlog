#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Flynn on 2018-02-25 14:27
from django.db import models


class Tag(models.Model):
	"""
	标签
	"""
	name = models.CharField('名称', max_length=16)
