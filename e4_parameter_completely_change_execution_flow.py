#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
有的时候某个参数会彻底的改变整个行为，比如 ``--help``, ``--version`` 会导致
其他所有的命令都被忽略。这种参数如何定义呢？

Ref:

- http://click.pocoo.org/5/options/#callbacks-and-eager-options
- http://click.pocoo.org/5/advanced/#callback-evaluation-order
"""

__version__ = "0.0.1"

import click


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo("Version %s" % __version__)
    ctx.exit()


@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def run():
    click.echo("Hello!")


def test_run():
    """
    如何测试命令行工具。
    """
    from click.testing import CliRunner

    runner = CliRunner()

    result = runner.invoke(run, ["--version"])
    assert __version__ in result.output

    result = runner.invoke(run)
    assert "Hello!" in result.output


test_run()

if __name__ == "__main__":
    run()
