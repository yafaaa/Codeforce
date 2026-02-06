import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    s = list(input_data[2])
    
    # Create the mapping: index 0 is 'a', 1 is 'b'...
    # map_to[i] is what the character (chr(97+i)) currently looks like
    map_to = [chr(97 + i) for i in range(26)]
    
    # Track the reverse: which original char currently maps to 'x'?
    # pos[i] tells us which index in map_to contains character chr(97+i)
    pos = [i for i in range(26)]
    
    # Process each swap
    idx = 3
    for _ in range(m):
        x = input_data[idx]
        y = input_data[idx+1]
        idx += 2
        
        if x == y:
            continue
            
        # Get the original indices that currently point to x and y
        idx_x = pos[ord(x) - 97]
        idx_y = pos[ord(y) - 97]
        
        # Swap the destinations in the map
        map_to[idx_x], map_to[idx_y] = map_to[idx_y], map_to[idx_x]
        
        # Update the positions so we can find them quickly next time
        pos[ord(x) - 97], pos[ord(y) - 97] = idx_y, idx_x

    # Final Translation
    # We need a map of OriginalChar -> FinalChar
    # map_to already is: index i (original char) -> final char
    final_map = {chr(97 + i): map_to[i] for i in range(26)}
    
    print("".join(final_map[c] for c in s))

solve()