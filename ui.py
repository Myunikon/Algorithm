import time
from movie_database import display_movies, sort_movies_by_rating, display_top_movies, show_statistics
from user_management import account_settings
from recommendation_engine import show_personal_recommendations
from watchlist_manager import manage_watchlist
from search_engine import search_menu

def typing_effect(text, delay=0.01):
    """
    Menampilkan teks dengan efek mengetik.
    
    Parameters:
    text (str): Teks yang akan ditampilkan
    delay (float): Jeda antar karakter dalam detik
    
    Returns:
    None
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def dynamic_greeting():
    """
    Memberikan salam berdasarkan waktu hari.
    
    Returns:
    str: Salam yang sesuai dengan waktu hari
    """
    current_hour = time.localtime().tm_hour
    if 5 <= current_hour < 12:
        return "Selamat Pagi"
    elif 12 <= current_hour < 18:
        return "Selamat Siang"
    else:
        return "Selamat Malam"

def run_main_menu(movies, users, current_user):
    """
    Menjalankan menu utama aplikasi.
    
    Parameters:
    movies (list): Daftar film
    users (dict): Data pengguna
    current_user (str): Email pengguna saat ini
    
    Returns:
    None
    """
    while True:
        print("\nPilih Opsi:")
        print("1. Menu Utama")
        print("2. Pencarian Film")
        print("3. Rekomendasi Personal")
        print("4. Pengaturan Akun")
        print("5. Kembali ke Menu Awal")
        
        try:
            choice = int(input("Masukkan pilihan Anda: "))
            if choice == 1:
                main_menu(movies, users, current_user)
            elif choice == 2:
                search_menu(movies)
            elif choice == 3:
                show_personal_recommendations(movies, users, current_user)
            elif choice == 4:
                account_settings(users, current_user)
            elif choice == 5:
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def main_menu(movies, users, current_user):
    """
    Menampilkan dan mengelola menu utama.
    
    Parameters:
    movies (list): Daftar film
    users (dict): Data pengguna
    current_user (str): Email pengguna saat ini
    
    Returns:
    None
    """
    while True:
        print("\nPilih Opsi Menu Utama:")
        print("1. Tampilkan Semua Film")
        print("2. Film Teratas (Berdasarkan Rating)")
        print("3. Statistik Film")
        print("4. Watchlist Saya")
        print("5. Beri Rating Film")
        print("6. Tambah Film Baru")
        print("7. Kembali")
        try:
            choice = int(input("Masukkan pilihan Anda: "))
            if choice == 1:
                display_movies(movies)
            elif choice == 2:
                display_top_movies(sort_movies_by_rating(movies.copy()))
            elif choice == 3:
                show_statistics(movies)
            elif choice == 4:
                manage_watchlist(movies, users, current_user)
            elif choice == 5:
                rate_movie(movies, users, current_user)
            elif choice == 6:
                add_new_movie(movies)
            elif choice == 7:
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def rate_movie(movies, users, current_user):
    """
    Memungkinkan pengguna memberi rating pada film.
    
    Parameters:
    movies (list): Daftar film
    users (dict): Data pengguna
    current_user (str): Email pengguna saat ini
    
    Returns:
    None
    """
    print("\n=== Beri Rating Film ===")
    display_movies(movies)
    
    title = input("\nMasukkan judul film yang ingin diberi rating: ")
    movie_exists = False
    
    for movie in movies:
        if movie["title"].lower() == title.lower():
            movie_exists = True
            try:
                rating = float(input("Masukkan rating (0-10): "))
                if 0 <= rating <= 10:
                    users[current_user]["ratings"][movie["title"]] = rating
                    print(f"\nBerhasil memberikan rating {rating} untuk film {movie['title']}")
                else:
                    print("\nRating harus berada di antara 0 dan 10!")
            except ValueError:
                print("\nRating harus berupa angka!")
            break
    
    if not movie_exists:
        print("\nFilm tidak ditemukan dalam database.")

def add_new_movie(movies):
    """
    Menambahkan film baru ke database.
    
    Parameters:
    movies (list): Daftar film
    
    Returns:
    list: Daftar film yang diperbarui
    """
    print("\n=== Tambah Film Baru ===")
    
    title = input("Masukkan judul film: ")
    genre = input("Masukkan genre film (pisahkan dengan koma jika lebih dari satu): ")
    
    while True:
        try:
            rating = float(input("Masukkan rating film (0-10): "))
            if 0 <= rating <= 10:
                break
            print("Rating harus berada di antara 0 dan 10!")
        except ValueError:
            print("Rating harus berupa angka!")
    while True:
        try:
            year = int(input("Masukkan tahun film: "))
            if 1888 <= year <= 2024:
                break
            print("Tahun tidak valid!")
        except ValueError:
            print("Tahun harus berupa angka!")
    new_movie = {"title": title,"genre": genre,"rating": rating,
        "year": year}
    movies.append(new_movie)
    print(f"\nFilm '{title}' berhasil ditambahkan!")
    
    return movies