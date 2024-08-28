

import unittest
import cap 

class Testcap(unittest.TestCase):
    def test_oneword(self):
        text = 'python'
        res = cap.cap_text(text)
        self.assertEqual(res,'Python')

    def test(self):
        text = 'month python'
        res = cap.cap_text(text)
        self.assertEqual(res,'Month Python')

if __name__ == "__main__":
    unittest.main()
