def generate_pyramid(n):
    return [(' ' * (n - i - 1)) + ('*' * (2 * i + 1)) + (' ' * (n - i - 1)) for i in range(n)]
