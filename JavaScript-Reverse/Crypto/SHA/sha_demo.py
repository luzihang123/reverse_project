# -*- coding:utf-8 -*-
# @Author: 聆风clark
# @Time: 2021/11/8 6:10 下午
# @File: sha_demo.py
# @project demand:
import hashlib


def sha1_text1():
    sha1 = hashlib.new('sha1', 'I Love Python!'.encode('utf-8'))
    print(sha1.hexdigest())  # ec84876f213c0a68a5448d736fdb84f3b9ceab5b


def sha1_text2():
    sha1 = hashlib.sha1()
    sha1.update('I Love Python!'.encode('utf-8'))
    print(sha1.hexdigest())  # ec84876f213c0a68a5448d736fdb84f3b9ceab5b


if __name__ == '__main__':
    sha1_text1()
    sha1_text2()
