class Vehicule:
    def __init__(self, nom, immatriculation, capacite_carburant):
        self.nom = nom
        self.immatriculation = immatriculation
        self.capacite_carburant = capacite_carburant

    def distance_possibles(self):
        return 0

    def __str__(self):
        return f"{self.nom} (Immatriculation: {self.immatriculation})"

    def __repr__(self):
        return f"Vehicule('{self.nom}', '{self.immatriculation}', {self.capacite_carburant})"

    def __lt__(self, autre):
        return self.distance_possibles() < autre.distance_possibles()

    def __le__(self, autre):
        return self.distance_possibles() <= autre.distance_possibles()

    def __gt__(self, autre):
        return self.distance_possibles() > autre.distance_possibles()

    def __ge__(self, autre):
        return self.distance_possibles() >= autre.distance_possibles()


class Voiture(Vehicule):
    def __init__(self, nom, immatriculation, capacite_carburant, nombre_places):
        super().__init__(nom, immatriculation, capacite_carburant)
        self.nombre_places = nombre_places

    def distance_possibles(self):
        return self.capacite_carburant * 15

    def __repr__(self):
        return f"Voiture('{self.nom}', '{self.immatriculation}', {self.capacite_carburant}, {self.nombre_places})"


class Camion(Vehicule):
    def __init__(self, nom, immatriculation, capacite_carburant, capacite_cargaison, type_cargaison):
        super().__init__(nom, immatriculation, capacite_carburant)
        self.capacite_cargaison = capacite_cargaison
        self.type_cargaison = type_cargaison

    def distance_possibles(self):
        return self.capacite_carburant * 5

    def __repr__(self):
        return f"Camion('{self.nom}', '{self.immatriculation}', {self.capacite_carburant}, {self.capacite_cargaison}, '{self.type_cargaison}')"


class Moto(Vehicule):
    def __init__(self, nom, immatriculation, capacite_carburant, type_moto):
        super().__init__(nom, immatriculation, capacite_carburant)
        self.type_moto = type_moto

    def distance_possibles(self):
        return self.capacite_carburant * 20

    def __repr__(self):
        return f"Moto('{self.nom}', '{self.immatriculation}', {self.capacite_carburant}, '{self.type_moto}')"


# Test des classes
voiture1 = Voiture("Toyota Corolla", "XYZ-123", 50, 5)
camion1 = Camion("MAN TGS", "ABD-567", 300, 20, "liquide")
moto1 = Moto("Harley Davidson", "JKL-890", 15, "chopper")

print(voiture1)  # Toyota Corolla (Immatriculation: XYZ-123)
print(voiture1.distance_possibles())  # 750

print(camion1)  # MAN TGS (Immatriculation: ABD-567)
print(camion1.distance_possibles())  # 1500

print(moto1)  # Harley Davidson (Immatriculation: JKL-890)
print(moto1.distance_possibles())  # 300

# Comparaison
print(voiture1 < camion1)  # True
print(moto1 > voiture1)   # False
