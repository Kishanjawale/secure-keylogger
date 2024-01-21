# Keylogger and Word Replacer

This Python script uses the pynput library to log key presses into a file named "keylog.txt". Additionally, it provides a function to replace specified words in a given file.

## Features

- **Key Logging**: Records key presses and logs them into a file.
- **Word Replacement**: Allows users to replace specified words in a file.

## Usage

1. Run the key logger script:

   ```python
   python keylogger.py

1.To replace words in the log file, use the provided function:
  file_path = 'keylog.txt'
  old_word = 'backspace'
  new_word = '...'
  replace_word_in_file(file_path, old_word, new_word)

Example: Replace 'backspace' with '...' and 'space' with '_'.

## Dependencies
    pynput: A library for controlling and monitoring input devices.

## Contributing
    Feel free to contribute by opening issues or submitting pull requests. Please follow our code of conduct.
