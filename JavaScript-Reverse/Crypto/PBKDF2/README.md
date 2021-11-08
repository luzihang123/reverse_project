简介：英文名称：Password-Based Key Derivation Function 2，PBKDF2 是 RSA 实验室的公钥加密标准（PKCS）系列的一部分，2017 年发布的 RFC 8018 （PKCS #5 v2.1）推荐使用 PBKDF2 进行密码散列。PBKDF2 将伪随机函数（例如 HMAC），把明文和一个盐值（salt）作为输入参数，然后进行重复运算，并最终产生密钥，如果重复的次数足够大，破解的成本就会变得很高。

参考资料：
- RFC 8018：https://datatracker.ietf.org/doc/rfc8018/
- PBKDF2 维基百科：https://en.wikipedia.org/wiki/PBKDF2