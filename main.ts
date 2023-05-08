input.onButtonPressed(Button.A, function () {
    x = x + 1
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("x=" + convertToText(x))
    y = x * (x + (x + 1))
    basic.showString("y=" + convertToText(y))
})
input.onButtonPressed(Button.B, function () {
    if (x > 0) {
        x = x - 1
    }
})
let y = 0
let x = 0
x = 0
