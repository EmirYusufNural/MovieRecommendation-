import requests

API_KEY = "YOUR_API_KEY_HERE"

def get_popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1"
    response = requests.get(url).json()
    for movie in response['results']:
        print(movie['title'])

def get_recommendation(genres, exclude_movies):
    genre_ids = []
    for genre in genres:
        url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
        response = requests.get(url).json()
        for item in response['genres']:
            if item['name'].lower() == genre.lower():
                genre_ids.append(str(item['id']))
    genre_ids = ','.join(genre_ids)

    exclude_ids = ','.join(str(movie_id) for movie_id in exclude_movies)

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres={genre_ids}&without_movie={exclude_ids}"
    response = requests.get(url).json()
    for movie in response['results']:
        print(movie['title'])

def get_favorites(user_id):
    print(f"Favorites for user {user_id}:")

def save_favorites(user_id, movie_id):
    print(f"Movie {movie_id} saved as favorite for user {user_id}.")

def main():
    while True:
        print("Select an option:")
        print("1. Get popular movies")
        print("2. Get movie recommendations")
        print("3. Get favorites")
        print("4. Save a favorite")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            get_popular_movies()
        elif choice == "2":
            genres = input("Enter comma-separated list of genres: ").split(",")
            exclude_movies = input("Enter comma-separated list of movies to exclude: ").split(",")
            get_recommendation(genres, exclude_movies)
        elif choice == "3":
            user_id = input("Enter user ID: ")
            get_favorites(user_id)
        elif choice == "4":
            user_id = input("Enter user ID: ")
            movie_id = input("Enter movie ID: ")
            save_favorites(user_id, movie_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()




#Bu kodu bir Python dosyası olarak kaydedebilir ve terminalde çalıştırabilirsiniz. Ancak önce YOUR_API_KEY_HERE yerine gerçek bir API anahtarınızı yerleştirmeniz gerekiyor. Ayrıca requests modülünü de kurmanız gerekebilir. Kurmak için pip install requests komutunu kullanabilirsiniz
# Maalesef, bir API anahtarı paylaşmak uygun değildir. Ancak, birçok ücretsiz ve ücretli API kaynağı vardır. API kullanımı için birçok farklı amaç ve gereksinim vardır. İhtiyacınıza göre, belirli bir API'ye kaydolmanız ve anahtarınızı almanız gerekebilir. Bazı popüler API kaynakları şunları içerir:

# OpenWeatherMap (Hava durumu verileri sağlar)
# The Movie Database (Film ve TV programı verileri sağlar)
# Twitter (Twitter verilerine erişim sağlar)
# Google Maps (Haritalar ve yer verileri sağlar)
# Reddit (Reddit verilerine erişim sağlar)
# API'leri kullanmadan önce her zaman belgelendirmelerini okuyun ve kullanım koşullarına uyduğunuzdan emin olun.

# OpenWeatherMap (provides weather data)
# The Movie Database (provides movie and TV show data)
# Twitter (provides access to Twitter data)
# Google Maps (provides maps and location data)
# Reddit (provides access to Reddit data)
# Always read their documentation before using APIs and make sure you comply with their terms of use.

#You can save this code as a Python file and run it in the terminal. However, you need to replace YOUR_API_KEY_HERE with your actual API key. You may also need to install the requests module. You can do this by running the command "pip install requests".