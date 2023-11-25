def my_fav_film():
    film = input("Твій улюблений фільм: ").lower()
    if not film.startswith('"') and not film.endswith('"'):
        film = f'"{film.title()}"'
    print("Мій улюблений фільм то є", film )

my_fav_film()