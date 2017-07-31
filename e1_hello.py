#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
option是可选参数, 也就是说凡是 ``--`` 开头的参数就算没有也不影响运行。
"""

import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times.

    Command to execute this::

        python __file__ --count 3 --name Jack
    """
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
