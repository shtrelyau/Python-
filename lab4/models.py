class Track:
    def __init__(self, title, artist, genre, duration):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration

    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "genre": self.genre,
            "duration": self.duration
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["artist"],
            data["genre"],
            data["duration"]
        )

    def __str__(self):
        return f"{self.title} — {self.artist} ({self.genre}, {self.duration} сек.)"


class Playlist:
    def __init__(self, name, tracks):
        self.name = name
        self.tracks = tracks

    def to_dict(self):
        return {
            "name": self.name,
            "tracks": [t.to_dict() for t in self.tracks]
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            [Track.from_dict(t) for t in data["tracks"]]
        )

    def __str__(self):
        return f"Плейлист '{self.name}' ({len(self.tracks)} композиций)"