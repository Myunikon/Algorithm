from movie_database import display_movies

def manage_watchlist(movies, users, current_user):
    """
    Mengelola watchlist pengguna.
    
    Parameters:
    movies (list): Daftar film
    users (dict): Data pengguna
    current_user (str): Email pengguna saat ini
    
    Returns:
    None
    """
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
    """
    Menampilkan watchlist pengguna.
    
    Parameters:
    watchlist (list): Daftar film dalam watchlist
    
    Returns:
    None
    """
    if not watchlist:
        print("\nWatchlist Anda kosong.")
        return
    
    print("\nWatchlist Anda:")
    for i, title in enumerate(watchlist, 1):
        print(f"{i}. {title}")

def add_to_watchlist(movies, watchlist):
    """
    Menambahkan film ke watchlist.
    
    Parameters:
    movies (list): Daftar film
    watchlist (list): Daftar film dalam watchlist
    
    Returns:
    None
    """
    display_movies(movies)
    title = input("\nMasukkan judul film yang ingin ditambahkan: ")
    
    if any(movie["title"].lower() == title.lower() for movie in movies):
        if title not in watchlist:
            watchlist.append(title)
            print(f"\n{title} berhasil ditambahkan ke watchlist!")
        else:
            print("\nFilm sudah ada dalam watchlist!")
    else:
        print("\nJudul film tidak ditemukan!")

def remove_from_watchlist(watchlist):
    """
    Menghapus film dari watchlist.
    
    Parameters:
    watchlist (list): Daftar film dalam watchlist
    
    Returns:
    None
    """
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
        print("\nInput harus berupa angka!")