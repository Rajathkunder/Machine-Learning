def remove_extremes(values, n):
    
    
   
    if len(values) < 2 * n:
        raise ValueError(f"List must contain at least {2*n} elements.")
    
    sorted_values = sorted(values)
    return sorted_values[n:-n]

def main():
    
    try:
        values = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    except ValueError:
        print("Invalid input. Please enter a list of integers.")
        return
    
    
    if len(values) < 4:
        print("Error: Please enter at least 4 values.")
        return
    
    
    n = 2
    
    
    try:
        filtered_values = remove_extremes(values, n)
        print(f"List with the {n} largest and {n} smallest values removed: {filtered_values}")
        print(f"Original list: {values}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
