# dl - Command-line File Downloader

A simple command-line tool to download files using `aria2c` and automatically sort them into categorized directories.

## Features

- **Automatic Sorting**: Organizes downloaded files into categories (e.g., media, compressed, music) based on their file extension.
- **Flexible Configuration**: Easily customizable via a simple JSON configuration file.

## Prerequisites

- **aria2c**: The `aria2c` daemon must be installed and running.
  ```bash
  aria2c --enable-rpc --rpc-listen-all
  ```

## Installation

### Using uv

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Vortriz/dl
    cd dl
    ```

2.  **Install the package:**
    ```bash
    uv tool install .
    ```

### Using Nix

If you are using Nix, you can try it out without installation:

```bash
nix run github:Vortriz/dl
```

Or if you are using flakes, you can install it system-wide by adding the following to your inputs:

```nix
{
    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
        dl = {
            url = "github:Vortriz/dl";
            inputs.nixpkgs.follows = "nixpkgs";
        };
    };
}
```

and then adding `dl.packages.${system}.dl` to your `environment.systemPackages` or `home.packages`.

## Usage

The tool is straightforward to use from your terminal.

**Basic Download**

To download a file and have it automatically sorted into your configured downloads directory:

```bash
dl <URL>
```

**Download to a Specific Path**

To download a file to a specific directory or save it with a different name:

```bash
dl --path /path/to/save/ <URL>
```

## Configuration

On its first run, the tool will create a default configuration file at `~/.config/dl/config.json`. You can edit this file to customize the tool's behavior.

```json
{
    "DOWNLOADS_DIR": "~/Downloads",
    "CATEGORIES": {
        "apks": ["apk"],
        "archives": ["zip", "rar", "7z", "tar", "gz", "iso"],
        "media": ["mp4", "mkv", "avi", "flv", "mov"],
        "music": ["mp3", "flac", "wav", "ogg"]
    },
    "ARIA2_HOST": "http://localhost",
    "ARIA2_PORT": 6800,
    "ARIA2_SECRET": "",
    "UPDATE_INTERVAL": 0.5
}
```

You can add more categories or modify existing ones by editing the `CATEGORIES` section.

### Configuration Options

- `DOWNLOADS_DIR`: The base directory where categorized downloads will be saved.
- `CATEGORIES`: A mapping of category names to lists of file extensions. Files with these extensions will be moved into a subdirectory with the category name. Files that don't match any category will be placed in a directory named `misc`.
- `ARIA2_HOST`: The hostname for the `aria2c` RPC interface.
- `ARIA2_PORT`: The port for the `aria2c` RPC interface.
- `ARIA2_SECRET`: The secret token for the `aria2c` RPC interface. This can also be set via the `ARIA2_SECRET` environment variable, which will take precedence.
- `UPDATE_INTERVAL`: The refresh rate (in seconds) for the progress bar.
