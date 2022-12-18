f=open("rom0.bin",'w+b')
array=[15,6,15,1,15,15,15,15]
binary_format=bytearray(array)
f.write(binary_format)
f.close()