#
"""
A
BB
CCC
DDDD
EEEEE
"""



for i in range(5):  # 5 lines ke liye
    ch = chr(65 + i)  # 65 = 'A' ka ASCII code
    print(ch * (i + 1))
