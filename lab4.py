from models import Track, Playlist
from services import (
    add_track, find_by_title, find_by_artist,
    filter_by_genre, sort_by_duration,
    average_duration, delete_track, create_playlist
)
from storage import (
    load_json, save_json, export_csv, ensure_data_folder,
    load_playlists, save_playlists
)
from exceptions import TrackNotFoundError, InvalidDurationError

JSON_PATH = "data/data.json"
PLAYLIST_PATH = "data/playlists.json"
CSV_PATH = "data/data.csv"


def input_track():
    title = input("Название: ")
    artist = input("Исполнитель: ")
    genre = input("Жанр: ")
    try:
        duration = int(input("Длительность (сек): "))
    except ValueError:
        print("Ошибка: нужно ввести целое число!")
        return None
    return Track(title, artist, genre, duration)


def show_tracks(tracks):
    if not tracks:
        print("Список пуст!")
        return
    for index, track in enumerate(tracks, start=1):
        print(f"{index}. {track}")


def show_playlists(playlists):
    if not playlists:
        print("Плейлистов нет.")
        return
    for index, playlist in enumerate(playlists, start=1):
        print(f"\n{index}. {playlist}")
        for track in playlist.tracks:
            print(f"   - {track}")


def menu():
    print("\n===== МЕНЮ =====")
    print("1. Добавить композицию")
    print("2. Показать все")
    print("3. Найти по названию")
    print("4. Найти по исполнителю")
    print("5. Фильтр по жанру")
    print("6. Сортировка по длительности")
    print("7. Средняя длительность")
    print("8. Удалить композицию")
    print("9. Сохранить в JSON")
    print("10. Экспорт в CSV")
    print("11. Создать плейлист")
    print("12. Показать плейлисты")
    print("0. Выход")


def lab4():
    ensure_data_folder()
    tracks = load_json(JSON_PATH)
    playlists = load_playlists(PLAYLIST_PATH)
    print(f"Загружено композиций: {len(tracks)}")
    print(f"Загружено плейлистов: {len(playlists)}")

    while True:
        menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            track = input_track()
            if track is None:
                continue
            try:
                add_track(tracks, track)
                print("Композиция добавлена!")
            except InvalidDurationError as error:
                print(f"Ошибка: {error}")

        elif choice == "2":
            show_tracks(tracks)

        elif choice == "3":
            title = input("Введите название: ")
            try:
                track = find_by_title(tracks, title)
                print(track)
            except TrackNotFoundError as error:
                print(f"Ошибка: {error}")

        elif choice == "4":
            artist = input("Введите исполнителя: ")
            result = find_by_artist(tracks, artist)
            if not result:
                print("Ничего не найдено.")
            else:
                show_tracks(result)

        elif choice == "5":
            genre = input("Введите жанр: ")
            result = filter_by_genre(tracks, genre)
            if not result:
                print("Ничего не найдено.")
            else:
                show_tracks(result)

        elif choice == "6":
            result = sort_by_duration(tracks)
            show_tracks(result)

        elif choice == "7":
            avg = average_duration(tracks)
            print(f"Средняя длительность: {avg:.2f} сек.")

        elif choice == "8":
            title = input("Введите название для удаления: ")
            try:
                delete_track(tracks, title)
                print("Композиция удалена!")
            except TrackNotFoundError as error:
                print(f"Ошибка: {error}")

        elif choice == "9":
            save_json(tracks, JSON_PATH)
            save_playlists(playlists, PLAYLIST_PATH)
            print("Сохранено в JSON.")

        elif choice == "10":
            export_csv(tracks, CSV_PATH)
            print("Экспортировано в CSV.")

        elif choice == "11":
            name = input("Название плейлиста: ")
            genre = input("Жанр для плейлиста: ")
            playlist = create_playlist(tracks, name, genre)
            if playlist is None:
                print("Нет композиций этого жанра.")
            else:
                playlists.append(playlist)
                print(f"Плейлист '{name}' создан ({len(playlist.tracks)} композиций).")

        elif choice == "12":
            show_playlists(playlists)

        elif choice == "0":
            save_json(tracks, JSON_PATH)
            save_playlists(playlists, PLAYLIST_PATH)
            print("Выход. Данные сохранены.")
            break

        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    lab4()