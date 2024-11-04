def is_fibonacci_number(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

num_to_check = int(input('Digite um número para verificar se pertence a sequência de Fibonacci: '))

if is_fibonacci_number(num_to_check):
    print(f'O número {num_to_check} pertence a sequência de Fibonacci!')
else:
    print(f'O número {num_to_check} não pertence a sequência de Fibonacci')