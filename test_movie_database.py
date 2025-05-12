import unittest
import io
import sys
from movie_database import generate_movie_data, display_movies, sort_movies_by_rating

class TestMovieDatabase(unittest.TestCase):
    def setUp(self):
        # Data film untuk pengujian
        self.test_movies = [
            {"title": "Film Test 1", "genre": "Action", "rating": 8.5, "year": 2020},
            {"title": "Film Test 2", "genre": "Comedy", "rating": 7.0, "year": 2019},
            {"title": "Film Test 3", "genre": "Drama", "rating": 9.0, "year": 2021}
        ]
    
    def test_generate_movie_data(self):
        # Memastikan generate_movie_data mengembalikan list
        movies = generate_movie_data()
        self.assertIsInstance(movies, list)
        # Memastikan setiap film memiliki atribut yang diperlukan
        for movie in movies:
            self.assertIn("title", movie)
            self.assertIn("genre", movie)
            self.assertIn("rating", movie)
            self.assertIn("year", movie)
    
    def test_display_movies(self):
        # Menangkap output ke stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            display_movies(self.test_movies)
            output = captured_output.getvalue()
            
            # Verifikasi bahwa output berisi judul film
            self.assertIn("Film Test 1", output)
            self.assertIn("Film Test 2", output)
            self.assertIn("Film Test 3", output)
            
            # Verifikasi bahwa output berisi genre
            self.assertIn("Action", output)
            self.assertIn("Comedy", output)
            self.assertIn("Drama", output)
        finally:
            # Kembalikan stdout
            sys.stdout = sys.__stdout__
    
    def test_sort_movies_by_rating(self):
        # Menguji pengurutan film berdasarkan rating
        sorted_movies = sort_movies_by_rating(self.test_movies.copy())
        
        # Verifikasi urutan
        self.assertEqual(sorted_movies[0]["title"], "Film Test 3")  # Rating tertinggi (9.0)
        self.assertEqual(sorted_movies[1]["title"], "Film Test 1")  # Rating kedua (8.5)
        self.assertEqual(sorted_movies[2]["title"], "Film Test 2")  # Rating terendah (7.0)

if __name__ == '__main__':
    unittest.main()