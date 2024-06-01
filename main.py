import pandas as pd
import numpy as np


# Function to generate a random name
def generate_random_name():
    vowels = list("QWRTPSDFGHJKLZXCVBNM")
    consonants = list("EYUIOA")

    # Random name length (5 or 6 characters)
    name_length = np.random.choice([5, 6])

    # Random first letter
    first_letter = np.random.choice(consonants + vowels)

    # Generating subsequent letters
    name_parts = [first_letter]
    for x in range(1, name_length):
        if name_parts[-1] in consonants:
            next_letter = np.random.choice(vowels)
            name_parts.append(next_letter)
        else:
            next_letter = np.random.choice(consonants)
            name_parts.append(next_letter)

    # Converting list of letters to string
    joined_name = ''.join(name_parts)

    # Converting all letters except the first one to lowercase
    lowercased_letters = joined_name[1:].lower()

    # Combining the first letter and the rest of the letters in lowercase
    final_name = name_parts[0] + lowercased_letters
    return final_name


# Function to generate a random country
def random_country():
    countries = ["USA", "Canada", "Ukraine", "German", "Poland", "Norway", "France"]
    random_country = np.random.choice(countries)
    return random_country


# Generating random ages (from 20 to 60 years) and salaries (from $30,000 to $150,000)
ages = np.random.randint(20, 60, size=100)
salaries = np.round(np.random.uniform(30000, 150000, size=100), 2)

# Generating random names and countries for 100 people
names = (generate_random_name() for _ in range(100))
countries = (random_country() for _ in range(100))

# Creating a DataFrame with names, countries, ages, and salaries
df = pd.DataFrame({"Name": names, "Countries": countries})

# Adding columns with ages and salaries to the DataFrame
df['Age'] = ages
df['Salaries'] = salaries

# Saving the DataFrame to a CSV file without indexes
df.to_csv("people_data.csv", index=False)

