import unittest
from fire_risk import get_ttf

def ttf_to_color(ttf):
    """Convert time-to-fire to traffic light color."""
    if ttf < 5:
        return "red"
    elif 5 <= ttf <= 15:
        return "yellow"
    else:
        return "green"

class TestTrafficLight(unittest.TestCase):
    def test_red(self):
        self.assertEqual(ttf_to_color(0), "red")
        self.assertEqual(ttf_to_color(4), "red")

    def test_yellow(self):
        self.assertEqual(ttf_to_color(5), "yellow")
        self.assertEqual(ttf_to_color(15), "yellow")

    def test_green(self):
        self.assertEqual(ttf_to_color(16), "green")
        self.assertEqual(ttf_to_color(30), "green")

if __name__ == "__main__":
    unittest.main()
