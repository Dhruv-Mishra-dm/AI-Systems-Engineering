import csv

# Our mock data (a List of Dictionaries)
users = [{"username": "torvalds", "repos" : 6, "followers": 200000},
         {"username": "Dhruv", "repos": 10, "followers":50}
         ]

# Open a file in "w" (write) mode. "newline=''" prevents blank lines in Windows.
with open("github_stats.csv", mode="w", newline="") as file:
    # We define the column headers based on our dictionary keys
    fieldnames = ["username", "repos", "followers"]
    
    # We set up the CSV writer 
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Loop through our list and write each dictionary as a row 
    for user in users: 
        writer.writerow(user)
        
print("Data succesfully saved to github_stats.csv!")