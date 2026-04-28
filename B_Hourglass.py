def solve():
    
    t_str = input().strip()
    if not t_str:
        return
    t = int(t_str)
    
    for _ in range(t):
        
        s, k, m = map(int, input().split())
        
        if s <= k:
        
            result = max(0, s - (m % k))
            print(result)
            
        else:
    
            time_in_cycle = m % (2 * k)
            
            if time_in_cycle < k:
                
                print(s - time_in_cycle)
            else:
                
                print(k - (time_in_cycle % k))

if __name__ == "__main__":
    solve()