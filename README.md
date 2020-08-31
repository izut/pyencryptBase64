# pyencryptBase64
基于base64的Token加密

# Usage:
1. 生成自己的TOKEN_CH85

        # 使用生成的字符串替换TOKEN_CH85
        token = disorder(CH85)
        print(token)
    
2. 加密解密


        s = '兔耳草'
        encoded_s = b64encode(s)
        print(encoded_s)
  
        decoded_s = b64decode(encoded_s)
        print(decoded_s)
