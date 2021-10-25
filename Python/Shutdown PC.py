import os

print("Enter Number of Seconds to Shutdown System : ")
sec = int(input())
print("PC is about to shutdown in",sec,"seconds")

strOne = "shutdown /s /t "
strTwo = str(sec)
str = strOne+strTwo

os.system(str)
