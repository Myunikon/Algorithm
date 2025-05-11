from user_management import load_users, initial_prompt
from movie_database import generate_movie_data
from ui import typing_effect, dynamic_greeting, run_main_menu

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

if __name__ == "__main__":
    main()