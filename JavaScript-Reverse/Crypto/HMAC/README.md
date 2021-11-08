简介：全称散列消息认证码、密钥相关的哈希运算消息认证码（英文名称：Hash-based Message Authentication Code 或者 Keyed-hash Message Authentication Code），于
1996 年提出，1997 年作为 RFC 2104 被公布，HMAC 加密算法是一种安全的基于加密 Hash 函数和共享密钥的消息认证协议，它要求通信双方共享密钥 key、约定算法、对报文进行 Hash
运算，形成固定长度的认证码。通信双方通过认证码的校验来确定报文的合法性。


Hmac算法也是一种哈希算法，它可以利用MD5或SHA1等哈希算法。不同的是，Hmac还需要一个密钥：
只要密钥发生了变化，那么同样的输入数据也会得到不同的签名，因此，可以把Hmac理解为用随机数“增强”的哈希算法。

参考资料：

- RFC 2104：https://datatracker.ietf.org/doc/rfc2104/
- HMAC 维基百科：https://en.wikipedia.org/wiki/HMAC