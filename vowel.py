a=input(" enter the string ")
count_v=0
count_c=0
count_s=0
count_num=0
count_sp=0

for x in a:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
         count_v+=1
    elif x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
         count_v+=1
    elif x=="0" or x=="1" or x=="2" or x=="3" or x=="4" or x=="5" or x=="6" or x=="7" or x=="8" or x=="9" :
        count_num+=1
    elif x==" ":
        count_s+=1
    elif x!="a" and x!="e" and x!="i" and x!="o" and x!="u" :
        count_c+=1
    elif x!="A" and x!="E" and x!="I" and x!="O" and x!="U" :
        count_c+=1
    else:
        count_sp+=1
print("vowels =",count_v)
print("consonants =",count_c)
print("numbers =",count_num)
print("spaces =",count_s)
print("special character =",count_sp)    