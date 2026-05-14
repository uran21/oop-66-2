import time

class User:
    def __init__(self,name, role ):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            return func(user)
        else :
            print(f"У пользователя {user.name} нет доступа")
    return wrapper

@is_admin
def delete_video(user):
    print( "Видое Удалено")



admin = User("Ardager", "admin")
user = User("Bek", "user")

delete_video(admin)


def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Время выполнения: {round(execution_time,0)} секунд")
    return wrapper
@timer
def download_video():
    time.sleep(7)
    print("Видео загружено")

download_video()

