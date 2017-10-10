#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nesting Command是指将多个命令行参数合并在一个文件下, 并用函数名区分不同的命令。
当然你可以在@click.command中指定命令名称。
"""

import click


@click.group()
def cli():
    pass


@cli.command("init")
def initdb():
    """Command to execute this::

        python __file__ init 
    """
    click.echo('Initialized the database')


@cli.command("drop")
def dropdb():
    """Command to execute this::

        python __file__ drop
    """
    click.echo('Dropped the database')


if __name__ == "__main__":
    # cli()
    print(initdb())