class Chien:
    def __init__(self, nom, poids):
        self.nom = nom
        self.poids = poids

    def quantite_nourriture(self):
        return self.poids * 0.03


class Pekinois(Chien):
    def quantite_nourriture(self):
        estimation_base = super().quantite_nourriture()
        return estimation_base * 1.10


class GoldenRetriever(Chien):
    pass


class SaintBernard(Chien):
    def quantite_nourriture(self):
        estimation_base = super().quantite_nourriture()
        return estimation_base * 1.20


# Instanciation et tests
chihuahua = Pekinois("Bella", 2)
print(f"{chihuahua.nom} requiert {chihuahua.quantite_nourriture():.2f}kg de nourriture par jour.")

golden = GoldenRetriever("Buddy", 30)
print(f"{golden.nom} requiert {golden.quantite_nourriture():.2f}kg de nourriture par jour.")

saint_bernard = SaintBernard("Duke", 70)
print(f"{saint_bernard.nom} requiert {saint_bernard.quantite_nourriture():.2f}kg de nourriture par jour.")
