import unittest
import json
import os
from user_management import load_users, save_users, login_user, user_registration, account_settings, update_preferences

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        # Membuat file users.json sementara untuk pengujian
        self.test_users = {
            "test@example.com": {
                "name": "Test User",
                "phone": "12345678",
                "watchlist": ["Film Test 1", "Film Test 2"],
                "ratings": {"Film Test 1": 8.5},
                "preferences": {
                    "favorite_genres": ["Action", "Comedy"],
                    "min_rating": 7.0
                }
            }
        }
        with open('test_users.json', 'w') as f:
            json.dump(self.test_users, f)
            
    def tearDown(self):
        # Menghapus file test setelah pengujian
        if os.path.exists('test_users.json'):
            os.remove('test_users.json')
    
    def test_load_users(self):
        # Mengganti nama file untuk pengujian
        original_open = open
        def mock_open(*args, **kwargs):
            if args[0] == 'users.json':
                return original_open('test_users.json', *args[1:], **kwargs)
            return original_open(*args, **kwargs)
            
        # Simpan fungsi open asli
        built_in_open = __builtins__['open']
        try:
            # Ganti dengan mock
            __builtins__['open'] = mock_open
            users = load_users()
            # Verifikasi bahwa admin selalu ada
            self.assertIn("admin@movie.com", users)
            # Verifikasi bahwa user test ada
            self.assertIn("test@example.com", users)
            self.assertEqual(users["test@example.com"]["name"], "Test User")
        finally:
            # Kembalikan fungsi open asli
            __builtins__['open'] = built_in_open
    
    def test_save_users(self):
        # Buat salinan users untuk dimodifikasi
        test_users_copy = self.test_users.copy()
        # Tambahkan user baru
        test_users_copy["new@example.com"] = {
            "name": "New User",
            "phone": "87654321",
            "watchlist": [],
            "ratings": {},
            "preferences": {
                "favorite_genres": ["Horror"],
                "min_rating": 6.0
            }
        }
        
        # Simpan ke file test
        original_open = open
        def mock_open(*args, **kwargs):
            if args[0] == 'users.json':
                return original_open('test_users.json', 'w')
            return original_open(*args, **kwargs)
            
        # Simpan fungsi open asli
        built_in_open = __builtins__['open']
        try:
            # Ganti dengan mock
            __builtins__['open'] = mock_open
            save_users(test_users_copy)
            
            # Baca file dan verifikasi
            with original_open('test_users.json', 'r') as f:
                saved_users = json.load(f)
                self.assertIn("new@example.com", saved_users)
                self.assertEqual(saved_users["new@example.com"]["name"], "New User")
        finally:
            # Kembalikan fungsi open asli
            __builtins__['open'] = built_in_open

if __name__ == '__main__':
    unittest.main()