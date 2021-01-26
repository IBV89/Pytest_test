import pytest
from .pages.main_page import MainPage


link = 'https://yandex.ru/'
text_to_search = 'тензор'  # Запрос вводимый в поискомой строке
link_to_search = 'tensor.ru'  # Ссылка искомая среди результатов поиска
count_to_search_link = 5  # Количество совпадений поисковой ссылки в результатах


@pytest.mark.xfail
class TestSearchFromMainPage:
    @pytest.mark.main
    def test_find_with_search_line(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_search_line()
        page.input_text_to_search_line(text_to_search)
        page.should_be_suggest_list()
        page.go_to_result_in_search_line()
        page.should_be_search_result_ul()
        page.should_first_count_result_is_text(link_to_search, count_to_search_link)
