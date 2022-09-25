# from app import app
#
# test_client = app.test_client()  # этот метод возвращает тестовый клиент, с помощью которого сервис может отправлять запросы сам к себе
#
# # response = test_client.get('/users')  # здесь содержится ответ на запрос
# # print("json = ", response.json)
# # print("code = ", response.status_code)
#
# # # Тестируем POST-запрос
# # user_data = {
# #     'username': 'test-user',
# #     'password': 'test-user'
# # }
# # res = test_client.post('/users',
# #                        json=user_data,
# #                        content_type='application/json')  # при отправке через тестовый клиент мы должны указывать контент-тайп. Постман делал это автоматически, а здесь мы должны вручную
# #
# # print("json = ", res.json)
# # print("code = ", res.status_code)
#
# # # Задача 3 из инструкции:
# # # Нельзя отправить одним запросом мразу всех пользователей -- придётся писать цикл
# # users_data = [
# #    {'username': 'user1', 'password': '12345'},
# #    {'username': 'user2', 'password': '12345'},
# #    {'username': 'user3', 'password': '12345'},
# # ]
# #
# # response = test_client.get('/users')
# # print("json = ", response.json)
# # print("code = ", response.status_code)
# #
# # for user in users_data:
# #     test_client.post('/users',
# #                        json=user,
# #                        content_type='application/json')  # при отправке через тестовый клиент мы должны указывать контент-тайп. Постман делал это автоматически, а здесь мы должны вручную
# #
# # response = test_client.get('/users/2')
# # print("json = ", response.json)
# # print("code = ", response.status_code)
#
# res = test_client.delete('/users/2')
# print(f"{res = }")
# response = test_client.get('/users/2')
# print("json = ", response.json)
# print("code = ", response.status_code)
#

from app import app
users_data = [
   {'username': 'user1', 'password': '12345'},
   {'username': 'user2', 'password': '12345'},
   {'username': 'user3', 'password': '12345'},
]


test_client = app.test_client()
# response = test_client.get('/users')
response = test_client.get('/users/2')
print("json = ", response.json)
print("code = ", response.status_code)

res = test_client.delete('/users/2')
print(res.data)

response = test_client.get('/users/2')
print("json = ", response.json)
print("code = ", response.status_code)