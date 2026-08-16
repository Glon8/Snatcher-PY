# Snatcher

**Snatcher** is a lightweight Python directory-monitoring utility extracted from my old **CustomKeys** project. It automatically copies files when changes are detected and includes a file restoration feature that can restore files if they are deleted from the source directory.

> **Important:** Snatcher does **not** delete files. It may overwrite existing directory when necessary.

## Features

* Monitors a directory for file changes
* Automatically copies changed files
* Restores files if they are deleted from the source directory
* Double-safe key bindings to prevent accidental activation
* Configurable through `config.json`
* Simple and lightweight console UI
* Optional emoji-based interface for consoles that support emojis

## Requirements

* Python **3.12.6 or higher** when activating the program through a code editor
* [`pynput`](https://pypi.org/project/pynput/)
* [`rich`](https://pypi.org/project/rich/)

Install the required packages with:

```bash
pip install pynput rich
```

## Usage

1. Download the project files.
2. Build the program with **PyInstaller**.
3. Run the program for the first time. A `config.json` file will be created.
4. Stop the program and open `config.json`.
5. Configure `path_from` and `path_to` according to your needs.
6. Restart the program.

## Configuration

The `config.json` file contains the following settings:

| Setting        | Description                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `display`      | Controls whether the interface uses emojis or plain text.                                                                                                 |
| `key_trigger`  | Configures the activation key bindings. Using at least two keys together is recommended to prevent accidental activation. Special keys are not supported. |
| `path_from`    | The source directory that Snatcher monitors.                                                                                                              |
| `path_to`      | The destination directory where files are copied and restored from when needed.                                                                           |
| `self_replace` | Enables or disables replacement of files in the source directory. Accepts `1` (enabled) or `0` (disabled). Disabled by default.                           |

### `self_replace`

`self_replace` is disabled by default.

When enabled, Snatcher is allowed to replace files in the source directory. This option should be used carefully, as it can overwrite the original files.

## Project Status

**Finished**
