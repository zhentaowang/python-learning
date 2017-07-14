#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 一个简单的条件循环实现汉诺塔


def my_print(args):
    print args


def move(n, a, b, c):
    my_print((a, '-->', c)) if n == 1 else (move(n-1, a, c, b) or move(1, a, b, c) or move(n-1, b, a, c))

move(3, 'a', 'b', 'c')

