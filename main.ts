input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (estado == 0) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        estado = 1
        basic.showIcon(IconNames.Happy)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0)
        estado = 0
        basic.clearScreen()
    }
    
})
input.onSound(DetectedSound.Loud, function on_sound_loud2() {
    
    if (estado == 0) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        estado = 1
        basic.showIcon(IconNames.Happy)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0)
        estado = 0
        basic.clearScreen()
        function on_sound_loud() {
            
        }
        
    }
    
})
let estado = 0
estado = 0
