uname=input("name: ")
uname=uname.upper()
name=""
for i in uname:
    if i in ("AEIOU"):
        continue
    name+=i

print(name)