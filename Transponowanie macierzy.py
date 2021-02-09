wielkosc_macierzy = input().split()

x = int(wielkosc_macierzy[0])  
y = int(wielkosc_macierzy[1])  

macierz = []
for i in range(x):
    wiersz = input().split()
    macierz.append(wiersz)

wiersz_po_transponowaniu = []
for j in range(y):  
    for v in macierz:  
        wiersz_po_transponowaniu.append( 
            v[j])  

    print(" ".join(wiersz_po_transponowaniu))
    wiersz_po_transponowaniu.clear()