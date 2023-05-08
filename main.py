def on_button_pressed_a():
    global x
    x = x + 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global y
    basic.show_string("x=" + convert_to_text(x))
    y = x * (x + (x + 1))
    basic.show_string("y=" + convert_to_text(y))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global x
    if x < 2:
        x = x - 1
input.on_button_pressed(Button.B, on_button_pressed_b)

y = 0
x = 0
x = 1