f=open("rom5.bin",'w+b')
array=[15,15,15,15,15,15,15,15]
binary_format=bytearray(array)
f.write(binary_format)
f.close()