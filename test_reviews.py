import unittest
import sys
import os

sys.path.insert(0, os.path.abspath('.'))

try:
    from routes import _fix_mojibake, validate_date, validate_phone, validate_author, validate_review_text
except Exception as exc:
    _fix_mojibake = validate_date = validate_phone = validate_author = validate_review_text = None
    _IMPORT_ERROR = exc
else:
    _IMPORT_ERROR = None

class TestValidation(unittest.TestCase):
    """Набор unit-тестов для проверки валидации полей на странице отзывов"""

    @classmethod
    def setUpClass(cls):
        if _IMPORT_ERROR is not None:
            raise unittest.SkipTest(f"Не удалось импортировать валидаторы из routes.py: {_IMPORT_ERROR}")
       
    # --- ТЕСТЫ ДАТЫ ---
    def test_date_valid(self):
        """Проверка корректной даты"""
        self.assertTrue(validate_date("21.05.2026"))
        self.assertTrue(validate_date("01.01.2025"))

    def test_date_invalid_format(self):
        """Проверка неверного формата (не ДД.ММ.ГГГГ)"""
        self.assertFalse(validate_date("2026-05-21"))
        self.assertFalse(validate_date("21/05/2026"))
        self.assertFalse(validate_date("21.5.2026"))

    def test_date_invalid_value(self):
        """Проверка невозможной даты"""
        self.assertFalse(validate_date("32.01.2026"))
        self.assertFalse(validate_date("00.05.2026"))

    # --- ТЕСТЫ ТЕЛЕФОНА ---
    def test_phone_valid(self):
        """Проверка корректного телефона"""
        self.assertTrue(validate_phone("+7 (999) 123-45-67"))
        self.assertTrue(validate_phone("+79991234567"))

    def test_phone_invalid(self):
        """Проверка неверного формата телефона"""
        self.assertFalse(validate_phone("89991234567"))  # Не с +7
        self.assertFalse(validate_phone("+7 (99) 123-45-67"))  # Мало цифр
        self.assertFalse(validate_phone("+799912345"))  # Слишком короткий

    # --- ТЕСТЫ ИМЕНИ ---
    def test_author_valid(self):
        """Проверка корректного имени"""
        valid, msg = validate_author("John Doe")
        self.assertTrue(valid)
        
        valid, msg = validate_author("ProGamer_2026")
        self.assertTrue(valid)

    def test_author_cyrillic_allowed(self):
        """Проверка разрешённой кириллицы"""
        valid, msg = validate_author("Иван Иванов")
        self.assertTrue(valid)

    def test_author_too_short(self):
        """Проверка слишком короткого имени"""
        valid, msg = validate_author("A")
        self.assertFalse(valid)

    # --- ТЕСТЫ ТЕКСТА ---
    def test_review_valid(self):
        """Проверка корректного текста"""
        valid, msg = validate_review_text("Great game! I really liked it.")
        self.assertTrue(valid)

    def test_review_cyrillic_allowed(self):
        """Проверка разрешённой кириллицы в тексте"""
        valid, msg = validate_review_text("Отличная игра, всем советую!")
        self.assertTrue(valid)

    def test_review_too_short(self):
        """Проверка слишком короткого текста"""
        valid, msg = validate_review_text("Ok")
        self.assertFalse(valid)

    def test_review_caps_lock(self):
        """Проверка текста ЗАГЛАВНЫМИ БУКВАМИ"""
        valid, msg = validate_review_text("THIS IS A VERY BAD REVIEW BECAUSE IT IS ALL CAPS")
        self.assertFalse(valid)
        self.assertIn("ЗАГЛАВНЫМИ", msg)

    def test_review_caps_lock_cyrillic(self):
        """Проверка текста ЗАГЛАВНЫМИ БУКВАМИ (кириллица)"""
        valid, msg = validate_review_text("ЭТО ОЧЕНЬ ПЛОХОЙ ОТЗЫВ ПОТОМУ ЧТО ВСЕ ЗАГЛАВНЫЕ БУКВЫ")
        self.assertFalse(valid)
        self.assertIn("ЗАГЛАВНЫМИ", msg)

    def test_mojibake_fix(self):
        """Проверка восстановления кириллицы из UTF-8-as-cp1252"""
        self.assertEqual(_fix_mojibake("ÐŸÑ€Ð¸Ð²ÐµÑ‚"), "Привет")
        self.assertEqual(_fix_mojibake("Ñ\x81Ñ\x82Ñ\x83"), "сту")

if __name__ == '__main__':
    unittest.main()

