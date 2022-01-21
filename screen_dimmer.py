import screen_brightness_control as sbc


def get_displays() -> int:
    number_of_displays = 0
    try:
        # No one has more than 5 monitors
        for i in range(5):
            sbc.set_brightness(20, i)
            number_of_displays += 1
            print(number_of_displays)
    except (LookupError, sbc.ScreenBrightnessError):
        return number_of_displays
    return number_of_displays


def change_all_brightness(brightness: int):
    for i in range(get_displays()):
        sbc.set_brightness(brightness, display=i)
