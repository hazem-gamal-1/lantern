import subprocess
import sys
import unittest


class EmptyListTest(unittest.TestCase):
    def test_message(self):
        result = subprocess.run(
            [sys.executable, "lantern.py", "list"],
            capture_output=True,
            text=True,
        )
        self.assertIn("No tasks yet.", result.stdout)


if __name__ == "__main__":
    unittest.main()