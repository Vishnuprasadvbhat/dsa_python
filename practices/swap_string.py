def minimize_difference(S, T):
    # Convert strings to lists of integers
    S_list = list(map(int, S))
    T_list = list(map(int, T))

    print(S_list)
    print(T_list)

    # Calculate the initial difference
    initial_diff = abs(sum(S_list) - sum(T_list))
    print(initial_diff)
    n = len(S_list)
    swaps = 0
    
    # Try to minimize the difference by swapping
    for i in range(n):
        for j in range(n):
            
            # Calculate the potential new sums after swap
            new_S_sum = sum(S_list) - S_list[i] + T_list[i]
            new_T_sum = sum(T_list) - T_list[j] + S_list[j]
            
            # Calculate new difference
            new_diff = abs(new_S_sum - new_T_sum)
            
            # If swapping reduces the difference, perform the swap
            if new_diff < initial_diff:
                # Perform the swap
                S_list[i], T_list[i] = T_list[i], S_list[i]
                swaps += 1
                initial_diff = new_diff  # Update the difference
    

    return swaps

# Example Usage
S = "123"
T = "456"
print(minimize_difference(S, T))
