def generate_floyds_triangle(n):
    if not (1 <= n <= 100):
        raise ValueError("n must be between 1 and 100")
    
    result = []
    current_num = 1
    
    for row in range(1, n + 1):
        # Create a row of numbers from current_num
        row_numbers = [str(current_num + i) for i in range(row)]
        result.append(" ".join(row_numbers))
        current_num += row  # Move to the next starting number
    
    return result
