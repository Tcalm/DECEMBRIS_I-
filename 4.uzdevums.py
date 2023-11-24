iev = int(input("Ievadiet skaitli: "))

if iev < 0:
    print("Skaitļiem zem 0 nav faktoriāla")
else:
    fak = 1
    for sk in range(1, iev + 1):
        fak *= sk
    print(f"Skaitļa {iev} faktoriāls ir: {fak}")