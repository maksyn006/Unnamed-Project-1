display_mode = {
    'is_game': False,
    'is_main_menu': True,
    'is_load_menu': False,
    'is_run': True
}


def set_display_mode_active(_mode: str):
    for mode in display_mode:
        if not mode == 'is_run':
            display_mode[mode] = False
    display_mode[_mode] = True


def set_display_mode_inactive(_mode: str):
    display_mode[_mode] = False


def disable_display_mode():
    for mode in display_mode:
        display_mode[mode] = False
