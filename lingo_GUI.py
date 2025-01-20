import tkinter as tk
from tkinter import messagebox
from lingo import Lingo  # Importeer de Lingo-klasse

class LingoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lingo Game")
        
        # De grootte van het venster instellen en het centreren
        window_width = 400
        window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Bereken de x en y posities om het venster te centreren
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        
        # Zet de geometrie van het venster
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        
        # Maak een instantie van de Lingo-klasse
        self.spel = Lingo()

        # Maak labels voor titel en uitleg
        self.title_label = tk.Label(self.root, text="Welkom bij Lingo!", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, columnspan=5, pady=10, sticky="nsew")  # Tekst centreren bovenaan

        self.info_label = tk.Label(self.root, text="Raad het 5-letter woord. Voer een woord in en druk op Enter.", font=("Arial", 12))
        self.info_label.grid(row=1, column=0, columnspan=5, pady=5, sticky="nsew")

        # Voeg een label toe voor de status
        self.status_label = tk.Label(self.root, text="Status: ", font=("Arial", 14))
        self.status_label.grid(row=2, column=0, columnspan=5, pady=10, sticky="nsew")

        # Maak een invoerveld voor het hele woord
        self.word_entry = tk.Entry(self.root, font=("Arial", 18), width=15, justify='center')
        self.word_entry.grid(row=3, column=0, columnspan=5, pady=10, sticky="nsew")
        self.word_entry.bind("<Return>", self.validate_input)

        # Maak een lijst van labels voor de resultaat van elke poging
        self.attempts_labels = []

    def validate_input(self, event):
        """Valideer de invoer als de gebruiker op Enter drukt."""
        ingevoerd_woord = self.word_entry.get().lower().strip()
        if len(ingevoerd_woord) != 5:
            messagebox.showerror("Fout", "Voer een woord van 5 letters in.")
            return

        # Zet het invoerveld op alleen-lezen (disabled)
        self.word_entry.config(state="disabled")

        # Roep validate_input van de Lingo-klasse aan
        try:
            resultaat = self.spel.validate_input(ingevoerd_woord)
            self.show_attempt_result(ingevoerd_woord, resultaat)

            # Controleer of het woord correct geraden is
            if ingevoerd_woord == self.spel.woord:
                self.show_win_message()

            # Maak een nieuwe invoer mogelijk voor de volgende gok
            self.reset_input()

        except ValueError as e:
            messagebox.showerror("Fout", str(e))

    def show_attempt_result(self, ingevoerd_woord, resultaat):
        """Toon het resultaat van de poging en kleur de vakjes."""
        kleur_map = {"🟩": "green", "🟨": "yellow", "⬛": "red"}

        # Maak een nieuwe rij voor de huidige poging
        row_labels = []
        for i, letter in enumerate(ingevoerd_woord):
            color = kleur_map.get(resultaat[i], "red")  # Standaard rood voor foute letters
            label = tk.Label(self.root, text=letter.upper(), font=("Arial", 14), width=3, height=2, relief="solid", anchor="center", bg=color)
            label.grid(row=len(self.attempts_labels) + 4, column=i, padx=5, pady=5)
            row_labels.append(label)

        # Voeg de nieuwe rij toe aan de lijst van pogingen
        self.attempts_labels.append(row_labels)

    def show_win_message(self):
        """Toon een win-bericht wanneer het juiste woord is geraden."""
        messagebox.showinfo("Gefeliciteerd!", "Je hebt het woord geraden!")
        self.root.quit()

    def reset_input(self):
        """Reset het invoerveld voor de volgende poging."""
        self.word_entry.config(state="normal")  # Zet het invoerveld weer bewerkbaar
        self.word_entry.delete(0, tk.END)  # Verwijder de tekst in het invoerveld

# Start de applicatie
if __name__ == "__main__":
    root = tk.Tk()
    gui = LingoGUI(root)
    root.mainloop()
