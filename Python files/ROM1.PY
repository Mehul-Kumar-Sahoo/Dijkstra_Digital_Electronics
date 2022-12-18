f=open("rom1.bin",'w+b')
array=[6,15,5,2,2,15,15,15]
binary_format=bytearray(array)
f.write(binary_format)
f.close()