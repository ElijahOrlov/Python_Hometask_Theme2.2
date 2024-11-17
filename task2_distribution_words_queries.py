def show_query_distribution(word_queries: list) -> None:
    """
    Отобразить распределение количества слов в запросах
    :param word_queries: список поисковых запросов пользователя
    """

    # формируем словарь содержащий количество запросов, сгруппированных по количеству слов в каждом запросе
    query_distribution = {}
    for query in word_queries:
        words = query.split(' ')
        words_count = len(words)
        query_distribution.setdefault(words_count, 0)
        query_distribution[words_count] += 1

    # формируем вывод распределения количества слов в запросах
    queries_count = len(word_queries)
    for words_count, query_count in sorted(query_distribution.items()):
        query_percent = round((query_count * 100) / queries_count, 2)
        print(f"Поисковых запросов, содержащих {words_count} слов(а): {query_percent}%")


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    ]
show_query_distribution(queries)
