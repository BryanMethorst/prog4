# lingo.py
import random

class Lingo:
    def __init__(self):
        """Initialiseer de Lingo-klasse met een willekeurig gekozen woord."""
        woordenlijst = ["plaat", "stoel", "water", "boord", "vloer"]
        self.woord = random.choice(woordenlijst)

    def validate_input(self, ingevoerd_woord):
        """
        Controleer of de letters in het ingevoerde woord overeenkomen met het te raden woord.

        :param ingevoerd_woord: Het woord dat de gebruiker invoert.
        :return: Een string met gekleurde vierkantjes voor elke letter.
        """
        if len(ingevoerd_woord) != len(self.woord):
            raise ValueError(f"Het ingevoerde woord moet {len(self.woord)} letters bevatten.")

        resultaat = []
        overgebleven_letters = {}  # Houd het aantal overgebleven letters bij

        # Bereken het aantal keer dat elke letter in het woord voorkomt
        for letter in self.woord:
            overgebleven_letters[letter] = overgebleven_letters.get(letter, 0) + 1

        # Controleer eerst op correcte posities (groen)
        for i, letter in enumerate(ingevoerd_woord):
            if letter == self.woord[i]:
                resultaat.append("🟩")
                overgebleven_letters[letter] -= 1  # Verlaag de teller voor deze letter
            else:
                resultaat.append(None)  # Plaats een tijdelijke waarde voor latere verwerking

        # Controleer op letters op verkeerde plaatsen (geel)
        for i, letter in enumerate(ingevoerd_woord):
            if resultaat[i] is None:  # Alleen letters die niet groen zijn
                if letter in overgebleven_letters and overgebleven_letters[letter] > 0:
                    resultaat[i] = "🟨"
                    overgebleven_letters[letter] -= 1  # Verlaag de teller voor deze letter
                else:
                    resultaat[i] = "⬜"  # Wit vierkantje

        # Vul ontbrekende wit vierkantjes in (indien nodig)
        resultaat = [vakje if vakje is not None else "⬜" for vakje in resultaat]

        return "".join(resultaat)
