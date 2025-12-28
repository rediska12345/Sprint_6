import pytest
import allure
from data import TestData


class TestQuestions:
    
    @allure.title("Проверка выпадающего списка вопросов о важном")
    @pytest.mark.parametrize("question_index", list(range(8)))
    def test_questions_dropdown(self, main_page, question_index):
        with allure.step(f"Нажать на вопрос {question_index + 1}"):
            main_page.accept_cookies()
            main_page.click_question(question_index)
        
        with allure.step(f"Проверить отображение ответа {question_index + 1}"):
            assert main_page.is_answer_displayed(question_index), \
                f"Ответ на вопрос {question_index + 1} не отображается"
        
        with allure.step(f"Проверить текст ответа {question_index + 1}"):
            actual_answer = main_page.get_answer_text(question_index)
            expected_answer = TestData.EXPECTED_ANSWERS[question_index]
            assert actual_answer == expected_answer, \
                f"Текст ответа не совпадает. Ожидалось: {expected_answer}, Получено: {actual_answer}"