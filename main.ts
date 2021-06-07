input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P0, 200)
    basic.showNumber(pins.analogReadPin(AnalogPin.P0))
    if (pins.analogReadPin(AnalogPin.P0) > 600) {
        basic.showString("\"H.alta\"")
        basic.showIcon(IconNames.No)
    } else if (pins.analogReadPin(AnalogPin.P0) < 200) {
        basic.showString("\"H.baja\"")
        basic.showIcon(IconNames.No)
    } else {
        basic.showString("\"H.normal\"")
        basic.showIcon(IconNames.Yes)
    }
})
input.onButtonPressed(Button.B, function () {
    while (input.temperature() > 30) {
        basic.showIcon(IconNames.No)
        basic.clearScreen()
        basic.showString("\"t.alta\"")
    }
    while (input.temperature() >= 8 && input.temperature() <= 30) {
        basic.showIcon(IconNames.Yes)
        basic.clearScreen()
        basic.showString("\"t.normal\"")
    }
    while (input.temperature() < 8) {
        basic.showIcon(IconNames.Sword)
        basic.clearScreen()
        basic.showString("\"t.baja\"")
    }
})
