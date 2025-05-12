import unittest
import io
import sys
from search_engine import search_by_title, search_by_genre, search_by_rating, search_by_year

class TestSearchEngine(unittest.TestCase):
    def setUp(self):
        # Data film untuk pengujian
        self.test_movies = [
            {"title": "Film Action 2020", "genre": "Action", "rating": 8.5, "year": 2020},
            {"title": "Film Comedy 2019", "genre": "Comedy", "rating": 7.0, "year": 2019},
            {"title": "Film Drama 2020", "genre": "Drama", "rating": 9.0, "year": 2020}
        ]
    
    def test_search_by_title(self):
        # Menyiapkan input pengguna
        sys.stdin = io.StringIO("Action\n")
        
        # Menangkap output ke stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            search_by_title(self.test_movies)
            output = captured_output.getvalue()
            
            # Verifikasi bahwa output berisi film yang sesuai
            self.assertIn("Film Action 2020", output)
            self.assertNotIn("Film Comedy 2019", output)
        finally:
            # Kembalikan stdin dan stdout
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
    
    def test_search_by_genre(self):
        # Menyiapkan input pengguna
        sys.stdin = io.StringIO("Comedy\n")
        
        # Menangkap output ke stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            search_by_genre(self.test_movies)
            output = captured_output.getvalue()
            
            # Verifikasi bahwa output berisi film yang sesuai
            self.assertIn("Film Comedy 2019", output)
            self.assertNotIn("Film Action 2020", output)
        finally:
            # Kembalikan stdin dan stdout
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
    
    def test_search_by_rating(self):
        # Menyiapkan input pengguna
        sys.stdin = io.StringIO("8.0\n10.0\n")
        
        # Menangkap output ke stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            search_by_rating(self.test_movies)
            output = captured_output.getvalue()
            
            # Verifikasi bahwa output berisi film yang sesuai
            self.assertIn("Film Action 2020", output)  # Rating 8.5
            self.assertIn("Film Drama 2020", output)   # Rating 9.0
            self.assertNotIn("Film Comedy 2019", output)  # Rating 7.0
        finally:
            # Kembalikan stdin dan stdout
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
    
    def test_search_by_year(self):
        # Menyiapkan input pengguna
        sys.stdin = io.StringIO("2020\n")
        
        # Menangkap output ke stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            search_by_year(self.test_movies)
            output = captured_output.getvalue()
            
            # Verifikasi bahwa output berisi film yang sesuai
            self.assertIn("Film Action 2020", output)
            self.assertIn("Film Drama 2020", output)
            self.assertNotIn("Film Comedy 2019", output)
        finally:
            # Kembalikan stdin dan stdout
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()