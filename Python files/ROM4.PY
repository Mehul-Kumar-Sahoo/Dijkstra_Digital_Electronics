f=open("rom4.bin",'w+b')
array=[15,2,5,1,15,15,15,15]
binary_format=bytearray(array)
f.write(binary_format)
f.close()