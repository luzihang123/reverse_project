# -*- coding:utf-8 -*-
# @Author: 聆风clark
# @Time: 2021/11/8 6:38 下午
# @File: hmac_demo.py
# @project demand:
import hmac


def hmac_test1():
    message = b"I love python!"
    key = b'secret'
    md5 = hmac.new(key, message, digestmod='MD5')
    print(md5.hexdigest())


def hmac_test2():
    key = 'secret'.encode('utf-8')
    sha1 = hmac.new(key, digestmod='sha1')
    sha1.update('I love '.encode('utf-8'))
    sha1.update('Python!'.encode('utf-8'))
    print(sha1.hexdigest())


if __name__ == '__main__':
    hmac_test1()  # 9c503a1f852edcc3526ea56976c38edf
    hmac_test2()  # 2d8449a4292d4bbeed99ce9ea570880d6e19b61a
