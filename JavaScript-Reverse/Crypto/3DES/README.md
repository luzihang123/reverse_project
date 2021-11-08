简介：全称三重数据加密算法（英文名称：Triple Data Encryption Standard、 Triple Data Encryption Algorithm、TDES、TDEA），是对称加密算法中的一种。70 年代初由 IBM
研发，后 1977 年被美国国家标准局采纳为数据加密标准，它相当于是对每个数据块应用三次 DES 加密算法。由于计算机运算能力的增强，原版 DES 密码的密钥长度变得容易被暴力破解；3DES 即是设计用来提供一种相对简单的方法，即通过增加
DES 的密钥长度来避免破解，所以严格来说 3DES 不是设计一种全新的块密码算法。

- mode 支持：CBC，CFB，CTR，CTRGladman，ECB，OFB 等。
- padding 支持：ZeroPadding，NoPadding，AnsiX923，Iso10126，Iso97971，Pkcs7 等。

参考资料：

- RFC 1851：https://datatracker.ietf.org/doc/rfc1851/
- 3DES 维基百科：https://en.wikipedia.org/wiki/Triple_DES