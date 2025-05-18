print("roll a die")
c_6=0
c_1=0
c_26=0
pre=0
for j in range(20):
    i=int(input("enter a number"))
    if i==6:
        c_6+=1
    if i==6 and pre==6:
        c_26+=1
    if i==1:
        c_1+=1
    pre=i
print(f"No of times 6 rolled {c_6}")
print(f"No of times 1 rolled {c_1}")
print(f"No of times 6 rolled in a row 2 times {c_26}")
total_jacks = 100
completed = 0

for i in range(0, total_jacks, 10):
    completed += 10
    print(f"Do 10 jumping jacks. Total done: {completed}")
    
    tired = input("Are you tired? (yes/y or no/n): ").lower()
    
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            remaining = total_jacks - completed
            print(f"{remaining} jumping jacks remaining.")
            continue

if completed == total_jacks:
    print("Congratulations! You completed the workout.")


        


       
 

