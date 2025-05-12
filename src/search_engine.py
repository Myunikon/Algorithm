from movie_database import display_movies

def search_menu(movies):
    """
    Menampilkan menu pencarian film.
    
    Parameters:
    movies (list): Daftar film
    
    Returns:
    None
    """
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
    """
    Mencari film berdasarkan judul.
    
    Parameters:
    movies (list): Daftar film
    
    Returns:
    None
    """
    query = input("Masukkan judul atau kata kunci: ").lower()
    results = [movie for movie in movies if query in movie["title"].lower()]
    
    if results:
        print(f"\nHasil Pencarian untuk \"{query}\":")
        display_movies(results)
    else:
        print(f"\nTidak ada film yang cocok dengan kata kunci \"{query}\".")

def search_by_genre(movies):
    """
    Mencari film berdasarkan genre.
    
    Parameters:
    movies (list): Daftar film
    
    Returns:
    None
    """
    genre = input("Masukkan genre yang dicari: ").capitalize()
    results = [movie for movie in movies if genre in movie["genre"]]
    
    if results:
        print(f"\nFilm dengan genre \"{genre}\":")
        display_movies(results)
    else:
        print(f"\nTidak ada film dengan genre \"{genre}\".")

def search_by_rating(movies):
    """
    Mencari film berdasarkan rating.
    
    Parameters:
    movies (list): Daftar film
    
    Returns:
    None
    """
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
    """
    Mencari film berdasarkan tahun.
    
    Parameters:
    movies (list): Daftar film
    
    Returns:
    None
    """
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
