
import pandas as pd

class_data = {
    "first_name": ["Fahad", "Derron", "alex", "Taylor", "roddick", "rana", "noman", "Liz",],
    "last_name": ["Alrashidi", "Hall", "Unsworth", "Dawson", "Mujib", "liaqut", "Ali", "smite" ],
    "age": [16,16,16,16,17,16,17,16]
}

display = pd.DataFrame(class_data)
print(display)


print()
print()


movie_data = {
    "name": ["oma", "derron", "fahad"],
    "movie": ["scott pilgrim", "your name", "good fellows"],
    "lead_actor": ["Michael Cera", "Ryunosuke Kamiki", "Robert De Niro"],
    "release_date": ["2010", "2016", "1990"]
}

display = pd.DataFrame(movie_data)
print(display)