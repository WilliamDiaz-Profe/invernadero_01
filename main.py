def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 200)
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
    if pins.analog_read_pin(AnalogPin.P0) > 600:
        basic.show_string("\"H.alta\"")
        basic.show_icon(IconNames.NO)
    elif pins.analog_read_pin(AnalogPin.P0) < 200:
        basic.show_string("\"H.baja\"")
        basic.show_icon(IconNames.NO)
    else:
        basic.show_string("\"H.normal\"")
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    while input.temperature() > 30:
        basic.show_icon(IconNames.NO)
        basic.clear_screen()
        basic.show_string("\"t.alta\"")
    while input.temperature() >= 8 and input.temperature() <= 30:
        basic.show_icon(IconNames.YES)
        basic.clear_screen()
        basic.show_string("\"t.normal\"")
    while input.temperature() < 8:
        basic.show_icon(IconNames.SWORD)
        basic.clear_screen()
        basic.show_string("\"t.baja\"")
input.on_button_pressed(Button.B, on_button_pressed_b)
