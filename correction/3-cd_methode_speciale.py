class CD:
    def __init__(self, titre, artiste, chansons):
        self.titre = titre
        self.artiste = artiste
        self.chansons = chansons

    def __repr__(self):
        return f"CD('{self.titre}', '{self.artiste}', {self.chansons})"

    def __str__(self):
        return f"'{self.titre}' par {self.artiste}. Chansons: {', '.join(self.chansons)}."

    def __eq__(self, autre):
        return self.titre == autre.titre and self.artiste == autre.artiste and self.chansons == autre.chansons

    def __add__(self, autre):
        nouveau_titre = self.titre + " & " + autre.titre
        return CD(nouveau_titre, self.artiste, self.chansons + autre.chansons)


# Tests
cd1 = CD("Album A", "Artiste", ["Chanson1", "Chanson2"])
cd2 = CD("Album B", "Artiste", ["Chanson3", "Chanson4"])
double_album = cd1 + cd2

print(cd1)  # Affiche: 'Album A' par Artiste. Chansons: Chanson1, Chanson2.
# Affiche: 'Album A & Album B' par Artiste. Chansons: Chanson1, Chanson2, Chanson3, Chanson4.
print(double_album)
