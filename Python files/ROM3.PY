f=open("rom3.bin",'w+b')
array=[15,2,15,15,1,15,15,15]
binary_format=bytearray(array)
f.write(binary_format)
f.close()