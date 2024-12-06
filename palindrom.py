
latters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
sentences=[]
front=""
back=""
end=False

print("Írj mondatokat ékezet és szimbólumok nélkül ENTER-ig")
while not end:
    text=input("")
    if len(text)!=0:
        db=0
        for letter in text:
            if ord(letter.upper()) >= 65 and ord(letter.upper()) <= 90 or ord(letter.upper()) == 32:
                db+=1
        if db==len(text):
            sentences.append(text)
            print("A mondat elmentve !")
        else:
            print("Hibás szöveg !")
    else:
        print("Az adatok bekérésének vége !")
        print()
        end=True

sentences.sort()
for i in sentences:
    print(i)
    db=0
    for y in i.lower():
        if ord(y.upper()) != 32:
            db+=1
            front+=y
    print("A mondatban lévő bezűk száma:",db)
    for z in reversed(front):
        back+=z
    if back == front:
         print("Palindróma")
    else:
         print("Nem palindróma")
    print(i.upper())
    for x in latters:
        character=i.lower().count(x)
        print(x,":",character)
    print()