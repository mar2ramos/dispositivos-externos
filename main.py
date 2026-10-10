def on_button_pressed_a():
    global estado
    if estado == 0:
        pins.digital_write_pin(DigitalPin.P0, 1)
        estado = 1
        basic.show_icon(IconNames.HAPPY)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
        estado = 0
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud2():
    global estado
    if estado == 0:
        pins.digital_write_pin(DigitalPin.P0, 1)
        estado = 1
        basic.show_icon(IconNames.HAPPY)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
        estado = 0
        basic.clear_screen()
        def on_sound_loud():
            pass
input.on_sound(DetectedSound.LOUD, on_sound_loud2)

estado = 0
estado = 0