// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function tripleDesEncrypt() {
    var key = CryptoJS.enc.Utf8.parse(desKey),
        iv = CryptoJS.enc.Utf8.parse(desIv),
        srcs = CryptoJS.enc.Utf8.parse(text),
        // ECB 加密方式，Iso10126 填充方式
        encrypted = CryptoJS.TripleDES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Iso10126
        });
    return encrypted.toString();
}

function tripleDesDecrypt() {
    var key = CryptoJS.enc.Utf8.parse(desKey),
        iv = CryptoJS.enc.Utf8.parse(desIv),
        srcs = encryptedData,
        // ECB 加密方式，Iso10126 填充方式
        decrypted = CryptoJS.TripleDES.decrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Iso10126
        });
    return decrypted.toString(CryptoJS.enc.Utf8);
}

var text = "I love Python!"       // 待加密对象
var desKey = "6f726c64f2c2057c"    // 密钥
var desIv = "0123456789ABCDEF"    // 偏移量

var encryptedData = tripleDesEncrypt()
var decryptedData = tripleDesDecrypt()

console.log("加密字符串: ", encryptedData)
console.log("解密字符串: ", decryptedData)

// 加密字符串:  3J0NX7x6GbewjjhoW2HKqg==
// 解密字符串:  I love Python!
