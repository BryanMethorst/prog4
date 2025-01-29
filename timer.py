import time

class Timer:
    def __init__(self):
        """Initialiseer de timer."""
        self.start_time = None
        self.end_time = None

    def start(self):
        """Start de timer."""
        self.start_time = time.time()
        self.end_time = None  # Reset de eindtijd

    def stop(self):
        """Stop de timer en return de verstreken tijd in seconden."""
        if self.start_time is None:
            raise ValueError("Timer is niet gestart.")
        self.end_time = time.time()
        return self.elapsed_time()

    def elapsed_time(self):
        """Geef de verstreken tijd in seconden terug."""
        if self.start_time is None:
            return 0
        if self.end_time is None:
            return round(time.time() - self.start_time, 2)
        return round(self.end_time - self.start_time, 2)
