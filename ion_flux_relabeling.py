# Ram Mohan

def locate(top,num,under):
    under=under//2
    right=top-1
    left=top-1-under
    if right==num or left==num:
        return top
    else:
        if num<=left:
            return locate(left, num, under)
        else:
            return locate(right,num,under)
def answer(h,q):
    head=(2**h)-1
    result=[]
    for i in range(len(q)):
        if q[i]<head and q[i]>=1:
            x=locate(head,q[i],head-1)
            print(x)
            result.append(x)
        else:
            result.append(-1)
            return result
print(answer(4,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
