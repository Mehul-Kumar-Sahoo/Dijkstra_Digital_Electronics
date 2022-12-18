f=open("rom2.bin",'w+b')
array=[15,5,15,15,5,15,15,15]
binary_format=bytearray(array)
f.write(binary_format)
f.close()