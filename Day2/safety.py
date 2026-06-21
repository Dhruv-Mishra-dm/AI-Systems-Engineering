# Functions

def calculate_metrics(followers, following):
    ratio = followers/following
    return ratio

linus_ratio = calculate_metrics(200000, 5)
print(f"Linus Follower Ratio: {linus_ratio}")

# Error Handling 
def safe_divide(a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Defaulting to 0.")
        return 0
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return None 
    
print(safe_divide(10, 2))
print(safe_divide(10, 0))