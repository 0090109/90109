q1= input('請輸入x值')
w2= input("請輸入y值")
e3= input("請輸入z值")

a=(float(q1))
b=(float(w2))
c=(float(e3))

x=(b*b-4*a*c)
if x<=0:
    print("無")

else:
     d=(-b+(b*b-4*a*c)**0.5)/(2*a) 
     e=(-b-(b*b-4*a*c)**0.5)/(2*a)  
     print("x1=",d,"x2=",e)
