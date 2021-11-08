// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js');

function SHA1Encrypt() {
    var text = "I Love Python!"
    return CryptoJS.SHA1(text).toString();
}

console.log(SHA1Encrypt())
// ec84876f213c0a68a5448d736fdb84f3b9ceab5b