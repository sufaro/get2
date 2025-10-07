import RPi.GPIO as GPIO
class R2R_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwm_frequency = pwm_frequency

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        self.pwm.stop()
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print("Напряжение выходит за диапазон")
            return 0
        
        else: 
            duty_cycle = (voltage / self.dynamic_range)*100
            self.pwm.ChangeDutyCycle(duty_cycle)
            print("Коэффицент заполнения:", float((voltage / self.dynamic_range)*100))

if __name__ == "__main__":
    try:
        dac = R2R_DAC(12, 500, 3.29, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз")
    
    finally:
        dac.deinit()