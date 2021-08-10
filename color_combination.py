colors=input()
c_list=[]
for color in colors:
    if color.isalpha():
        c_list.append(color)
while(len(c_list)!=1):
    c=1
    while(len(c_list)>len(c_list)-1):
        if c_list[c]=="R" and c_list[c-1]=="G":
            c_list[c]="B"
            c_list.pop(c-1)
            break
        elif c_list[c]=="B" and c_list[c-1]=="G":
            c_list[c]="R"
            c_list.pop(c-1)
            break   
        elif c_list[c]=="R" and c_list[c-1]=="B":
            c_list[c]="G"
            c_list.pop(c-1)
            break            
        elif c_list[c]=="G" and c_list[c-1]=="R":
            c_list[c]="B"
            c_list.pop(c-1)
            break       
        elif c_list[c]=="G" and c_list[c-1]=="B":
            c_list[c]="R"
            c_list.pop(c-1)
            break    
        elif c_list[c]=="B" and c_list[c-1]=="R":
            c_list[c]="G"
            c_list.pop(c-1)
            break    
        else:
            c+=1
print("",end="")
print(*c_list,end="")
print("")