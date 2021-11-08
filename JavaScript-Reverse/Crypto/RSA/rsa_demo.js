// 引用 node-rsa 加密模块
var NodeRSA = require('node-rsa');

function rsaEncrypt() {
    pubKey = new NodeRSA(publicKey, 'pkcs8-public');
    var encryptedData = pubKey.encrypt(text, 'base64');
    return encryptedData
}

function rsaDecrypt() {
    priKey = new NodeRSA(privatekey, 'pkcs8-private');
    var decryptedData = priKey.decrypt(encryptedData, 'utf8');
    return decryptedData
}

var key = new NodeRSA({b: 512});                    //生成512位秘钥
var publicKey = key.exportKey('pkcs8-public');    //导出公钥
var privatekey = key.exportKey('pkcs8-private');  //导出私钥
var text = "I love Python!"

var encryptedData = rsaEncrypt()
var decryptedData = rsaDecrypt()

console.log("公钥:\n", publicKey)
console.log("私钥:\n", privatekey)
console.log("加密字符串: ", encryptedData)
console.log("解密字符串: ", decryptedData)

/*
公钥:
 -----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAOV1BwTJSVce/QjJAro5fXG9WzOpal09
Qtv1yuXKE81vZSNTHxW6dICwPT/kjCfC3bA5Qs6wnYBANuwD6wlAS0UCAwEAAQ==
-----END PUBLIC KEY-----
私钥:
 -----BEGIN PRIVATE KEY-----
MIIBVAIBADANBgkqhkiG9w0BAQEFAASCAT4wggE6AgEAAkEA5XUHBMlJVx79CMkC
ujl9cb1bM6lqXT1C2/XK5coTzW9lI1MfFbp0gLA9P+SMJ8LdsDlCzrCdgEA27APr
CUBLRQIDAQABAkAiXwJbJC+5PioXG80tyhjRZdT4iyMkrl2Kh2oKO9f1iLaBXLya
D0HW82wFh+cUy8GcMl9jse8DE8wd1TdORmHhAiEA/rwmWjXHVgDqcH/fqk8Ufku0
fXvs56h5QDoh1so5vokCIQDmmL3JDW6Y7RuK2qwFbHBZtYPRFRVdn5X1oqU2FOSX
3QIhAOVTjVN5RtNuT6Cn/jvcpZ5tmTe+8TA8w6vGqeAsfn/BAiBvKKIUEQ2HWoU0
YkUaODPQiteIKomqIAvB5S2O7HNlYQIgWMuLUxGZbbcAmIX+YmRXuET97S7OWv+z
WHVfb/rbXtI=
-----END PRIVATE KEY-----
加密字符串:  hHXTF1K3w55Wd6OSjVYtqxceJ5VhlySNUahel9pwKD92Ef7wIT7DYPuJRKiqz5tuHtUqujbmbZBSL0qDE/EA+A==
解密字符串:  I love Python!
*/
