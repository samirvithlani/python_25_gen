teams = {"INDIA":["ms","virat","rohit","hardik","rahul"],"AUS":["head","pet","starc","josh","ponting"]}
print(teams)

for i,j in teams.items():
    print(i,end=" ")
    #print(j)
    for player in j:
        print(player,end=",")
    print()    