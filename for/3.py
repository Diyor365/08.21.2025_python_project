Suxbatdosh=int(input("Bugun suxbatlashgan odamlaringiz sonini kiriting: "))
Suxbatdoshlar=[]
for i in range(Suxbatdosh):
    ism=input(f"{i+1}-Suxbatdoshingiz ismini kiriting: ")
    Suxbatdoshlar.append(ism)
print("Suxbatdoshlaringiz:")
for ism in Suxbatdoshlar:
    print(ism)