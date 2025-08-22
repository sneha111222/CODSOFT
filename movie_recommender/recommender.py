import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class ContentBasedRecommender:
    def __init__(self, csv_path):
        self.movies = pd.read_csv(csv_path)
        self._prepare()

    def _prepare(self):
        self.movies['genre'] = self.movies['genre'].fillna('')
        tfidf = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
        self.tfidf_matrix = tfidf.fit_transform(self.movies['genre'])
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        self.indices = pd.Series(self.movies.index, index=self.movies['title']).drop_duplicates()

    def recommend(self, title, top_n=5):
        idx = self.indices.get(title)
        if idx is None:
            return [f"Movie '{title}' not found."]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        top_indices = [i[0] for i in sim_scores[1:top_n+1]]
        return self.movies['title'].iloc[top_indices].tolist()
