class Track:
    def __init__(self, title, artist, genre, duration, rating):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def __str__(self):
        return f"{self.title} — {self.artist} ({self.genre}, {self.duration} сек., рейтинг {self.rating})"