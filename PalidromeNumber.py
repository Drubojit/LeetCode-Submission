x=input()
rev = x[::-1]
flag = True
if len(x) != len(rev):
    flag = False
else:
    if x!=rev:
        flag = False

print(flag)