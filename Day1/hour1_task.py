
for i in range(101) :
    if i == 0 : 
        print (f"{i} is niether even nor odd") # 0 is even 
        
    elif i % 2 == 0:
        print (f"{i} is a even number")
            
    else :
        print (f"{i} is a odd number")
        

# Given solution from AI

# for i in range(1, 101):  # Starting from 1 excludes the 0 ambiguity entirely
#     if i % 2 == 0:
#         print(f"{i} is an even number")
#     else:
#         print(f"{i} is an odd number")