from recommender import ContentBasedRecommender

def main():
    recommender = ContentBasedRecommender("data/movies.csv")
    movie = input("🎬 Enter a movie you like: ")
    print("\n📽️ Recommended movies:")
    for rec in recommender.recommend(movie):
        print(f"- {rec}")

if __name__ == "__main__":
    main()
