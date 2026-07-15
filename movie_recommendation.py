from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = {
    "Interstellar": "space science future adventure drama",
    "Inception": "dream science fiction thriller action",
    "Titanic": "romance drama ship historical",
    "Avengers": "superhero action science fiction",
    "The Dark Knight": "superhero action crime thriller",
    "Frozen": "animation family fantasy musical",
    "Jurassic Park": "dinosaurs adventure science fiction thriller",
    "The Conjuring": "horror supernatural mystery thriller",
    "Harry Potter": "fantasy magic adventure family",
    "Toy Story": "animation family comedy adventure"
}


def recommend_movies(movie_name, number_of_recommendations=3):
    movie_names = list(movies.keys())
    descriptions = list(movies.values())

    if movie_name not in movie_names:
        print("\nMovie not found.")
        print("Available movies:")

        for movie in movie_names:
            print("-", movie)

        return

    vectorizer = TfidfVectorizer()
    feature_matrix = vectorizer.fit_transform(descriptions)

    similarity_matrix = cosine_similarity(feature_matrix)

    movie_index = movie_names.index(movie_name)

    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda item: item[1],
        reverse=True
    )

    recommended_movies = similarity_scores[1:number_of_recommendations + 1]

    print(f"\nMovies recommended for '{movie_name}':")

    for index, score in recommended_movies:
        print(f"- {movie_names[index]} | Similarity Score: {score:.2f}")


def display_movies():
    print("=" * 50)
    print("         MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)
    print("\nAvailable Movies:")

    for movie in movies:
        print("-", movie)


def main():
    display_movies()

    user_movie = input("\nEnter a movie name: ").strip()

    matching_movie = None

    for movie in movies:
        if movie.lower() == user_movie.lower():
            matching_movie = movie
            break

    if matching_movie:
        recommend_movies(matching_movie)
    else:
        print("\nMovie not found. Please enter a movie from the list.")


if __name__ == "__main__":
    main()
