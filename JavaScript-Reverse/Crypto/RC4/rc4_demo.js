// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function RC4Encrypt() {
    return CryptoJS.RC4.encrypt(text, key).toString();
}

function RC4Decrypt() {
    return CryptoJS.RC4.decrypt(encryptedData, key).toString(CryptoJS.enc.Utf8);
}

var text = "I love Python!"
var key = "6f726c64f2c2057c"

var encryptedData = RC4Encrypt()
var decryptedData = RC4Decrypt()

console.log("加密字符串: ", encryptedData)
console.log("解密字符串: ", decryptedData)

// 加密字符串:  U2FsdGVkX18hMm9WWdoEQGPolnXzlg9ryArdGNwv
// 解密字符串:  I love Python!
