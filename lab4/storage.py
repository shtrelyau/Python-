import json
import csv
import os

from models import Track, Playlist


def ensure_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")


def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return [Track.from_dict(item) for item in data]


def save_json(tracks, path):
    data = [track.to_dict() for track in tracks]
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_playlists(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return [Playlist.from_dict(item) for item in data]


def save_playlists(playlists, path):
    data = [playlist.to_dict() for playlist in playlists]
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def export_csv(tracks, path):
    with open(path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["title", "artist", "genre", "duration"])
        for track in tracks:
            writer.writerow([track.title, track.artist, track.genre, track.duration])