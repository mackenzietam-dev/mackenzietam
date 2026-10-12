# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?


# Question 1

def print_stars():
    for star in targets:
        print(star)

# Question 2

def print_spectral_types():
    for star in targets:
        print(star, targets[star]["Spectral Type"])


# Question 3

def find_magnitudes():
    for star in targets:
        if targets[star]["Magnitude"] > 0.1:
            print(star, targets[star]["Magnitude"])


# Question 4

targets["Altair"] = {
    "RA": "19h 50m 47.0s",
    "Dec": "+08° 52′ 06″",
    "Magnitude": 0.76,
    "Spectral Type": "A7V"
}


# Question 5

def find_closest_brightest():
    closest_star = None
    smallest_difference = float("inf")

    for star in targets:
        dec = targets[star]["Dec"]

        degrees = int(dec.split("°")[0].replace("−", "-"))
        difference = abs(degrees - 20)

        if difference < smallest_difference:
            smallest_difference = difference
            closest_star = star

        elif difference == smallest_difference:
            if targets[star]["Magnitude"] < targets[closest_star]["Magnitude"]:
                closest_star = star

    print(closest_star)


# Question 6

print("My favorite constellation is Orion.")

print("Question 1:")
print_stars()

print("\nQuestion 2:")
print_spectral_types()

print("\nQuestion 3:")
find_magnitudes()

print("\nQuestion 4:")
print("Added Altair:", targets["Altair"])

print("\nQuestion 5:")
find_closest_brightest()

print("\nQuestion 6:")
print("Orion")