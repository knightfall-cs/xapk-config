# XAPK Config

Generate XAPK manifest JSON files with ease using Python. This script simplifies the process of creating XAPK packages for app distribution by configuring expansion OBB files and split APKs.

## Features

- Support for multiple expansion OBB files.
- Flexible split APK configuration with optional APK IDs.
- Automatic OBB file naming based on package name and version code.

## Usage

1. Run the script using a Python interpreter.
2. Follow the prompts to enter XAPK details, OBB files, and APK configurations.
3. The script generates a `manifest.json` file with the configured XAPK settings.

## How to Create an XAPK Package using xapk-config

Welcome to the guide on creating an XAPK (eXpansion APK) package for your Android app using the `xapk-config` script.

### Prerequisites

- **Python:** Ensure you have Python installed on your system.
- **Clone Repository:** Clone the `xapk-config` repository to your local machine:

    ```bash
    git clone https://github.com/knightfall-cs/xapk-config.git
    cd xapk-config
    ```

### Steps

1. **Run the Script to Create the `manifest.json` File:**

    Open a terminal/command prompt and navigate to the `xapk-config` directory:

    ```bash
    cd path/to/xapk-config
    ```

    Run the script:

    ```bash
    python xapk-config.py
    ```

2. **Prepare Your Files:**

    Organize your app files as follows:

    - `Android/obb/{PackageName}/main.{VersionCode}.{PackageName}.obb`
    - `icon.png`
    - `manifest.json`
    - `{AppName}.apk`

    Replace `{PackageName}`, `{VersionCode}`, and `{AppName}` with your actual values.

    ```
     📂 Your-App-Files
     ├── Android/
     │    ├── obb/
     │    │    ├── {PackageName}/
     │    │    │    ├── main.{VersionCode}.{PackageName}.obb
     ├── icon.png
     ├── manifest.json
     ├── {AnyName}.apk
   ```   

4. **Create the XAPK:**

    - Package all the files (including the generated `manifest.json`) into a ZIP file.
    - Rename the ZIP file's extension from `.zip` to `.xapk`.

## Done.

---

Author: KNIGHTFALL
