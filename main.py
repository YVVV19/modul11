from fastapi import FastAPI, status

app=FastAPI()


@app.get("user", tags=["read"], summary="about user")
def user():
    return "user"

@app.get("cat", tags=["read"], summary="about cat")
def cat():
    return "cat"

@app.get("car", tags=["read"], summary="about car")
def car():
    return "car"

@app.get("plane", tags=["read"], summary="about plane")
def plane():
    return "plane"

####
@app.post("user", tags=["create"], summary="about user")
def user():
    return "user"

@app.post("cat", tags=["create"], summary="about cat")
def cat():
    return "cat"

@app.post("car", tags=["create"], summary="about car")
def car():
    return "car"

@app.post("plane", tags=["create"], summary="about plane")
def plane():
    return "plane"

"""
Створить FastAPI додаток із кількома маршрутами, ви можете використовувати домашнє завдання з минулого модуля як приклад додатку.
Переконайтесь, що Swagger UI був доступний і працював з вашим API.
Піся цього, додайте детальні описи до кожного маршруту використовуючи Swagger. 
Зробіть скриншоти, як можна тестувати маршрути API через Swagger UI.
Додайте анотації та коментарі до кожного маршруту у вашому API.
Додайте описи, теги та сумарі до кожного маршруту.
Внесіть зміни в OpenAPI специфікацію, запишіть, які зміни були зроблені та чому.
"""