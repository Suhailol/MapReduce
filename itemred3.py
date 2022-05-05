
# import fileinput

# transactionCount = 0
# monthsSum = 0

# for line in fileinput.input():
#     data = line.strip()
#     data = line.split()

#     # print(data)
#     if len(data)!=2:
#         continue

#     key, value = data
#     value = float(value)
#     transactionCount +=1
#     monthsSum += value

# print(transactionCount,"\t", monthsSum)

# import fileinput

# transactionCount = 0
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


import fileinput

transactionCount = 0
monthsSum = 0
# final = []

for line in fileinput.input():
    data = line.strip()
    data = line.split()

    # print(data)
    if len(data)!=2:
        continue

    key, value = data
    b = key.strip()
    # print(b)
    b = key.split("-")
    # print(b)
    year, month, specific = b
    #print(specific)
    date = specific.split('T')
    print(date)
    day, time = date

    hash = {"01":"January", "02":"February", "03":"March", "04":"April", "05":"May", "06":"June", "07":"July", "08":"August", "09":"September", "10":"October", "11":"November", "12":"December",  }
    # if month == "01":
    final = [year, hash["01"], day, time]
    
    print(final)

    value = float(value)
    transactionCount +=1
    monthsSum += value

print(transactionCount,"\t", monthsSum)