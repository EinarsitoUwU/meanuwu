import sys
print("Insert data")
i=0
b=0
a=0
count=0
try:
    num=int(sys.argv[1])
except:
    print("Argument Integer number")
    num = None

if num == None:
    while i == 0:
        count=count+1
        a = float(input(":"))
        a = b + a
        b=a
        o=input("Continue? ")
        if o == "y":
            i = 0
        else:
            i = 1
    b="{:.2f}".format(b/count)
    print("average",b)
else:
    for i in range(0,num,1):
        a = float(input(":"))
        a = b + a
        b=a
    b="{:.2f}".format(b/num)
    print("average",b)
