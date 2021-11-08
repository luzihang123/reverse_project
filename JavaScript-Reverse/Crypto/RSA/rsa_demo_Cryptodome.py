# -*- coding:utf-8 -*-
# @Author: 聆风clark
# @Time: 2021/11/8 10:58 下午
# @File: rsa_demo.py
# @project demand:
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5

data = "cKK8B2rWwfwWeXhz"
public_key = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAM1xhOWaThSMpfxFsjV5YaWOFHt+6RvS+zH2Pa47VVr8PkZYnRaaKKy2MYBuEh7mZfM/R1dUXTgu0gp6VTNeNQkCAwEAAQ=="
rsa_key = RSA.import_key(base64.b64decode(public_key))  # 导入读取到的公钥
cipher = PKCS1_v1_5.new(rsa_key)  # 生成对象
cipher_text = base64.b64encode(cipher.encrypt(data.encode(encoding="utf-8")))
print(cipher_text)
