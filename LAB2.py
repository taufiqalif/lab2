# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


a = eval(input("masukan nilai a: "))
b = eval(input("masukan nilai b: "))

print("variable a= ", a)
print("variable b= ", b)
print("hasil penggabungan {1} & {0} = %d".format(a,b) %(a+b))

#konversi nilai variable
a = int(a)
b = int(b)
print("hasil penjumlahan {1}+{0} = %d".format(a,b) %(a+b))
print("hasil penjumlahan {1}/{0} = %d".format(a,b) %(a/b))