#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
为你的command line tool写一个 ``setup.py`` 文件, 定义好entry_points文件, 那么
你使用pip安装时就会在Scripts目录下创建一个可执行文件, 然后就可以直接在命令行中
使用这个文件了。
(不需要 ``if __name__ == "__main__": cli()``, 只有你要将该脚本当成命令行工具时
才需要)

ref: http://click.pocoo.org/6/setuptools/
"""

import click

@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!')