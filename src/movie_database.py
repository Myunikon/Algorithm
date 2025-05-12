from collections import defaultdict

def generate_movie_data():
    """
    Menghasilkan data film.
    
    Returns:
    list: Daftar film
    """
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
    """
    Menampilkan daftar film dalam format tabel.
    
    Parameters:
    movies (list): Daftar film yang akan ditampilkan
    
    Returns:
    None
    """
    print("\n" + "=" * 80)
    print(f"{'No':4} | {'Judul':35} | {'Genre':15} | {'Rating':8} | {'Tahun'}")
    print("=" * 80)
    
    for i, movie in enumerate(movies, 1):
        stars = "★" * int(movie['rating'])
        print(f"{i:<4} | {movie['title'][:35]:<35} | {movie['genre'][:15]:<15} | {movie['rating']:<8.1f} | {movie['year']}")
    
    print("=" * 80)

def sort_movies_by_rating(movies):
    """
    Mengurutkan film berdasarkan rating.
    
    Parameters:
    movies (list): Daftar film
    
    Returns:
    list: Daftar film yang diurutkan
    """
    return sorted(movies, key=lambda x: x["rating"], reverse=True)

def display_top_movies(movies, limit=5):
    """
    Menampilkan film teratas berdasarkan rating.
    
    Parameters:
    movies (list): Daftar film yang sudah diurutkan
    limit (int): Jumlah film yang ditampilkan
    
    Returns:
    None
    """
    print(f"\n=== {limit} Film Teratas ===")
    display_movies(movies[:limit])

def show_statistics(movies):
    """
    Menampilkan statistik film.
    
    Parameters:
    movies (list): Daftar film
    
    Returns:
    None
    """
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
