import unittest
import io
import sys
from recommendation_engine import get_personalized_recommendations, display_recommendations

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        # Data film untuk pengujian
        self.test_movies = [
            {"title": "Film Action 1", "genre": "Action", "rating": 8.5, "year": 2020},
            {"title": "Film Comedy 1", "genre": "Comedy", "rating": 7.0, "year": 2019},
            {"title": "Film Drama 1", "genre": "Drama", "rating": 9.0, "year": 2021},
            {"title": "Film Action 2", "genre": "Action", "rating": 6.5, "year": 2018},
            {"title": "Film Comedy 2", "genre": "Comedy", "rating": 8.0, "year": 2022}
        ]
        
        # Preferensi pengguna untuk pengujian
        self.test_preferences = {
            "favorite_genres": ["Action", "Comedy"],
            "min_rating": 7.0
        }
    
    def test_get_personalized_recommendations(self):
        # Menguji fungsi rekomendasi personal
        recommendations = get_personalized_recommendations(self.test_movies, self.test_preferences)
        
        # Verifikasi bahwa rekomendasi adalah list
        self.assertIsInstance(recommendations, list)
        
        # Verifikasi bahwa rekomendasi tidak kosong
        self.assertTrue(len(recommendations) > 0)
        
        # Verifikasi bahwa setiap rekomendasi memiliki film dan skor
        for rec in recommendations:
            self.assertIn("movie", rec)
            self.assertIn("score", rec)
            
        # Verifikasi bahwa film dengan rating < min_rating tidak direkomendasikan
        for rec in recommendations:
            self.assertGreaterEqual(rec["movie"]["rating"], self.test_preferences["min_rating"])
            
        # Verifikasi bahwa film dengan genre favorit mendapat skor lebih tinggi
        action_scores = [rec["score"] for rec in recommendations if "Action" in rec["movie"]["genre"]]
        drama_scores = [rec["score"] for rec in recommendations if "Drama" in rec["movie"]["genre"]]
        
        if action_scores and drama_scores:
            self.assertGreater(max(action_scores), max(drama_scores))
    
    def test_display_recommendations(self):
        # Membuat rekomendasi untuk pengujian
        test_recommendations = [
            {
                "movie": {"title": "Film Test 1", "genre": "Action", "rating": 8.5, "year": 2020},
                "score": 9.5
            },
            {
                "movie": {"title": "Film Test 2", "genre": "Comedy", "rating": 7.0, "year": 2019},
                "score": 8.0
            }
        ]
        
        # Menangkap output ke stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            display_recommendations(test_recommendations)
            output = captured_output.getvalue()
            
            # Verifikasi bahwa output berisi judul film
            self.assertIn("Film Test 1", output)
            self.assertIn("Film Test 2", output)
            
            # Verifikasi bahwa output berisi genre
            self.assertIn("Action", output)
            self.assertIn("Comedy", output)
            
            # Verifikasi bahwa output berisi skor rekomendasi
            self.assertIn("9.5", output)
            self.assertIn("8.0", output)
        finally:
            # Kembalikan stdout
            sys.stdout = sys.__stdout__
        
        # Menguji kasus rekomendasi kosong
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            display_recommendations([])
            output = captured_output.getvalue()
            
            # Verifikasi pesan tidak ada rekomendasi
            self.assertIn("Tidak ada rekomendasi yang tersedia", output)
        finally:
            # Kembalikan stdout
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()