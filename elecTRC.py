from base64 import b64encode,b64decode
import socket
import time
def xor(val1,val2):
    result=b''
    for a,b in zip(val1,val2):
        result+=bytes([a^b])
    return result




tosol=b'flag_07dff90f4233e272a390.txt'

known=b'AAAAAAAAAAAAAAAAAAAAAAAAA.txt'
c64='68seV6DjWOOhQkMASX4xeevLHleg41jjoS12OXw='

cd64=b64decode(c64)
print(cd64)
assert len(known)==len(cd64)
key=xor(known,cd64)
print(b64encode(xor(key,tosol)).decode())



#CCQCOL+Iy9ZNHDqQt5DN5AgkAji/iMvWTRx1ha6F
