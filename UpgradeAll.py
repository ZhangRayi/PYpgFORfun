# Copyright (c) 2019 Zhang_Ray
#
# -*- coding:utf-8 -*-
# @Script: up.py
# @作者: Zhang_Ray
# @Email: 1228506574@qq.com
# @Create At: 2019-04-27 17:08:41
# @最后编辑者: Zhang_Ray
# @最后编辑时间: 2019-04-27 17:09:27
# @文件说明: This is upgrade python wheel/sdist.

import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions
for dist in get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)