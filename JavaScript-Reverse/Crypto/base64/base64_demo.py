# -*- coding:utf-8 -*-
# @Author: 聆风clark
# @Time: 2021/11/5 6:15 下午
# @File: base64_demo.py
# @project demand:
import base64


def base64_encode(text):
    encode_data = base64.b64encode(text.encode())
    return encode_data


def base64_decode(encode_data):
    decode_data = base64.b64decode(encode_data)
    return decode_data


if __name__ == '__main__':
    text = 'I love Python!'
    encode_data = base64_encode(text)
    decode_data = base64_decode(encode_data)
    print('Base64 编码：', encode_data)
    print('Base64 解码：', decode_data)

# Base64 编码：b'SSBsb3ZlIFB5dGhvbiE='
# Base64 解码：b'I love Python!'
