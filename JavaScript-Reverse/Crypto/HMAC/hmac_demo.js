// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function HMACEncrypt() {
    var text = "I love python!"
    var key = "secret"
    return CryptoJS.HmacMD5(text, key).toString(); // 9c503a1f852edcc3526ea56976c38edf
    // return CryptoJS.HmacSHA1(text, key).toString();
    // return CryptoJS.HmacSHA256(text, key).toString();
}

console.log(HMACEncrypt())
