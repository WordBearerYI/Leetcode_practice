a = ['A','D','A','A']
b = ['D','A','C','B','C']
print a
print b
#i canner can can as many cans as a canner can cans
n = [0]*min(len(b),len(a))
def LCS_topDown(x1,x2):
    if x1<0 or x2<0:
        return 0
    if m1[x1][x2]==-1:
        if a[x1]==b[x2]:
            n.append(a[x1])
            m1[x1][x2]= 1+LCS_topDown(x1-1,x2-1)
            return 1+LCS_topDown(x1-1,x2-1)
        else:
            m1[x1][x2]=max(LCS_topDown(x1,x2-1),LCS_topDown(x1-1,x2))
            return max(LCS_topDown(x1,x2-1),LCS_topDown(x1-1,x2))
    else:
        return m1[x1][x2]

def LCS_botUp(a1,a2):
    m= [0]*(len(a1)+1)
    print 'size a1:',len(a1),' size a2:',len(a2), ' len memoization:',len(m)
    for i in range(1,len(a2)+1):
        for j in range(1,len(a1)+1):
            if a1[j-1]==a2[i-1]:
                m[j]= m[j-1]+1
            else:
		        m[j] = max(m[j],m[j-1])
	print m
    print [a1[k] for k in range(len(m)-1) if m[k]<m[k+1]]

m1 = [[-1]*len(b) for q in range(len(a))]
print 'recursive topDown:',LCS_topDown(len(a)-1,len(b)-1)

LCS_botUp(a,b)
