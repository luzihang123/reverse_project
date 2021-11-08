// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function pbkdf2Encrypt() {
    var text = "I love Python!"
    var salt = "43215678"
    // key 长度 128，10 次重复运算
    var encryptedData = CryptoJS.PBKDF2(text, salt, {keySize: 128 / 32, iterations: 10});
    return encryptedData.toString()
}

console.log(pbkdf2Encrypt())  // 7fee6e8350cfe96314c76aaa6e853a50
