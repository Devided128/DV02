for i in range(2, 100):
    for x in range(2, i):
        print(f"Kontroluji číslo {i} dělené číslem {x}")
        if i % x == 0:
            break
    else:
        print(f"Číslo {i} je prvočíslo")
