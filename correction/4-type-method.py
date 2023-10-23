class Restaurant:
    total_repas_vendus = 0

    def __init__(self, nom, ville):
        self.nom = nom
        self.ville = ville
        self.repas_vendus = 0

    def vendre_repas(self, nombre):
        self.repas_vendus += nombre
        Restaurant.total_repas_vendus += nombre

    def statistiques_restaurant(self):
        return f"Restaurant {self.nom} à {self.ville} a vendu {self.repas_vendus} repas."

    @classmethod
    def statistiques_chaine(cls):
        return f"La chaîne de restaurants a vendu {cls.total_repas_vendus} repas au total."

    @staticmethod
    def evaluer_repas(note):
        evaluations = {
            1: "Mauvais",
            2: "Moyen",
            3: "Bon",
            4: "Très bon",
            5: "Excellent"
        }
        return evaluations.get(note, "Note invalide")


# Instances de restaurant
restaurant1 = Restaurant("Le Gourmet", "Paris")
restaurant2 = Restaurant("Pasta Delight", "Rome")
restaurant3 = Restaurant("Burger Queen", "New York")

# Ventes de repas
restaurant1.vendre_repas(50)
restaurant2.vendre_repas(30)
restaurant3.vendre_repas(60)

# Afficher les statistiques
print(restaurant1.statistiques_restaurant())
print(restaurant2.statistiques_restaurant())
print(restaurant3.statistiques_restaurant())
print(Restaurant.statistiques_chaine())

# Évaluation d'un repas
print(Restaurant.evaluer_repas(4))
