import arcade

time_scheduler = 0


def schedule(func, time):
    def inner(*args, **kwargs):
        func()
        arcade.unschedule(inner)

    global time_scheduler
    arcade.schedule(inner, time_scheduler)
    time_scheduler += time
    return inner


def move_backward(step=1):
    def inner_move():
        print('going backward')

    for i in range(step):
        schedule(inner_move, 1)


def move_forward(step=1):
    def inner_move():
        print('going forward')

    for i in range(step):
        schedule(inner_move, 1)
