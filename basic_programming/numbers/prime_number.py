def prime_number(n):
    if n <= 1:
        print(f"{n} is not Prime")
        return
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            print(f"{n} is not Prime")
            return
    print(f"{n} is Prime")

# Example usage
prime_number(5)  # Output: 5 is Prime
prime_number(10) # Output: 10 is not Prime
prime_number(13) # Output: 13 is Prime
prime_number(15) # Output: 15 is not Prime