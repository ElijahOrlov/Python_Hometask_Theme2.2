def find_uniq_geopoints(user_geopoints: dict) -> None:
    """
    Поиск уникальных гео-меток всех пользователей
    :param geopoints: словарь гео-меток пользователей
    """
    uniq_geopoints = set()
    for geopoint in user_geopoints.values():
        uniq_geopoints.update(geopoint)
    print(uniq_geopoints)


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
find_uniq_geopoints(ids)
