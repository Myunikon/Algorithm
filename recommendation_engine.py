from movie_database import display_movies

def show_personal_recommendations(movies, users, current_user):
    """
    Menampilkan rekomendasi film personal untuk pengguna.
    
    Parameters:
    movies (list): Daftar film
    users (dict): Data pengguna
    current_user (str): Email pengguna saat ini
    
    Returns:
    None
    """
    user_prefs = users[current_user]["preferences"]
    if not user_prefs["favorite_genres"]:
        print("\nAnda belum mengatur preferensi genre. Silakan atur di Pengaturan Akun.")
        return

    print("\n=== Rekomendasi Personal ===")
    recommendations = get_personalized_recommendations(movies, user_prefs)
    
    if recommendations:
        display_recommendations(recommendations[:5])
    else:
        print("\nTidak ada rekomendasi yang cocok dengan preferensi Anda saat ini.")
        print("Coba ubah preferensi Anda atau tambahkan lebih banyak genre favorit.")

def get_personalized_recommendations(movies, user_prefs):
    """
    Memberikan rekomendasi film berdasarkan preferensi pengguna.
    
    Parameters:
    movies (list): Daftar film
    user_prefs (dict): Preferensi pengguna
    
    Returns:
    list: Daftar film yang direkomendasikan dengan skor relevansi
    """
    favorite_genres = user_prefs["favorite_genres"]
    min_rating = user_prefs["min_rating"]
    
    # Filter film berdasarkan preferensi
    recommendations = []
    for movie in movies:
        # Periksa apakah genre film cocok dengan preferensi pengguna
        movie_genres = movie["genre"].split(", ")
        genre_match = any(genre in favorite_genres for genre in movie_genres)
        
        # Periksa apakah rating film memenuhi minimum
        rating_match = movie["rating"] >= min_rating
        
        if genre_match and rating_match:
            # Tambahkan skor relevansi untuk pengurutan
            relevance_score = 0
            for genre in movie_genres:
                if genre in favorite_genres:
                    relevance_score += 1
            
            # Tambahkan bonus untuk rating tinggi
            relevance_score += (movie["rating"] - min_rating) / 2
            
            recommendations.append({
                "movie": movie,
                "score": relevance_score
            })
    
    # Urutkan berdasarkan relevansi
    sorted_recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)
    
    return sorted_recommendations

def display_recommendations(recommendations):
    """
    Menampilkan daftar rekomendasi film.
    
    Parameters:
    recommendations (list): Daftar rekomendasi film
    
    Returns:
    None
    """
    if not recommendations:
        print("\nTidak ada rekomendasi yang tersedia.")
        return
        
    print("\nRekomendasi Film Untuk Anda:")
    print("=" * 60)
    
    for i, rec in enumerate(recommendations, 1):
        movie = rec["movie"]
        score = rec["score"]
        print(f"\n{i}. {movie['title']}")
        print(f"   Genre: {movie['genre']}")
        print(f"   Rating: {'★' * int(movie['rating'])}")
        print(f"   Tahun: {movie['year']}")
        print(f"   Skor Rekomendasi: {score:.1f}")
        print("-" * 60)

def get_trending_movies(movies, limit=5):
    """
    Mendapatkan film trending berdasarkan rating tertinggi.
    
    Parameters:
    movies (list): Daftar film
    limit (int): Jumlah film yang akan ditampilkan
    
    Returns:
    list: Daftar film trending
    """
    # Urutkan film berdasarkan rating (dari tinggi ke rendah)
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    
    # Tambahkan skor trending (sama dengan rating untuk saat ini)
    trending = [{"movie": movie, "score": movie["rating"]} for movie in sorted_movies[:limit]]
    
    return trending

def show_trending_movies(movies):
    """
    Menampilkan film trending.
    
    Parameters:
    movies (list): Daftar film
    
    Returns:
    None
    """
    print("\n=== Film Trending ===")
    trending = get_trending_movies(movies)
    display_recommendations(trending)

def show_genre_recommendations(movies, genre):
    """
    Menampilkan rekomendasi film berdasarkan genre tertentu.
    
    Parameters:
    movies (list): Daftar film
    genre (str): Genre yang dicari
    
    Returns:
    None
    """
    # Filter film berdasarkan genre
    genre_movies = [movie for movie in movies if genre in movie["genre"]]
    
    # Urutkan berdasarkan rating
    sorted_movies = sorted(genre_movies, key=lambda x: x["rating"], reverse=True)
    
    # Konversi ke format rekomendasi
    recommendations = [{"movie": movie, "score": movie["rating"]} for movie in sorted_movies[:5]]
    
    print(f"\n=== Rekomendasi Film Genre {genre} ===")
    display_recommendations(recommendations)