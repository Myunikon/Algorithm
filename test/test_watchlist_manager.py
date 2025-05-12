import unittest
import io
import sys
from watchlist_manager import display_watchlist, add_to_watchlist, remove_from_watchlist

class TestWatchlistManager(unittest.TestCase):
    def setUp(self):
        # Data film untuk pengujian
        self.test_movies = [
            {"title": "Film Test 1", "genre": "Action", "rating": 8.5, "year": 2020},
            {"title": "Film Test 2", "genre": "Comedy", "rating": 7.0, "year": 2019}
        ]
        
        # Watchlist untuk pengujian
        self.test_watchlist = ["Film Test 1"]
    
    def test_display_watchlist(self):
        # Menangkap output ke stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            display_watchlist(self.test_watchlist)
            output = captured_output.getvalue()
            
            # Verifikasi bahwa output berisi film dalam watchlist
            self.assertIn("Film Test 1", output)
        finally:
            # Kembalikan stdout
            sys.stdout = sys.__stdout__
        
        # Menguji kasus watchlist kosong
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            display_watchlist([])
            output = captured_output.getvalue()
            
            # Verifikasi pesan watchlist kosong
            self.assertIn("Watchlist Anda kosong", output)
        finally:
            # Kembalikan stdout
            sys.stdout = sys.__stdout__
    
    def test_add_to_watchlist(self):
        # Menyiapkan input pengguna
        sys.stdin = io.StringIO("Film Test 2\n")
        
        # Menangkap output ke stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            # Membuat salinan watchlist
            watchlist_copy = self.test_watchlist.copy()
            add_to_watchlist(self.test_movies, watchlist_copy)
            
            # Verifikasi bahwa film ditambahkan ke watchlist
            self.assertIn("Film Test 2", watchlist_copy)
            self.assertEqual(len(watchlist_copy), 2)
            
            # Verifikasi pesan sukses
            output = captured_output.getvalue()
            self.assertIn("berhasil ditambahkan ke watchlist", output)
        finally:
            # Kembalikan stdin dan stdout
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
    
    def test_remove_from_watchlist(self):
        # Menyiapkan input pengguna
        sys.stdin = io.StringIO("1\n")
        
        # Menangkap output ke stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            # Membuat salinan watchlist
            watchlist_copy = self.test_watchlist.copy()
            remove_from_watchlist(watchlist_copy)
            
            # Verifikasi bahwa film dihapus dari watchlist
            self.assertNotIn("Film Test 1", watchlist_copy)
            self.assertEqual(len(watchlist_copy), 0)
            
            # Verifikasi pesan sukses
            output = captured_output.getvalue()
            self.assertIn("berhasil dihapus dari watchlist", output)
        finally:
            # Kembalikan stdin dan stdout
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
