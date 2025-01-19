from fastapi import FastAPI, status

app=FastAPI

@app.get("user", tags=["user"], summary="about user")
def user():
    return "user"

@app.get("cat", tags=["cat"], summary="about cat")
def cat():
    return "cat"

@app.get("car", tags=["car"], summary="about car")
def car():
    return "car"

@app.get("plane", tags=["plane"], summary="about plane")
def plane():
    return "plane"

####
@app.post("user", tag=["user"], summary="about user")
def user():
    return "user"

@app.post("cat", tag=["cat"], summary="about cat")
def cat():
    return "cat"

@app.post("car", tag=["car"], summary="about car")
def car():
    return "car"

@app.post("plane", tags=["plane"], summary="about plane")
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