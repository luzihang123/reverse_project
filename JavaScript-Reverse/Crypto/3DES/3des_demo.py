# -*- coding:utf-8 -*-
# @Author: 聆风clark
# @Time: 2021/11/8 10:14 下午
# @File: 3des_demo.py
# @project demand:
from Cryptodome.Cipher import DES3
from Cryptodome import Random


# 需要补位，str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)


def des_encrypt(key, text, iv):
    # 加密模式 OFB
    cipher_encrypt = DES3.new(add_to_16(key), DES3.MODE_OFB, iv)
    encrypted_text = cipher_encrypt.encrypt(text.encode("utf-8"))
    return encrypted_text


def des_decrypt(key, text, iv):
    # 加密模式 OFB
    cipher_decrypt = DES3.new(add_to_16(key), DES3.MODE_OFB, iv)
    decrypted_text = cipher_decrypt.decrypt(text)
    return decrypted_text


if __name__ == '__main__':
    key = '12345678'  # 密钥，16 位
    text = 'I love Python!'  # 加密对象
    iv = Random.new().read(DES3.block_size)  # DES3.block_size == 8
    secret_str = des_encrypt(key, text, iv)
    print('加密字符串：', secret_str)
    clear_str = des_decrypt(key, secret_str, iv)
    print('解密字符串：', clear_str)

# 加密字符串： b'\xa5\x8a\xd4R\x99\x16j\xba?vg\xf2\xb6\xa9'
# 解密字符串： b'I love Python!'
