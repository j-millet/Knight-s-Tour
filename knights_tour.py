import time
import random

def shuffle(arr):  #przemieszaj tablice
    for x in range(len(arr)):
        idx = random.randint(0,len(arr)-1)
        arr[x],arr[idx] = arr[idx], arr[x]
    return arr

moveset = [(-2,1),(-2,-1),(-1,2),(-1,-2),(2,1),(2,-1),(1,2),(1,-2)] #tablica dostępnych ruchów
size = 8    #rozmiar planszy
start = (0,7)   #pozycja startowa

b = [[None for x in range(size)] for x in range(size)] #plansza


t = time.time()

time_tolerance = size**2  #maksymalny czas szukania rozwiązania

def move(board,pos,n,mov):
    global size, t,time_tolerance

    if time.time()-t > time_tolerance: return None  #jeżeli przekroczono czas zakończ
    print(f"\rn: {(n)} ",end="")

    x,y = pos
    if board[y][x] != None: #jeżeli zajęte zakończ
        return None

    board[y][x] = n

    if n == size**2:    #jeżeli znaleziono podaj statystyki
        print("\n\nFOUND!\n")
        print("board:")
        for row in board: print(row)
        return [pos]

    for m in mov:
        newpos = (x+m[0],y+m[1])
        if not (newpos[0]<0 or newpos[0]>=size or newpos[1]<0 or newpos[1]>=size) and board[newpos[1]][newpos[0]] == None:
            r = move(board,newpos,n+1,mov)
            if r!= None: 
                ret = [pos]
                ret.extend(r)
                return ret

    board[y][x] = None
    return None


print(1)
print(1)
tries = 0
ret = None
while ret == None: #szukaj do skutku
    tries+=1
    t = time.time()
    ms = shuffle(moveset) #przemieszaj liste kroków (z inną kolejnością ruchów może znaleźć szybciej)
    print(f"\033A[\033A[\rMoveset: {ms}")
    print(f"\rRestarts: {tries}")
    ret = move(b,start,1,ms)

print(f"Execution time: {(tries-1)*time_tolerance+round(time.time()-t,2)}s")
print(f"Moves: {ret}")
