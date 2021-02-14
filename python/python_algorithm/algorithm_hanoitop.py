def move(n,sp,ep,boo):
	if n > 1:
		move(n-1,sp,6-sp-ep,boo)
	print(str(sp)+" "+str(ep))
	if n > 1:
		move(n-1,6-sp-ep,ep,boo)

n = int(input())
boo = True
print(2**n-1)
if n <=  20:
	move(n,1,3,boo)


