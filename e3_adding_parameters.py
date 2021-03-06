#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Argument是指强制要求的参数。
"""

import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)
        
if __name__ == "__main__":
    hello()