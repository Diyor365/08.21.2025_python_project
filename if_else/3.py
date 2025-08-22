users=['ali', 'vali', 'hasan', 'husan', 'qobil']
ism= input("Ismingizni kiriting: ")
if ism.lower() == 'admin':
    print(f"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
    if input("HA yoki YO'Q\n").lower() == 'ha':
        print("Foydalanuvchilar ro'yxati:", users)

else: 
    print(f"Xush kelibsiz, {ism}!")
    users.append(ism)