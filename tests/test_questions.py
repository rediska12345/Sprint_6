import pytest
import allure
from data import TestData


class TestQuestions:
    
    @allure.title("Проверка выпадающего списка вопросов о важном")
    @pytest.mark.parametrize("question_index", list(range(8)))
    def test_questions_dropdown(self, main_page, question_index):
        with allure.step("Принять куки"):
            main_page.accept_cookies()
        
        with allure.step(f"Нажать на вопрос {question_index + 1}"):
            main_page.click_question(question_index)
        
        with allure.step(f"Проверить отображение и текст ответа {question_index + 1}"):
            # Проверка что ответ отображается
            is_displayed = main_page.is_answer_displayed(question_index)
            
            # Проверка что текст ответа правильный
            actual_answer = main_page.get_answer_text(question_index)
            expected_answer = TestData.EXPECTED_ANSWERS[question_index]
            
            assert is_displayed, f"Ответ на вопрос {question_index + 1} не отображается"
            assert actual_answer == expected_answer, \
                f"Текст ответа не совпадает. Ожидалось: {expected_answer}, Получено: {actual_answer}"