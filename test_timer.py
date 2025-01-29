import time
import unittest
from timer import Timer

class TestTimer(unittest.TestCase):
    def test_start_timer(self):
        timer = Timer()
        timer.start()
        self.assertIsNotNone(timer.start_time)

    def test_elapsed_time(self):
        timer = Timer()
        timer.start()
        time.sleep(1)
        elapsed = timer.elapsed_time()
        self.assertGreaterEqual(elapsed, 1)

    def test_stop_timer(self):
        timer = Timer()
        timer.start()
        time.sleep(2)
        elapsed = timer.stop()
        self.assertGreaterEqual(elapsed, 2)
    
    def test_stop_without_start(self):
        timer = Timer()
        with self.assertRaises(ValueError):
            timer.stop()

if __name__ == '__main__':
    unittest.main()
