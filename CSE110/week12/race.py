with open("CSE110/week12/race.csv") as f:

    fastest = float("inf")
    for line in f:
        num = line.strip().split(",")
print(f"the fastest runner is {num}")