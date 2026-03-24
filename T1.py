actors_mcu = {
    "Robert Downey Jr.",
    "Chris Evans",
    "Chris Hemsworth",
    "Mark Ruffalo",
    "Scarlett Johansson",
    "Jeremy Renner",
    "Tom Hiddleston",
    "Benedict Cumberbatch",
    "Paul Rudd",
    "Brie Larson",
    "Chadwick Boseman"
}

# Actors in DC Extended Universe
actors_dceu = {
    "Henry Cavill",
    "Ben Affleck",
    "Gal Gadot",
    "Jason Momoa",
    "Ezra Miller",
    "Ray Fisher",
    "Margot Robbie",
    "Will Smith",
    "Jared Leto",
    "Zachary Levi"
}

# Actors who have done superhero movies in general (including non-MCU/DCEU)
actors_superhero = {
    "Robert Downey Jr.",
    "Chris Evans",
    "Christian Bale",  # Batman (Dark Knight Trilogy)
    "Tobey Maguire",  # Spider-Man
    "Andrew Garfield",  # Spider-Man
    "Hugh Jackman",  # X-Men
    "Patrick Stewart",  # X-Men
    "Ian McKellen",  # X-Men
    "Ryan Reynolds",  # Deadpool
    "Michael Keaton",  # Batman
    "Ben Affleck",
    "Gal Gadot"
}

print("\n🦸 Actors in Marvel Cinematic Universe:")
print(actors_mcu)

print("\n🦇 Actors in DC Extended Universe:")
print(actors_dceu)

print("\n🎭 Actors in superhero movies (any franchise):")
print(actors_superhero)

print("\n❓ Are there any actors in BOTH MCU and DCEU?")
print(actors_mcu & actors_dceu)

print("\n❓ Actors in superhero movies but NOT in MCU?")
print(actors_superhero - actors_mcu)

print("\n❓ Is the DCEU set a subset of any superhero actors?")
print(actors_mcu <= actors_superhero)

print("\n❓ Actors ONLY in MCU (not in other franchises)?")
print(actors_mcu - actors_dceu - actors_superhero)

print("\n❓ Is all_superhero_actors a superset of DCEU?")
print(actors_superhero >= actors_dceu)