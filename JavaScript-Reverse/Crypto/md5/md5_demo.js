// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function MD5Test() {
    var text = "I love python!"
    return CryptoJS.MD5(text).toString()
}

console.log(MD5Test())  // 21169ee3acd4a24e1fcb4322cfd9a2b8