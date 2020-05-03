#                          0        1          2
favourite_particles = ["photon", "higgs", "positron"]

print(favourite_particles[0])

print(favourite_particles + ["quarks"])     # hier bleibt die liste fav_particles unveraendert

favourite_particles += ["electron"]         # hier veraendert man fav_particles an sich fuer immer (auch wie bei append und extend)

print(favourite_particles)
