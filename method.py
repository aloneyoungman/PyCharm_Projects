a=(3,2)

def CetOnlyEven(spisok: list)-> list:
    b=[]
    if type(spisok)==list:
        for i in range(len(spisok)):
            if i%2==0:
                 b.append(spisok[i])
        return b
    else:
         return "ArgumentError"
print(CetOnlyEven(1))

def OrderString(string: str)->str:
    if type(string)==str:
        return "".join(sorted(string))
    else:
        return "ArgumentError"
print(OrderString(a))