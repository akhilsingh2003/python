f1=int(input( "enter first feet : "))
i1=int(input( "enter first inches : "))
f2=int(input( "enter second feet : "))
i2=int(input( "enter second inches : "))
sum_f=(f1+f2)+((i1+i2)//12)
sum_i=(i1+i2)%12
print(sum_f,"feet",sum_i,"inches")