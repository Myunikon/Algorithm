import random
import time

def main():
    print("""
=============================================================
                SELAMAT DATANG DI DUNIA FILM!
=============================================================
Bayangkan Anda sedang memasuki sebuah bioskop digital.
Kami siap membantu Anda menemukan film yang sempurna untuk ditonton.

✨ Eksplor film terbaik dari berbagai genre.
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
        print("3. Quiz atau Fun Fact")
        print("4. Keluar")

        try:
            choice = int(input("Masukkan pilihan Anda: "))
            if choice == 1:
                loading_animation()  # Loading sebelum menu pencarian film
                search_menu(movies)
            elif choice == 2:
                loading_animation()  # Loading sebelum masuk ke menu utama
                main_menu(movies)
            elif choice == 3:
                loading_animation()  # Loading sebelum quiz atau fun fact
                fun_fact_or_quiz()
            elif choice == 4:
                print("Terima kasih telah menggunakan sistem rekomendasi film!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def loading_animation():
    for i in range(3):
        print("Loading" + "." * i, end="\r")
        time.sleep(0.5)

def initial_prompt(users):
    while True:
        response = input("Apakah Anda anggota? (ya/tidak): ").strip().lower()
        if response == "ya":
            email = input("Masukkan email Anda: ").strip()
            if validate_email(email) and email in users:
                print(f"Selamat datang kembali, {users[email]['name']}!")
                return email
            else:
                print("Email tidak ditemukan atau format salah. Silakan coba lagi atau daftar.")
        elif response == "tidak":
            return user_registration(users)
        else:
            print("Jawaban tidak valid. Silakan jawab dengan 'ya' atau 'tidak'.")

def validate_phone(phone):
    return phone.isdigit()

def validate_email(email):
    return "@" in email and "." in email

def user_registration(users):
    print("\n=== Registrasi Anggota Baru ===")
    while True:
        name = input("Masukkan nama lengkap Anda: ").strip()
        phone = input("Masukkan nomor telepon Anda: ").strip()
        email = input("Masukkan alamat email Anda: ").strip()

        if not name or not phone or not email:
            print("Semua kolom harus diisi. Silakan coba lagi.")
        elif not validate_phone(phone):
            print("Nomor telepon harus berupa angka. Silakan coba lagi.")
        elif not validate_email(email):
            print("Format email tidak valid. Silakan coba lagi.")
        elif email in users:
            print("Email ini sudah terdaftar. Silakan gunakan email lain.")
        else:
            users[email] = {"name": name, "phone": phone, "watchlist": []}
            print(f"\nSelamat datang, {name}! Registrasi Anda berhasil.")
            return email

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
                loading_animation()  # Loading sebelum menampilkan semua film
                display_movies(movies)
            elif choice == 2:
                loading_animation()  # Loading sebelum menampilkan statistik
                show_statistics(movies)
            elif choice == 3:
                loading_animation()  # Loading sebelum rekomendasi acak
                random_recommendation(movies)
            elif choice == 4:
                loading_animation()  # Loading sebelum menambahkan film baru
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

def fun_fact_or_quiz():
    print("\n=== Quiz atau Fun Fact ===")
    options = ["fun_fact", "quiz"]
    choice = random.choice(options)

    if choice == "fun_fact":
        facts = [
            "Tahukah Anda? Film 'The Shawshank Redemption' awalnya tidak sukses di box office!",
            "Film 'The Dark Knight' mendapatkan 8 nominasi Oscar.",
            "Film 'Inception' membutuhkan waktu 10 tahun untuk ditulis oleh Christopher Nolan."
        ]
        print(random.choice(facts))
    else:
        print("\nQuiz: Apa genre dari film 'The Godfather'?\n")
        answer = input("Jawaban Anda: ").strip().lower()
        if "crime" in answer and "drama" in answer:
            print("Benar! 'The Godfather' bergenre Crime, Drama.")
        else:
            print("Salah! Jawaban yang benar adalah Crime, Drama.")

def display_movies(movies):
    print("\nLeaderboard Film Terbaik:")
    print("=" * 60)
    print(f"{'No':<3} | {'Judul':<30} | {'Genre':<12} | {'Rating':<7}")
    print("=" * 60)
    for idx, movie in enumerate(sorted(movies, key=lambda x: x['rating'], reverse=True), start=1):
        stars = "★" * int(movie["rating"])
        print(f"{idx:<3} | {movie['title'][:30]:<30} | {movie['genre'][:12]:<12} | {stars}")

def search_movie(movies, query):
    results = [movie for movie in movies if query.lower() in movie["title"].lower()]
    if results:
        print(f"\nHasil Pencarian untuk \"{query}\":")
        for movie in results:
            stars = "\u2605" * int(movie["rating"])
            print(f"- {movie['title']} ({movie['genre']}, Rating: {movie['rating']} {stars})")
    else:
        print(f"\nMaaf, tidak ada film yang cocok dengan kata kunci \"{query}\".")

def generate_movie_data():
    movies = [
        {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
        {"title": "The Dark Knight", "genre": "Action, Crime, Drama", "rating": 9.0},
        {"title": "The Godfather", "genre": "Crime, Drama", "rating": 9.2},
        {"title": "Inception", "genre": "Action, Adventure, Sci-Fi", "rating": 8.8}
    ]
    return movies

def show_statistics(movies):
    genre_count = {}
    for movie in movies:
        genres = movie["genre"].split(", ")
        for genre in genres:
            genre_count[genre] = genre_count.get(genre, 0) + 1

    print("\nStatistik Film:")
    for genre, count in genre_count.items():
        print(f"- {genre}: {count} film")

def random_recommendation(movies):
    movie = random.choice(movies)
    stars = "\u2605" * int(movie["rating"])
    print("\nRekomendasi Acak:")
    print(f"- {movie['title']} ({movie['genre']}, Rating: {movie['rating']} {stars})")

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
            print(f"Film \"{title}\" berhasil ditambahkan!")
        else:
            print("Rating harus antara 0 dan 10.")
    except ValueError:
        print("Rating harus berupa angka.")

if __name__ == "__main__":
    main()
