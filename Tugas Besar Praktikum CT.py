#Versi satu File
import time
import json
from collections import defaultdict

def typing_effect(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def dynamic_greeting():
    current_hour = time.localtime().tm_hour
    if 5 <= current_hour < 12:
        return "Selamat Pagi"
    elif 12 <= current_hour < 18:
        return "Selamat Siang"
    else:
        return "Selamat Malam"

def load_users():
    default_admin = {
        "admin@movie.com": {"name": "Admin","phone": "123456789",
        "watchlist": [],"ratings": {},"preferences": {
        "favorite_genres": ["Action", "Drama"],"min_rating": 8.0}}}
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
            users.update(default_admin)
            return users
    except FileNotFoundError:
        return default_admin

def save_users(users):
    default_admin = {
        "admin@movie.com": {"name": "Admin","phone": "123456789",
        "watchlist": [],"ratings": {},"preferences": {
        "favorite_genres": ["Action", "Drama"],"min_rating": 8.0}}}
    users.update(default_admin)
    with open('users.json', 'w') as f:
        json.dump(users, f)

def main():
    while True:
        greeting = dynamic_greeting()
        typing_effect(f""" 
====================================================================
          {greeting}, SELAMAT DATANG DI DUNIA FILM!
====================================================================
Bayangkan Anda sedang memasuki sebuah bioskop digital. 
Kami siap membantu Anda menemukan film yang sempurna untuk ditonton.
🌟 Eksplor film terbaik dari berbagai genre.
🎥 Temukan rekomendasi khusus hanya untuk Anda.
🍿 Nikmati pengalaman sinematik tanpa keluar dari rumah!
====================================================================
""")  
        users = load_users()
        
        current_user = initial_prompt(users)
        if current_user is None:
            print("Terima kasih telah menggunakan sistem kami!")
            break
            
        movies = generate_movie_data()
        run_main_menu(movies, users, current_user)

def initial_prompt(users):
    while True:
        print("\nPilih Opsi:")
        print("1. Sudah menjadi anggota")
        print("2. Belum menjadi anggota")
        print("3. Keluar")
        
        choice = input("Masukkan pilihan Anda (1/2/3): ").strip()
        
        if choice == "1":
            return login_user(users)
        elif choice == "2":
            registered_email = user_registration(users)
            if registered_email:
                print("\nSilakan login dengan akun yang baru dibuat.")
                return login_user(users, registered_email)
            continue
        elif choice == "3":
            return None
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

def login_user(users, registered_email=None):
    while True:
        if registered_email:
            email = registered_email
        else:
            email = input("Masukkan email Anda: ").strip()
        
        if "@" not in email:
            print("Email harus mengandung simbol @!")
            continue
        if email in users:
            print(f"Selamat datang kembali, {users[email]['name']}!")
            return email
        else:
            print("Email tidak ditemukan. Silakan coba lagi atau daftar.")
            return None

def run_main_menu(movies, users, current_user):
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

def user_registration(users):
    print("\n=== Registrasi Anggota Baru ===")
    while True:
        name = input("Masukkan nama lengkap Anda: ").strip()
        phone = ""
        email = ""
        
        while True:
            phone = input("Masukkan nomor telepon Anda: ").strip()
            if phone.isdigit() and len(phone) >= 8:
                break
            print("Nomor telepon harus berupa angka dan minimal 8 digit!")
            if input("Ingin mencoba masukkan nomor telepon lagi? (y/n): ").lower() != 'y':
                return None
            
        while True:
            email = input("Masukkan alamat email Anda: ").strip()
            if "@" in email and "." in email:
                break
            print("Email tidak valid! Harus mengandung @ dan domain (contoh: user@domain.com)")
            if input("Ingin mencoba masukkan email lagi? (y/n): ").lower() != 'y':
                return None
        if not name or not phone or not email:
            print("Semua kolom harus diisi. Silakan coba lagi.")
        elif email in users:
            print("Email ini sudah terdaftar. Silakan gunakan email lain.")
        else:
            favorite_genres = []
            min_rating = 0.0
            
            print("\nMari atur preferensi film Anda!")
            
            while True:
                genre = input("Masukkan genre film favorit Anda (atau ketik 'selesai'): ").capitalize()
                if genre.lower() == 'selesai' and favorite_genres:
                    break
                if genre and genre not in favorite_genres:
                    favorite_genres.append(genre)
                print(f"Genre yang sudah ditambahkan: {', '.join(favorite_genres)}")
                if not favorite_genres or input("Ingin menambah genre lagi? (y/n): ").lower() != 'y':
                    if not favorite_genres:
                        print("Anda harus memasukkan minimal 1 genre!")
                        continue
                    break
            while True:
                try:
                    min_rating = float(input("\nMasukkan rating minimum film yang Anda sukai (0-10): "))
                    if 0 <= min_rating <= 10:
                        break
                    print("Rating harus antara 0 dan 10!")
                except ValueError:
                    print("Rating harus berupa angka!")
                if input("Ingin mencoba masukkan rating lagi? (y/n): ").lower() != 'y':
                    min_rating = 0.0
                    break
            
            users[email] = {
                "name": name,
                "phone": phone,
                "watchlist": [],
                "ratings": {},
                "preferences": {
                    "favorite_genres": favorite_genres,
                    "min_rating": min_rating
                }
            }
            save_users(users)

            print(f"\nSelamat datang, {name}!")
            print("Registrasi Anda berhasil dengan preferensi berikut:")
            print(f"Genre Favorit: {', '.join(favorite_genres)}")
            print(f"Rating Minimum: {min_rating}")
            return email
        
        if input("\nIngin mencoba registrasi lagi? (y/n): ").lower() != 'y':
            return None

def rate_movie(movies, users, current_user):
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

def main_menu(movies, users, current_user):
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

def generate_movie_data():
    movies = [
        {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "year": 1994},
        {"title": "The Dark Knight", "genre": "Action, Crime", "rating": 9.0, "year": 2008},
        {"title": "The Godfather", "genre": "Crime, Drama", "rating": 9.2, "year": 1972},
        {"title": "The Lord of the Rings: Return of the King", "genre": "Adventure, Fantasy", "rating": 9.0, "year": 2003},
        {"title": "Pulp Fiction", "genre": "Crime, Drama", "rating": 8.9, "year": 1994},
        {"title": "Schindler's List", "genre": "Biography, Drama", "rating": 9.0, "year": 1993},
        {"title": "Inception", "genre": "Action, Sci-Fi", "rating": 8.8, "year": 2010},
        {"title": "Fight Club", "genre": "Drama", "rating": 8.8, "year": 1999},
        {"title": "The Matrix", "genre": "Action, Sci-Fi", "rating": 8.7, "year": 1999},
        {"title": "Goodfellas", "genre": "Crime, Drama", "rating": 8.7, "year": 1990},
        {"title": "Star Wars: Episode V", "genre": "Action, Fantasy", "rating": 8.7, "year": 1980},
        {"title": "Parasite", "genre": "Comedy, Thriller", "rating": 8.6, "year": 2019},
        {"title": "Interstellar", "genre": "Adventure, Sci-Fi", "rating": 8.6, "year": 2014},
        {"title": "The Silence of the Lambs", "genre": "Crime, Thriller", "rating": 8.6, "year": 1991},
        {"title": "Saving Private Ryan", "genre": "Drama, War", "rating": 8.6, "year": 1998}
    ]
    return sorted(movies, key=lambda x: x["title"].lower())

def display_movies(movies):
    print("\n" + "=" * 80)
    print(f"{'No':4} | {'Judul':35} | {'Genre':15} | {'Rating':8} | {'Tahun'}")
    print("=" * 80)
    
    for i, movie in enumerate(movies, 1):
        stars = "★" * int(movie['rating'])
        print(f"{i:<4} | {movie['title'][:35]:<35} | {movie['genre'][:15]:<15} | {movie['rating']:<8.1f} | {movie['year']}")
    
    print("=" * 80)

def sort_movies_by_rating(movies):
    n = len(movies)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if movies[j]["rating"] < movies[j+1]["rating"]:
                movies[j], movies[j+1] = movies[j+1], movies[j]
                swapped = True
        if not swapped:
            break
    return movies

def display_top_movies(movies, limit=5):
    print(f"\n=== {limit} Film Teratas ===")
    display_movies(movies[:limit])

def show_statistics(movies):
    print("\n=== Statistik Film ===")
    
    genre_count = defaultdict(int)
    total_rating = 0
    years = []
    
    for movie in movies:
        genres = movie["genre"].split(", ")
        for genre in genres:
            genre_count[genre] += 1
        total_rating += movie["rating"]
        years.append(movie["year"])
    
    avg_rating = total_rating / len(movies)
    
    print("\nStatistik Genre:")
    for genre, count in sorted(genre_count.items()):
        print(f"- {genre}: {count} film")
    
    print(f"\nJumlah Film: {len(movies)}")
    print(f"Rating Rata-rata: {avg_rating:.2f}")
    print(f"Tahun Tertua: {min(years)}")
    print(f"Tahun Terbaru: {max(years)}")

def search_menu(movies):
    while True:
        print("\nPilih Metode Pencarian Film:")
        print("1. Cari Berdasarkan Judul")
        print("2. Cari Berdasarkan Genre")
        print("3. Cari Berdasarkan Rating")
        print("4. Cari Berdasarkan Tahun")
        print("5. Kembali")

        try:
            choice = int(input("Masukkan pilihan Anda: "))
            if choice == 1:
                search_by_title(movies)
            elif choice == 2:
                search_by_genre(movies)
            elif choice == 3:
                search_by_rating(movies)
            elif choice == 4:
                search_by_year(movies)
            elif choice == 5:
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def search_by_title(movies):
    query = input("Masukkan judul atau kata kunci: ").lower()
    results = [movie for movie in movies if query in movie["title"].lower()]
    
    if results:
        print(f"\nHasil Pencarian untuk \"{query}\":")
        display_movies(results)
    else:
        print(f"\nTidak ada film yang cocok dengan kata kunci \"{query}\".")

def search_by_genre(movies):
    genre = input("Masukkan genre yang dicari: ").capitalize()
    results = [movie for movie in movies if genre in movie["genre"]]
    
    if results:
        print(f"\nFilm dengan genre \"{genre}\":")
        display_movies(results)
    else:
        print(f"\nTidak ada film dengan genre \"{genre}\".")

def search_by_rating(movies):
    try:
        min_rating = float(input("Masukkan rating minimum (0-10): "))
        max_rating = float(input("Masukkan rating maksimum (0-10): "))
        
        if 0 <= min_rating <= max_rating <= 10:
            results = [movie for movie in movies if min_rating <= movie["rating"] <= max_rating]
            if results:
                print(f"\nFilm dengan rating antara {min_rating} dan {max_rating}:")
                display_movies(results)
            else:
                print(f"\nTidak ada film dengan rating dalam rentang tersebut.")
        else:
            print("Rating harus berada antara 0 dan 10!")
    except ValueError:
        print("Rating harus berupa angka!")

def search_by_year(movies):
    try:
        year = int(input("Masukkan tahun film: "))
        results = [movie for movie in movies if movie["year"] == year]
        
        if results:
            print(f"\nFilm dari tahun {year}:")
            display_movies(results)
        else:
            print(f"\nTidak ada film dari tahun {year}.")
    except ValueError:
        print("Tahun harus berupa angka!")

def show_personal_recommendations(movies, users, current_user):
    user_prefs = users[current_user]["preferences"]
    if not user_prefs["favorite_genres"]:
        print("\nAnda belum mengatur preferensi genre. Silakan atur di Pengaturan Akun.")
        return

    print("\n=== Rekomendasi Personal ===")
    recommendations = get_personalized_recommendations(movies, user_prefs)
    display_recommendations(recommendations[:5])

def get_personalized_recommendations(movies, preferences):
    recommendations = []
    for movie in movies:
        score = calculate_recommendation_score(movie, preferences)
        recommendations.append({"movie": movie, "score": score})
    return sorted(recommendations, key=lambda x: x["score"], reverse=True)

def calculate_recommendation_score(movie, preferences):
    base_score = movie["rating"] * 10
    genre_bonus = 0
    
    genre_match = 0
    for genre in preferences["favorite_genres"]:
        if genre in movie["genre"]:
            genre_match |= 1
    
    if genre_match:
        genre_bonus = 20
    
    total_score = base_score + genre_bonus
    
    if movie["rating"] < preferences["min_rating"]:
        total_score *= 0.5
        
    return total_score

def display_recommendations(recommendations):
    for i, rec in enumerate(recommendations, 1):
        movie = rec["movie"]
        score = rec["score"]
        print(f"\n{i}. {movie['title']}")
        print(f"   Genre: {movie['genre']}")
        print(f"   Rating: {'★' * int(movie['rating'])}")
        print(f"   Skor Rekomendasi: {score:.1f}")
        print("-" * 50)

def manage_watchlist(movies, users, current_user):
    while True:
        print("\n=== Watchlist Management ===")
        print("1. Tampilkan Watchlist")
        print("2. Tambah Film ke Watchlist")
        print("3. Hapus Film dari Watchlist")
        print("4. Kembali")
        
        try:
            choice = int(input("Masukkan pilihan: "))
            if choice == 1:
                display_watchlist(users[current_user]["watchlist"])
            elif choice == 2:
                add_to_watchlist(movies, users[current_user]["watchlist"])
            elif choice == 3:
                remove_from_watchlist(users[current_user]["watchlist"])
            elif choice == 4:
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input tidak valid!")

def display_watchlist(watchlist):
    if not watchlist:
        print("\nWatchlist Anda kosong.")
        return
    
    print("\nWatchlist Anda:")
    for i, title in enumerate(watchlist, 1):
        print(f"{i}. {title}")

def add_to_watchlist(movies, watchlist):
    display_movies(movies)
    title = input("\nMasukkan judul film yang ingin ditambahkan: ")
    
    if any(movie["title"].lower() == title.lower() for movie in movies):
        if title not in watchlist:
            watchlist.append(title)
            print(f"\n{title} berhasil ditambahkan ke watchlist!")
        else:
            print("\nFilm sudah ada dalam watchlist!")
    else:
        print("\nFilm tidak ditemukan!")

def remove_from_watchlist(watchlist):
    if not watchlist:
        print("\nWatchlist Anda kosong.")
        return
        
    display_watchlist(watchlist)
    try:
        index = int(input("\nMasukkan nomor film yang ingin dihapus: ")) - 1
        if 0 <= index < len(watchlist):
            removed = watchlist.pop(index)
            print(f"\n{removed} berhasil dihapus dari watchlist!")
        else:
            print("\nNomor tidak valid!")
    except ValueError:
        print("\nInput tidak valid!")

def account_settings(users, current_user):
    while True:
        print("\n=== Pengaturan Akun ===")
        print("1. Ubah Preferensi Genre")
        print("2. Ubah Rating Minimum")
        print("3. Lihat Profil")
        print("4. Kembali")
        
        try:
            choice = int(input("Masukkan pilihan: "))
            if choice == 1:
                update_genre_preferences(users[current_user])
            elif choice == 2:
                update_rating_preference(users[current_user])
            elif choice == 3:
                display_profile(users[current_user])
            elif choice == 4:
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input tidak valid!")

def update_genre_preferences(user):
    print("\nMasukkan genre favorit Anda (ketik 'selesai' untuk mengakhiri):")
    genres = []
    while True:
        genre = input("Genre: ").capitalize()
        if genre.lower() == 'selesai':
            break
        genres.append(genre)
    user["preferences"]["favorite_genres"] = genres
    print("\nPreferensi genre berhasil diperbarui!")

def update_rating_preference(user):
    while True:
        try:
            rating = float(input("\nMasukkan rating minimum (0-10): "))
            if 0 <= rating <= 10:
                user["preferences"]["min_rating"] = rating
                print("\nRating minimum berhasil diperbarui!")
                break
            else:
                print("Rating harus antara 0 dan 10!")
        except ValueError:
            print("Rating harus berupa angka!")

def display_profile(user):
    print("\n=== Profil Pengguna ===")
    print(f"Nama: {user['name']}")
    print(f"Genre Favorit: {', '.join(user['preferences']['favorite_genres']) or 'Belum diatur'}")
    print(f"Rating Minimum: {user['preferences']['min_rating']}")
    print(f"Jumlah Film di Watchlist: {len(user['watchlist'])}")

if __name__ == "__main__":
    main()
