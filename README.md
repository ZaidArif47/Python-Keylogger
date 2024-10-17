# Python Keylogger

This Python keylogger records every keystroke with a timestamp and saves it to a log file (`logs.txt`). It captures all key presses and logs them until the `Esc` key is pressed, which gracefully stops the logger.

## Features

- **Timestamped Logs**: Each keystroke is recorded with the exact time it was captured.
- **Append Mode Logging**: Keystrokes are continuously appended to the log file without clearing previous entries.
- **Termination**: Press the `Esc` key to stop logging, releasing resources automatically.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/zaidarif47/python-keylogger.git

2. **Navigate to the project directory**:
   ```bash
   cd python-keylogger

3. **Install dependencies**: The keylogger uses pynput for capturing keystrokes. Install it using pip
   ```bash
   pip install pynput

## How It Works

### **Commit 1:**
The `open` function is a built-in Python function used to open a file. It takes at least one argument—the file name—and an optional second argument specifying the mode (e.g., `"r"` for read, `"w"` for write, `"a"` for append). In this case:
- `open("logs.txt", "a")` opens the file `logs.txt` in append mode.
- When `open` is used, it allocates resources and memory to the file. Therefore, it is generally necessary to use the `close` function to release those resources from the system.

### **Commit 2:**
The `with` keyword simplifies resource management. By using `with`, memory is released automatically once the block is executed, which means we don’t need to manually close the file. This is especially beneficial when handling resources like file operations or listeners:
- The `with` keyword ensures that resources are released even if an error occurs, which reduces the risk of memory leaks.
  
### **Commit 3:**
To capture keystrokes, we import `Listener` from the `pynput.keyboard` module:
- The `writeToFile` function runs each time a key is pressed, taking `key` as a parameter and appending it to `logs.txt` by converting each key press to a string.
- By calling `.join()`, the script waits for keystrokes indefinitely, allowing us to capture and log keys until manually stopped. Without this, the listener would stop immediately after starting.

### **Commit 4:**
- Imported `datetime` to add timestamps to key logs.
- `strftime` stands for "string format time," which is used to format the timestamp.
- Used an f-string to efficiently append logs to the text file.
- Also imported `Key` from the `pynput.keyboard` package to set the Esc key as the termination key in the `on_release` function.
  - The `on_release` function checks if the Esc key is released; if it is, the function returns `False`, gracefully stopping the listener.
- The `Listener` continuously monitors the `on_release` condition, enabling it to detect when the Esc key is pressed.

## Example Log Entry
```bash
2024-10-17 17:18:33: 'H'
2024-10-17 17:18:34: 'i'
2024-10-17 17:18:34: Key.space
2024-10-17 17:18:36: Key.shift
2024-10-17 17:18:37: 'I'
2024-10-17 17:18:38: 't'
2024-10-17 17:18:39: Key.space
2024-10-17 17:18:39: 'i'
2024-10-17 17:18:39: 's'
2024-10-17 17:18:40: Key.space
2024-10-17 17:18:40: Key.shift
2024-10-17 17:18:40: 'Z'
2024-10-17 17:18:41: 'a'
2024-10-17 17:18:41: 'i'
2024-10-17 17:18:41: 'd'
```
This is displayed in the logs.txt file.
Each line logs the timestamp and the corresponding keystroke.

## Contributing
Feel free to fork the repository and make contributions. For any major changes, please open an issue first to discuss what you would like to change.

## License
This project is open-source and available under the MIT License.




