#!/usr/bin/env python3

class Dog:
    def __init__(self, dog_name, dog_breed = "Mutt"):
        self.name = dog_name
        self.breed = dog_breed

rufus = Dog("Rufus", "Bobel")
name = rufus.name
breed = rufus.breed
print(f"{name} is a {breed} breed.")