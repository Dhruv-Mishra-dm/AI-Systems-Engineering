# Lists(Arrays)
# Ordered Collection, O(n) time complexity

tech_stack = ["Python", "C", 'SQL']

# Add to the end 
tech_stack.append("FastAPI")

# Access the first item (Index starts at 0)
print(tech_stack[0])

# Loop through the List
for tech in tech_stack:
    print (f"I am learning {tech}") 
    
    
# Dictionaries (Hash Map)

student_profile = {
    "name": "Candidate",
    "role": "SWE",
    "dsa_solved": 0
}

# update a value
student_profile["dsa_solved"] = 1

# add a new key-value pair 
student_profile["target_company"] = "Google"

# Print the value attached to the 'role' key 
print(student_profile["role"])