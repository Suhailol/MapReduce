import fileinput

highest_death = 0
deathPlace = None

for line in fileinput.input():
    data = line.strip()
    data = data.split()

    if len(data)!=2:
        continue


    # print(data)

    name, noOfDeaths = data
    noOfDeaths = int(noOfDeaths)

    if noOfDeaths > highest_death:
        highest_death = noOfDeaths
        deathPlace = name

print(deathPlace, "\t", highest_death)

# import fileinput

# # transactionCount = 0
# highest_deaths = 0
# deathPlace = None
# # previousValue = 0

# for line in fileinput.input():
#     data = line.strip()
#     data = line.split()

#     # print(data)
#     if len(data)!=2:
#         continue

#     key, value = data
#     value = float(value)
#     # print(data)
#     # highest_deaths = max(highest_deaths, value)
#     if value > highest_deaths:
#         highest_deaths = value
#         deathPlace = key
#     # if data[1] == "42072":
#     #     deathPlace = data[0]
#     transactionCount +=1
#     # previousValue = value

# print(deathPlace,"\t", highest_deaths)

