import RPi.GPIO as GPIO
import time


class IR:
    def __init__(self, ir_pin):
        self.pin = ir_pin

        # Values I sort of understand:
        self.bit_0 = 450
        self.bit_1 = 1500
        self.bits_len = 32
        self.bits = [0 for _ in range(self.bits_len)]

        # Values I don't understand:
        self.FirstLastBit = 15
        self.BIT_START = 4000
        self.remote_verification = 32257  # Used to be 16128

        # Values that are too long:
        self.key_keys = {
            32512: 'Power',
            32002: 'Function/Stop',
            31492: 'Rewind',
            31237: 'Pause/Play',
            30982: 'Fast Forward',
            32257: 'Vol +',
            30217: 'Vol -',
            30472: 'Down',
            29962: 'Up',
            29197: 'EQ',
            28942: 'Start/Repeat',
            29452: 0,
            28432: 1,
            28177: 2,
            27922: 3,
            27412: 4,
            27157: 5,
            26902: 6,
            26392: 7,
            26137: 8,
            25882: 9,
        }

    def time_pulse_us(self):
        # Wait for the pin to go HIGH
        while GPIO.input(self.pin) == GPIO.LOW:
            pass
        start_time = time.perf_counter()  # Record start time

        # Wait for the pin to go LOW
        while GPIO.input(self.pin) == GPIO.HIGH:
            pass
        end_time = time.perf_counter()  # Record end time

        # Calculate pulse duration in microseconds
        pulse_duration_us = (end_time - start_time) * 1000000
        return pulse_duration_us

    def get_ir_key(self):
        # If the initial pulse duration is less than BIT_START, it's not a valid IR pulse
        if not self.time_pulse_us() < self.BIT_START:
            self.pulse_to_bits()
            key_code = self.bits_to_int()

            key = self.key_keys.get(key_code, None)
            
            if key == None:
                f'Key {key_code} is unknown!'
            
            # Introduce a short delay to debounce or avoid reading too frequently
            time.sleep(0.2)
            return key

    def pulse_to_bits(self):
        # Translate the pulse durations into bits
        for bit in range(self.bits_len):
            pulse = self.time_pulse_us()

            if pulse > self.bit_1:
                self.bits[bit] = 1
            elif pulse > self.bit_0:
                self.bits[bit] = 0
            else:
                print(f'Error when translating the pulse {pulse} to bit.')

    def bits_to_int(self):
        # Convert the bit sequence into an integer (key code)
        key_code = 0
        seed = 1

        # We usually care only about the last 15 bits
        for bit in range(self.bits_len - self.FirstLastBit, self.bits_len):
            if self.bits[bit] == 1:
                key_code += seed
            seed *= 2

        return key_code

