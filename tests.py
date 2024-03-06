from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # Проверка, что книги с возрастным рейтингом отсутствуют в списке книг для детей
    def test_get_books_for_children_not_age_rating_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Book1" not in children_books

    # Проверка,что у добавленной книги нет жанра
    def test_added_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book2")
        assert collector.get_book_genre("Book2") == ""

     # Проверка вывода жанра книги по её имени

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book3")
        collector.set_book_genre("Book3", "Детективы")
        assert collector.get_book_genre("Book3") == "Детективы"

    #Проверка вывода текущего словаря books_genre
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book4")
        collector.set_book_genre("Book4", "Детективы")
        books_genre = collector.get_books_genre()
        assert books_genre["Book4"] == "Детективы"

    # Проверка добавления книги в Избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Book5")
        collector.add_book_in_favorites("Book5")
        favorites = collector.get_list_of_favorites_books()
        assert "Book9" in favorites

    # Проверка удаления книги из Избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Book6")
        collector.add_book_in_favorites("Book6")
        collector.delete_book_from_favorites("Book6")
        favorites = collector.get_list_of_favorites_books()
        assert "Book8" not in favorites

    # Проверка получения списка Избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Book7")
        collector.add_book_in_favorites("Book7")
        favorites = collector.get_list_of_favorites_books()
        assert "Book11" in favorites

    # Параметризованный тест для метода set_book_genre

    import pytest
    @pytest.mark.parametrize("name, genre", [("Book8", "Фантастика"), ("Book9", "Ужасы")])
    def test_set_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # Параметризованный тест для метода get_books_with_specific_genre
    @pytest.mark.parametrize("genre, expected_books", [("Фантастика", ["Book10"]), ("Ужасы", ["Book11"])])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book("Book10")
        collector.add_new_book("Book11")
        collector.set_book_genre("Book10", "Фантастика")
        collector.set_book_genre("Book11", "Ужасы")
        assert collector.get_books_with_specific_genre(genre) == expected_books










