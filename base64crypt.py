import base64
import random

# Don't Edit CH85!!
CH85 = '!#$%&()*+-0123456789;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`abcdefghijklmnopqrstuvwxyz{|}~'

# Make your own TOKEN_CH85
TOKEN_CH85 = '&*+-167;?ACDIKMNOUWXYZ^`acdekmtwxy{~S@<_q>nL%V8vzj}Q3uJTb!$|hg4s#9FG52(po=HB)lifRErP0'

def disorder(s):
    # 打乱字符串顺序
    ls = list(s)
    n = len(ls)
    
    for i in range(n):
        p = random.randint(0, n-1)
        ls.append(ls.pop(p))
    return ''.join(ls)

def b64encode(v: str)->str:
    # 加密
    d = dict(zip(list(CH85), list(TOKEN_CH85)))
    return ''.join([d[s] for s in str(base64.b85encode(bytes(v, encoding='utf8')), encoding='utf8')])

def b64decode(v: str)->str:
    # 解密
    d = dict(zip(list(TOKEN_CH85), list(CH85)))
    return str(base64.b85decode(bytes(''.join([d[s] for s in v]), encoding='utf8')), encoding='utf8')
