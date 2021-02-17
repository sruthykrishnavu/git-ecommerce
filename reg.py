import re

txt = "Hello,Iam sruthy.her name is sruthy"
x = re.findall("sruthy$", txt)
if x:
  print("Yes, the string starts with 'hello'")
  print(x)
else:
  print("No match")

