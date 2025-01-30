#Brute force method
def cat_hat(str):
    cat_count = 0
    hat_count = 0
    
    for i in range(len(str) - 2):
        if str[i:i+3] == "cat":
            cat_count += 1
        if str[i:i+3] == "hat":
            hat_count += 1
    
    return cat_count == hat_count
    
print(cat_hat("catcat"))
print(cat_hat("cathat"))
print(cat_hat("cathathat"))
print(cat_hat("cathathathat"))


#Count method
def cat_hat(str):
    cat_count = str.count("cat")
    hat_count = str.count("hat")
    return cat_count == hat_count

# Example usage
print(cat_hat("catinahat"))  # Output: True
print(cat_hat("bazingaa"))   # Output: True
print(cat_hat("catcat"))     # Output: False
print(cat_hat("hathat"))     # Output: False