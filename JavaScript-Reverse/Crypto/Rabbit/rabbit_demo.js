// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function rabbitEncrypt() {
    return CryptoJS.Rabbit.encrypt(text, key).toString();
}

function rabbitDecrypt() {
    return CryptoJS.Rabbit.decrypt(encryptedData, key).toString(CryptoJS.enc.Utf8);
}

var text = "I love Python!"
var key = "6f726c64f2c2057"

var encryptedData = rabbitEncrypt()
var decryptedData = rabbitDecrypt()

console.log("加密字符串: ", encryptedData)
console.log("解密字符串: ", decryptedData)

// 加密字符串:  U2FsdGVkX1+ZVCHRXlhmG5Xw87YPWMNIBlbukuh8
// 解密字符串:  I love Python!
