def solve():
    # Read number of TV sets
    line = input().strip()
    if not line:
        return
    n = int(line)

    intervals = []
    coords_set = set()
    
    # 1. Collect all coordinates
    # We add L, R, and R+1 to ensure we track the "gaps" between TV sets
    for i in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r, i + 1))
        coords_set.add(l)
        coords_set.add(r)
        coords_set.add(r + 1)
    
    # 2. Coordinate Compression
    # Sort unique coordinates and map them to 0, 1, 2...
    sorted_coords = sorted(list(coords_set))
    mapping = {val: i for i, val in enumerate(sorted_coords)}
    m = len(sorted_coords)
    print(coords_set)
    print(sorted_coords)
    print(mapping)
    
    # 3. Difference Array to count coverage
    # diff[i] stores the change in number of TVs at this coordinate
    diff = [0] * (m + 1)
    for l, r, idx in intervals:
        diff[mapping[l]] += 1
        diff[mapping[r] + 1] -= 1
        
    # 4. Calculate actual coverage count at each compressed point
    count = [0] * m
    current_coverage = 0
    for i in range(m):
        current_coverage += diff[i]
        count[i] = current_coverage
        
    # 5. Create a Prefix Sum of "Unique" points
    # unique_pref[i] counts how many points from 0 to i are covered by ONLY 1 TV
    unique_pref = [0] * (m + 1)
    for i in range(m):
        # If count[i] == 1, this point is critical (only one TV covers it)
        is_critical = 1 if count[i] == 1 else 0
        unique_pref[i + 1] = unique_pref[i] + is_critical
        
    # 6. Check each TV set for redundancy
    for l, r, idx in intervals:
        start_idx = mapping[l]
        end_idx = mapping[r]
        
        # Calculate how many "critical" points are in this TV's range
        # Sum = Pref[end + 1] - Pref[start]
        critical_points_count = unique_pref[end_idx + 1] - unique_pref[start_idx]
        
        # If there are 0 critical points, this TV is redundant!
        if critical_points_count == 0:
            print(idx)
            return
            
    print("-1")

if __name__ == "__main__":
    solve()