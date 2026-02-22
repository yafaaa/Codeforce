def fun():
    n = int(input())
    string = input()
    block = 1
    con = False
    
    for i in range(1,n):
        if string[i] != string[i-1]:
            block += 1
            continue
        con = True
    if string[0] == string[-1]:
        
        return(block)
    
    if con: 
        return(block+1)
    
    return(block)

if __name__ == "__main__":
    for _ in range(int(input())):
        print(fun())
        

