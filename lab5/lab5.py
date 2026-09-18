from models import Track
from operations import filter_objects, transform_objects, sort_objects, average
from generators import tracks_by_genre, tracks_longer_than, TrackIterator


def create_tracks():
    return [
        Track("Секвойя", "GONE.Fludd", "Rap", 300, 4.9),
        Track("Жди меня", "Земфира", "Rock", 283, 4.8),
        Track("Эгоизм", "Noize MC", "Pop", 294, 4.7),
        Track("Из окна", "Noize MC", "Pop", 233, 4.5),
        Track("Маленький", "Дайте танк", "Rock", 301, 4.6),
        Track("Утренний расвет", "Король и Шут", "Rock", 294, 4.3),
    ]


def show_tracks(tracks):
    if not tracks:
        print("Список пуст!")
        return
    for index, track in enumerate(tracks, start=1):
        print(f"{index}. {track}")


def check_artist(tracks, artist):
    has_artist = any(t.artist.lower() == artist.lower() for t in tracks)
    if has_artist:
        print(f"Исполнитель {artist} есть в списке.")
    else:
        print(f"Исполнителя {artist} нет в списке.")


def menu():
    print("\n===== МЕНЮ =====")
    print("1. Показать все композиции")
    print("2. Фильтр по рейтингу")
    print("3. Получить названия")
    print("4. Сортировка по длительности")
    print("5. Средняя длительность")
    print("6. Проверка: есть ли композиции жанра")
    print("7. Проверка: все ли длиннее N")
    print("8. Генератор по жанру")
    print("9. Генератор длиннее N")
    print("10. Собственный итератор")
    print("11. Проверка наличия исполнителя")
    print("0. Выход")


def lab5():
    tracks = create_tracks()
    print(f"Создано композиций: {len(tracks)}")

    while True:
        menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_tracks(tracks)

        elif choice == "2":
            try:
                minimum = float(input("Минимальный рейтинг: "))
            except ValueError:
                print("Ошибка: нужно число!")
                continue
            result = filter_objects(tracks, lambda t: t.rating >= minimum)
            show_tracks(result)

        elif choice == "3":
            names = transform_objects(tracks, lambda t: t.title)
            print("Названия:")
            for name in names:
                print(f"- {name}")

        elif choice == "4":
            result = sort_objects(tracks, lambda t: t.duration)
            show_tracks(result)

        elif choice == "5":
            durations = [t.duration for t in tracks]
            avg = average(durations)
            print(f"Средняя длительность: {avg:.2f} сек.")

        elif choice == "6":
            genre = input("Введите жанр: ")
            has_genre = any(t.genre.lower() == genre.lower() for t in tracks)
            if has_genre:
                print(f"Есть композиции жанра {genre}.")
            else:
                print(f"Композиций жанра {genre} нет.")

        elif choice == "7":
            try:
                minimum = int(input("Минимальная длительность: "))
            except ValueError:
                print("Ошибка: нужно число!")
                continue
            all_longer = all(t.duration > minimum for t in tracks)
            if all_longer:
                print("Все композиции длиннее указанного значения.")
            else:
                print("Не все композиции длиннее указанного значения.")

        elif choice == "8":
            genre = input("Введите жанр: ")
            for track in tracks_by_genre(tracks, genre):
                print(track)

        elif choice == "9":
            try:
                minimum = int(input("Минимальная длительность: "))
            except ValueError:
                print("Ошибка: нужно число!")
                continue
            for track in tracks_longer_than(tracks, minimum):
                print(track)

        elif choice == "10":
            iterator = TrackIterator(tracks)
            try:
                print("Первые три композиции через итератор:")
                print(next(iterator))
                print(next(iterator))
                print(next(iterator))
            except StopIteration:
                print("Элементы закончились.")

        elif choice == "11":
            artist = input("Введите исполнителя: ")
            check_artist(tracks, artist)

        elif choice == "0":
            print("Выход.")
            break

        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    lab5()