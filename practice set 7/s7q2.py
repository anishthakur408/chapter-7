# Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
# l = ["anish", "Soham", "Sachin", "Rahul"] 


l = ["anish", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")): # using startwith
      print(f"name is",{name})