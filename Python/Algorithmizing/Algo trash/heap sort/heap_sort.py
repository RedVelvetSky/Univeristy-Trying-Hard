halda = [] 
N = int(input()) 
 
for i in range(N): 
    cislo = int(input()) 
    halda.append(cislo) 
 
def halduj(halda,delka,i): 
    max = i 
    levy = 2 * i + 1 
    pravy = 2 * i + 2 
   
    if levy < delka and halda[i] < halda[levy]: 
        max = levy 
   
    if pravy < delka and halda[max] < halda[pravy]: 
        max = pravy 
   
    if max != i: 
        halda[i], halda[max] = halda[max], halda[i] 
        halduj(halda, delka, max) 
 
 
def heapSort(halda): 
    delka = len(halda) 
    for i in range(delka//2, -1, -1): 
        halduj(halda, delka, i) 
 
    for i in range(delka): 
        print(str(halda[i])+" ", end='') 
    print() 
 
    for i in range(delka-1, 0, -1): 
        halda[i], halda[0] = halda[0], halda[i] 
 
        halduj(halda, i, 0) 
        for i in range(delka): 
            print(str(halda[i])+" ", end='') 
        print() 
   
heapSort(halda)