from DiamondTrap import King


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

print(Joffrey.__str__)
Tyrion = Joffrey.create_lannister("Tyrion")
print(Tyrion.__dict__)
print(Joffrey.__str__)
