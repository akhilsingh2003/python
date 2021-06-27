# def smallest(lst):
#     for i ,n in enumerate(lst):
#         if n!='0':
#             tmp=lst.pop(i)
#             break
#     return str(tmp)+''.join(lst)    
# # if __name__=='__main__':
        
# A=int(input())
# lst=list(str(A))
# lst.sort()
# print(smallest(lst))

# def smallest(lst):

# 	for i,n in enumerate(lst):

# 		if n != '0':

# 			tmp = lst.pop(i)
# 			break
# 	return str(tmp) + ''.join(lst)
# if __name__ == '__main__':
#     A=int(input())
#     lst = list(str(A))
#     lst.sort()
#     print( smallest(lst))
for i in range(int(input())):
    a=input()
    if(a[0]=="1"):
        b=a[0]+"0"+a[1:]
        print(b)
    else:
        b="1"+a
        print(b)