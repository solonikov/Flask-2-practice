# Обычно если папке дают название bla, то это означает, что содержимое папки ни на что не влияет

# def test_correct():
#    assert 2 == 2
#
# def test_equal():
#    assert "2" == 2

from app import app

def test_user_get_by_id():
   test_client = app.test_client()
   response = test_client.get('/users/1')
   assert response.status_code == 200
   assert response.json.get("username") # через response.json мы получаем доступ к телу ответа. Если username существует, то он вернётся как ответ. Если его нет, то вернётся none, и будет asserionerror
   assert response.json.get("username") == "test-user"
   assert response.json.get("id") == 1

"""
Тест не должен зависеть от наполнения базы данных в каждом конкретном случае.
Поэтому при выполнении тестов создаётся специальная тестовая база данных, и вся работа ведётся с ней!
Все тесты делаются независимо – БД создаётся под каждый тест заново и в конце каждого теста удаляется.
Все тесты должны быть абсолютно независимы!
"""