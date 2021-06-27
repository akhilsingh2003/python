try:

    for i in range(int(input())):
        a=input()
        b=len(a)-1
        if (a[:2]=="</" and a[-1]==">"):
            if (a[2:b].isalnum() and a[2:b].islower()) :
                print("Success")
            elif (a[2:b].isnumeric()):
                print("Success")
            else:
                print("Error")
        else:
            print("Error")
except:
    pass            