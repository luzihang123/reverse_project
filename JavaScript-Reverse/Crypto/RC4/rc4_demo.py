# -*- coding:utf-8 -*-
# @Author: 聆风clark
# @Time: 2021/11/8 10:25 下午
# @File: rc4_demo.py
# @project demand:
import base64
from Cryptodome.Cipher import ARC4


def rc4_encrypt(key, t):
    enc = ARC4.new(key.encode('utf8'))
    res = enc.encrypt(t.encode('utf-8'))
    res = base64.b64encode(res)
    return res


def rc4_decrypt(key, t):
    data = base64.b64decode(t)
    enc = ARC4.new(key.encode('utf8'))
    res = enc.decrypt(data)
    return res


if __name__ == "__main__":
    secret_key = '12345678'  # 密钥
    text = 'I love Python!'  # 加密对象
    encrypted_str = rc4_encrypt(secret_key, text)
    print('加密字符串：', encrypted_str)
    decrypted_str = rc4_decrypt(secret_key, encrypted_str)
    print('解密字符串：', decrypted_str)

# 加密字符串： b'8tNVu3/U/veJR2KgyBw='
# 解密字符串： b'I love Python!'
