import screen_brightness_control as sbc


def get_displays() -> int:
    number_of_displays = 0
    try:
        # No one has more than 5 monitors
        for i in range(5):
            sbc.get_brightness(display=i)
            number_of_displays = i + 1
    except sbc.ScreenBrightnessError:
        return number_of_displays


def change_all_brightness(number_of_displays: int, brightness: int):
    for i in range(number_of_displays):
        sbc.set_brightness(brightness, display=i)
