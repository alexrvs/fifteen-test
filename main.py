from Board import Board
from pynput import keyboard


b = Board()


def main():
    print(b)
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def on_press(key):
    pass


def on_release(key):
    if key == keyboard.Key.esc:
        return False
    elif key == keyboard.Key.up:
        b.board, b.e_loc = b.move_up(b.board, b.e_loc)
    elif key == keyboard.Key.right:
        b.board, b.e_loc = b.move_right(b.board, b.e_loc)
    elif key == keyboard.Key.left:
        b.board, b.e_loc = b.move_left(b.board, b.e_loc)
    elif key == keyboard.Key.down:
        b.board, b.e_loc = b.move_down(b.board, b.e_loc)
    b.refresh()


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

if __name__ == '__main__':
    main()