# test_lingo.py
from lingo import Lingo

if __name__ == "__main__":
    # Maak een instantie van de Lingo-klasse
    spel = Lingo()

    print("Welkom bij Lingo!")
    while True:
        # Vraag de gebruiker om input
        ingevoerd_woord = input("Voer een woord in van 5 letters (of 'stop' om te stoppen): ")

        if ingevoerd_woord.lower() == "stop":
            print("Bedankt voor het spelen!")
            break

        try:
            # Roep validate_input aan en toon het resultaat
            resultaat = spel.validate_input(ingevoerd_woord)
            print("Resultaat per letter:")
            print(resultaat)

            # Controleer of het woord correct geraden is
            if ingevoerd_woord == spel.woord:
                print("Gefeliciteerd! Je hebt het woord geraden.")
                break
        except ValueError as e:
            print("Fout:", e)
            resultaat.append("⬜")