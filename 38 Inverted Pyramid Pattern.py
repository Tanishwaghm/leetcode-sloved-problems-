def generate_inverted_pyramid(n):
    return [(' ' * i) + ('*' * (2 * (n - i) - 1)) + (' ' * i) for i in range(n)]
