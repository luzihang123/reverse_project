简介：全称数据加密标准（英文名称：Data Encryption Standard），加密与解密使用同一密钥，属于对称加密算法，1977 年被美国联邦政府的国家标准局确定为联邦资料处理标准（FIPS），DES 是一个分组加密算法，使用 56
位的密钥（一般认为密钥是 64 位，但是密钥的每个第 8 位设置为奇偶校验位，所以实际上有效位只有 56 位），由于 56 位密钥长度相对较短，所以 DES 是不安全的，现在基本上已被更高级的加密标准 AES 取代。

- mode 支持：CBC，CFB，CTR，CTRGladman，ECB，OFB 等。
- padding 支持：ZeroPadding，NoPadding，AnsiX923，Iso10126，Iso97971，Pkcs7 等。

参考资料：

- RFC 4772：https://datatracker.ietf.org/doc/rfc4772/
- DES 维基百科：https://en.wikipedia.org/wiki/Data_Encryption_Standard