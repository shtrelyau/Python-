def tracks_by_genre(tracks, genre):
    for track in tracks:
        if track.genre.lower() == genre.lower():
            yield track


def tracks_longer_than(tracks, minimum):
    for track in tracks:
        if track.duration > minimum:
            yield track


class TrackIterator:
    def __init__(self, tracks):
        self.tracks = tracks
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.tracks):
            raise StopIteration
        result = self.tracks[self.index]
        self.index += 1
        return result