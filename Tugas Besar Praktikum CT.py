import random

# Fungsi utama
def main():
    print("""
=============================================================
                SELAMAT DATANG DI DUNIA FILM!
=============================================================
Bayangkan Anda sedang memasuki sebuah bioskop digital.
Kami siap membantu Anda menemukan film yang sempurna untuk ditonton.

🌟 Eksplor film terbaik dari berbagai genre.
🎥 Temukan rekomendasi khusus hanya untuk Anda.
🍿 Nikmati pengalaman sinematik tanpa keluar dari rumah!
=============================================================
""")

    users = {
        "farel@example.com": {"name": "Farel", "phone": "123", "watchlist": []}
    }
    current_user = initial_prompt(users)

    movies = generate_movie_data()

    while True:
        print("\nPilih Opsi:")
        print("1. Cari Film")
        print("2. Menu Utama")
        print("3. Keluar")

        try:
            choice = int(input("Masukkan pilihan Anda: "))
            if choice == 1:
                search_menu(movies)
            elif choice == 2:
                main_menu(movies)
            elif choice == 3:
                print("Terima kasih telah menggunakan sistem rekomendasi film!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def main_menu(movies):
    while True:
        print("\nPilih Opsi Menu Utama:")
        print("1. Tampilkan Semua Film")
        print("2. Statistik Film")
        print("3. Rekomendasi Acak")
        print("4. Tambahkan Film Baru")
        print("5. Kembali ke Menu Awal")

        try:
            choice = int(input("Masukkan pilihan Anda: "))
            if choice == 1:
                display_movies(movies)
            elif choice == 2:
                show_statistics(movies)
            elif choice == 3:
                random_recommendation(movies)
            elif choice == 4:
                add_new_movie(movies)
            elif choice == 5:
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def search_menu(movies):
    while True:
        print("\nPilih Metode Pencarian Film:")
        print("1. Cari Berdasarkan Judul")
        print("2. Kembali ke Menu Awal")

        try:
            choice = int(input("Masukkan pilihan Anda: "))
            if choice == 1:
                query = input("Masukkan judul atau kata kunci: ")
                search_movie(movies, query)
            elif choice == 2:
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

# Fungsi untuk memeriksa status pengguna
def initial_prompt(users):
    while True:
        response = input("Apakah Anda anggota? (ya/tidak): ").strip().lower()
        if response == "ya":
            email = input("Masukkan email Anda: ").strip()
            if email in users:
                print(f"Selamat datang kembali, {users[email]['name']}!")
                return email
            else:
                print("Email tidak ditemukan. Silakan coba lagi atau daftar.")
        elif response == "tidak":
            return user_registration(users)
        else:
            print("Jawaban tidak valid. Silakan jawab dengan 'ya' atau 'tidak'.")

# Fungsi untuk registrasi pengguna baru
def user_registration(users):
    print("\n=== Registrasi Anggota Baru ===")
    while True:
        name = input("Masukkan nama lengkap Anda: ").strip()
        phone = input("Masukkan nomor telepon Anda: ").strip()
        email = input("Masukkan alamat email Anda: ").strip()

        if not name or not phone or not email:
            print("Semua kolom harus diisi. Silakan coba lagi.")
        elif email in users:
            print("Email ini sudah terdaftar. Silakan gunakan email lain.")
        else:
            users[email] = {"name": name, "phone": phone, "watchlist": []}
            print(f"\nSelamat datang, {name}! Registrasi Anda berhasil.")
            return email

# Fungsi untuk menghasilkan data film
def generate_movie_data():
    movies = [
        {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
        {"title": "The Dark Knight", "genre": "Action, Crime, Drama", "rating": 9.0},
        {"title": "The Godfather", "genre": "Crime, Drama", "rating": 9.2},
        {"title": "The Lord of the Rings: The Return of the King", "genre": "Adventure, Drama, Fantasy", "rating": 9.0},
        {"title": "Pulp Fiction", "genre": "Crime, Drama", "rating": 8.9},
        {"title": "Schindler's List", "genre": "Biography, Drama, History", "rating": 9.0},
        {"title": "Forrest Gump", "genre": "Drama, Romance", "rating": 8.8},
        {"title": "Inception", "genre": "Action, Adventure, Sci-Fi", "rating": 8.8},
        {"title": "Fight Club", "genre": "Drama", "rating": 8.8},
        {"title": "The Matrix", "genre": "Action, Sci-Fi", "rating": 8.7},
        {"title": "Goodfellas", "genre": "Crime, Drama", "rating": 8.7},
        {"title": "The Empire Strikes Back", "genre": "Action, Adventure, Fantasy", "rating": 8.7},
        {"title": "The Lord of the Rings: The Fellowship of the Ring", "genre": "Adventure, Drama, Fantasy", "rating": 8.8},
        {"title": "The Lord of the Rings: The Two Towers", "genre": "Adventure, Drama, Fantasy", "rating": 8.7},
        {"title": "Star Wars: A New Hope", "genre": "Action, Adventure, Fantasy", "rating": 8.6},
    ]
    return sorted(movies, key=lambda x: x["title"].lower())

# Fungsi untuk menampilkan semua film
def display_movies(movies):
    print("\nDaftar Film:")
    for movie in movies:
        print(f"- {movie['title']} ({movie['genre']}, Rating: {movie['rating']})")

# Fungsi untuk mencari film
def search_movie(movies, query):
    results = [movie for movie in movies if query.lower() in movie["title"].lower()]
    if results:
        print(f"\nHasil Pencarian untuk \"{query}\":")
        for movie in results:
            print(f"- {movie['title']} ({movie['genre']}, Rating: {movie['rating']})")
    else:
        print(f"\nMaaf, tidak ada film yang cocok dengan kata kunci \"{query}\".")

# Fungsi untuk menampilkan statistik film
def show_statistics(movies):
    genre_count = {}
    for movie in movies:
        genres = movie["genre"].split(", ")
        for genre in genres:
            genre_count[genre] = genre_count.get(genre, 0) + 1

    print("\nStatistik Film:")
    for genre, count in genre_count.items():
        print(f"- {genre}: {count} film")

# Fungsi untuk rekomendasi acak
def random_recommendation(movies):
    movie = random.choice(movies)
    print("\nRekomendasi Acak:")
    print(f"- {movie['title']} ({movie['genre']}, Rating: {movie['rating']})")

# Fungsi untuk menambahkan film baru
def add_new_movie(movies):
    print("\n=== Tambahkan Film Baru ===")
    title = input("Masukkan judul film: ")
    genre = input("Masukkan genre film: ").capitalize()
    try:
        rating = float(input("Masukkan rating film (0-10): "))
        if 0 <= rating <= 10:
            new_movie = {
                "title": title,
                "genre": genre,
                "rating": rating
            }
            movies.append(new_movie)
            movies.sort(key=lambda x: x["title"].lower())
            print(f"Film \"{title}\" berhasil ditambahkan!")
        else:
            print("Rating harus antara 0 dan 10.")
    except ValueError:
        print("Rating harus berupa angka.")

if __name__ == "__main__":
    main()
