import csv

overall_min = float("inf")
overall_max = float("-inf")
overall_min_country = ""
overall_max_country = ""
overall_min_year = ""
overall_max_year = ""

data = []


with open("CSE110/week11/life-expectancy.csv") as f:
    reader = csv.reader(f)
    next(reader)  

    for row in reader:
        if len(row) < 4:
            continue 

        try:
            country = row[0]
            year = int(row[2])
            life_expectancy = float(row[3])
            
            data.append((country, year, life_expectancy))
            
            
            if life_expectancy < overall_min:
                overall_min = life_expectancy
                overall_min_country = country
                overall_min_year = year
            
            if life_expectancy > overall_max:
                overall_max = life_expectancy
                overall_max_country = country
                overall_max_year = year
        
        except ValueError:
            continue 


year_of_interest = int(input("Enter the year of interest: "))

year_life_expectancies = [entry for entry in data if entry[1] == year_of_interest]

if year_life_expectancies:
    avg_life_expectancy = sum(entry[2] for entry in year_life_expectancies) / len(year_life_expectancies)
    min_country, _, min_life = min(year_life_expectancies, key=lambda x: x[2])
    max_country, _, max_life = max(year_life_expectancies, key=lambda x: x[2])

    print(f"\nThe overall max life expectancy is: {overall_max:.2f} from {overall_max_country} in {overall_max_year}")
    print(f"The overall min life expectancy is: {overall_min:.2f} from {overall_min_country} in {overall_min_year}")
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg_life_expectancy:.2f}")
    print(f"The max life expectancy was in {max_country} with {max_life:.2f}")
    print(f"The min life expectancy was in {min_country} with {min_life:.2f}")
else:
    print(f"No data available for the year {year_of_interest}.")


country_of_interest = input("\nEnter the country of interest: ").strip()

country_life_expectancies = [entry[2] for entry in data if entry[0].lower() == country_of_interest.lower()]

if country_life_expectancies:
    min_life = min(country_life_expectancies)
    max_life = max(country_life_expectancies)
    avg_life = sum(country_life_expectancies) / len(country_life_expectancies)

    print(f"\nFor {country_of_interest}:")
    print(f"The average life expectancy was {avg_life:.2f}")
    print(f"The max life expectancy was {max_life:.2f}")
    print(f"The min life expectancy was {min_life:.2f}")
else:
    print(f"No data available for {country_of_interest}.")

