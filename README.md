# ANSI Codes Storage Module

This Python module, `ansi.py`, provides a collection of ANSI escape codes for styling text output in the terminal. ANSI escape codes are used to change text color, background color, and apply various text styles.

## Classes

### `fg` (Foreground) Class

- Contains attributes for changing the text color.
- Provides various color options such as black, red, green, and more, each represented by an ANSI escape code.

### `bg` (Background) Class

- Contains attributes for changing the background color.
- Provides background color options similar to the `fg` class.

### `style` Class

- Contains attributes for applying text styles.
- Includes options to reset styles, apply bold, disable, underline, reverse (invert text/background colors), strikethrough, and make text invisible.

## How to Use

1. Import the `ansi` module in your Python script.

2. Create an instance of the desired class (e.g., `fg()`, `bg()`, or `style()`).

3. Use the attributes of the class to style your text output by concatenating them with the text.

4. Remember to use `style().reset` at the end to reset styles back to default.
