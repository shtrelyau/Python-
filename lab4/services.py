from exceptions import TrackNotFoundError, InvalidDurationError


def add_track(tracks, track):
    if track.duration <= 0:
        raise InvalidDurationError("Длительность должна быть положительной!")
    tracks.append(track)


def find_by_title(tracks, title):
    for track in tracks:
        if track.title.lower() == title.lower():
            return track
    raise TrackNotFoundError(f"Композиция '{title}' не найдена!")


def find_by_artist(tracks, artist):
    result = []
    for track in tracks:
        if track.artist.lower() == artist.lower():
            result.append(track)
    return result


def filter_by_genre(tracks, genre):
    result = []
    for track in tracks:
        if track.genre.lower() == genre.lower():
            result.append(track)
    return result


def sort_by_duration(tracks):
    return sorted(tracks, key=lambda t: t.duration)


def average_duration(tracks):
    if not tracks:
        return 0
    total = 0
    for track in tracks:
        total += track.duration
    return total / len(tracks)


def delete_track(tracks, title):
    track = find_by_title(tracks, title)
    tracks.remove(track)


def create_playlist(tracks, name, genre):
    selected = []
    for track in tracks:
        if track.genre.lower() == genre.lower():
            selected.append(track)
    if not selected:
        return None
    from models import Playlist
    return Playlist(name, selected)