filmlar=[]
for i in range(5):
    film=input(f"{i+1}-Sevimli filmingiz nomini kiriting:  ")
    filmlar.append(film)
print("Sizning sevimli filmlaringiz:")
for film in filmlar:
    print(film)
print(f"Siz {len(filmlar)}ta film kiritdingiz.")