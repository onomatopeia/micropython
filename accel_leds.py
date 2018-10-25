import pyb

SENSITIVITY = 3

accel = pyb.Accel()

sw = pyb.Switch()

leds = [pyb.LED(i) for i in range(1,5)]

def read_accel():
    return accel.x(), accel.y()


def decide(x,y):
    result =[]
    if x > SENSITIVITY:
        result.append(0)
    elif x < -SENSITIVITY:
        result.append(1)
    if y > SENSITIVITY:
        result.append(2)
    elif y < -SENSITIVITY:
        result.append(3)
    return result


def toggle_light(offs, ons):
    for led_off in offs:
        led_off.off()
    for led_on in ons:
        led_on.on()


def on_switch():
    on_leds = []
    try:    
        while True:
            off_leds = on_leds.copy()
            x,y = read_accel()
            on_leds = [leds[i] for i in decide(x,y)]
            toggle_light(off_leds, on_leds)
            pyb.delay(100)
    finally:
        toggle_light(on_leds, [])


"""
Unfortunately, adding on_switch as a callback function for the USR switch causes Memory Error.
>>> sw = pyb.Switch()
>>> sw.callback(on_switch)
>>> Uncaught exception in ExtInt interrupt handler line 3
MemoryError:
"""

