
with open("CSE110/week11/life-expectancy.csv") as f:
   
    lowest_life_expectancy = float("inf")  
    highest_life_expectancy = float("-inf")  
    for line in f:
        num = line.strip().split(",") 

        try:
            life_expectancy = float(num[3])  
            
            if life_expectancy < lowest_life_expectancy:
                lowest_life_expectancy = life_expectancy
            
            if life_expectancy > highest_life_expectancy:
                highest_life_expectancy = life_expectancy
                
        except ValueError:
            continue


print(f"Lowest Life Expectancy: {lowest_life_expectancy}")
print(f"Highest Life Expectancy: {highest_life_expectancy}")
