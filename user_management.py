import json

def load_users():
    """
    Memuat data pengguna dari file JSON.
    
    Returns:
    dict: Data pengguna
    """
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
    """
    Menyimpan data pengguna ke file JSON.
    
    Parameters:
    users (dict): Data pengguna
    
    Returns:
    None
    """
    default_admin = {
        "admin@movie.com": {"name": "Admin","phone": "123456789",
        "watchlist": [],"ratings": {},"preferences": {
        "favorite_genres": ["Action", "Drama"],"min_rating": 8.0}}}
    users.update(default_admin)
    with open('users.json', 'w') as f:
        json.dump(users, f)

def initial_prompt(users):
    """
    Menampilkan prompt awal untuk login atau registrasi.
    
    Parameters:
    users (dict): Data pengguna
    
    Returns:
    str: Email pengguna yang login atau None jika keluar
    """
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
    """
    Melakukan login pengguna.
    
    Parameters:
    users (dict): Data pengguna
    registered_email (str, optional): Email yang baru didaftarkan
    
    Returns:
    str: Email pengguna yang login atau None jika gagal
    """
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

def user_registration(users):
    """
    Mendaftarkan pengguna baru.
    
    Parameters:
    users (dict): Data pengguna
    
    Returns:
    str: Email pengguna yang baru didaftarkan atau None jika gagal
    """
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

def account_settings(users, current_user):
    """
    Mengelola pengaturan akun pengguna.
    
    Parameters:
    users (dict): Data pengguna
    current_user (str): Email pengguna saat ini
    
    Returns:
    None
    """
    print("\n=== Pengaturan Akun ===")
    print(f"Nama: {users[current_user]['name']}")
    print(f"Email: {current_user}")
    print(f"Nomor Telepon: {users[current_user]['phone']}")
    print("\nPreferensi Film:")
    print(f"Genre Favorit: {', '.join(users[current_user]['preferences']['favorite_genres'])}")
    print(f"Rating Minimum: {users[current_user]['preferences']['min_rating']}")
    
    print("\nPilih Pengaturan untuk Diubah:")
    print("1. Ubah Nama")
    print("2. Ubah Nomor Telepon")
    print("3. Ubah Preferensi Film")
    print("4. Kembali")
    
    try:
        choice = int(input("Masukkan pilihan Anda: "))
        if choice == 1:
            new_name = input("Masukkan nama baru: ").strip()
            if new_name:
                users[current_user]["name"] = new_name
                print("Nama berhasil diubah!")
        elif choice == 2:
            while True:
                new_phone = input("Masukkan nomor telepon baru: ").strip()
                if new_phone.isdigit() and len(new_phone) >= 8:
                    users[current_user]["phone"] = new_phone
                    print("Nomor telepon berhasil diubah!")
                    break
                print("Nomor telepon harus berupa angka dan minimal 8 digit!")
        elif choice == 3:
            update_preferences(users, current_user)
        elif choice == 4:
            return
        else:
            print("Pilihan tidak valid!")
    except ValueError:
        print("Input tidak valid!")
    
    save_users(users)

def update_preferences(users, current_user):
    """
    Memperbarui preferensi film pengguna.
    
    Parameters:
    users (dict): Data pengguna
    current_user (str): Email pengguna saat ini
    
    Returns:
    None
    """
    print("\n=== Ubah Preferensi Film ===")
    print("1. Ubah Genre Favorit")
    print("2. Ubah Rating Minimum")
    print("3. Kembali")
    
    try:
        choice = int(input("Masukkan pilihan Anda: "))
        if choice == 1:
            favorite_genres = []
            while True:
                genre = input("Masukkan genre film favorit (atau ketik 'selesai'): ").capitalize()
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
            users[current_user]["preferences"]["favorite_genres"] = favorite_genres
            print("Genre favorit berhasil diubah!")
        elif choice == 2:
            while True:
                try:
                    min_rating = float(input("Masukkan rating minimum (0-10): "))
                    if 0 <= min_rating <= 10:
                        users[current_user]["preferences"]["min_rating"] = min_rating
                        print("Rating minimum berhasil diubah!")
                        break
                    print("Rating harus antara 0 dan 10!")
                except ValueError:
                    print("Rating harus berupa angka!")
        elif choice == 3:
            return
        else:
            print("Pilihan tidak valid!")
    except ValueError:
        print("Input tidak valid!")