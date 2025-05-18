justice_league= ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print(len(justice_league))
justice_league.extend(["Batgirl","Nightwing"])
print(justice_league)
justice_league.remove("Wonder Woman")
justice_league.insert(0,"Wonder Woman")
print(justice_league)
justice_league.remove("Green Lantern")
justice_league.insert(4,"Green Lantern")
print(justice_league)
justice_league=["Cyborg","Shazam", "Hawkgirl","Martian","Manhunter","Green Arrow"]
print(justice_league)
justice_league.sort()
print(justice_league)
print(f"The leader is {justice_league[0]}")


