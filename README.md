# Extension Creator

This is a simple Python script to create a Chrome extension that replaces all images on a webpage with a given image URL.

## How to Use the Extension

1. **Create the Extension:**
   - Run the script `extension_creator.py` to generate your extension files.
   - You will be prompted to enter the name, version, description, and image URL for your extension.

2. **Load the Extension in Chrome:**
   - Open Chrome and navigate to `chrome://extensions/`.
   - Enable "Developer mode" in the top right corner.
   - Click on "Load unpacked" and select the folder containing your newly created extension.

3. **Functionality:**
   - Once loaded, the extension will automatically replace all images on the loaded pages with the specified replacement image URL.
   - The extension also handles dynamically loaded images (e.g., images loaded as you scroll).

4. **Notes:**
   - Ensure that the URL of the replacement image is publicly accessible.
   - The extension works on all pages loaded after activation.

## Files Generated

- **manifest.json**: Contains metadata and configuration for the Chrome extension.
- **content.js**: The script that handles image replacement on the webpage.
- **icon16.png**, **icon48.png**, **icon128.png**: Icons for your extension in various sizes.

## Requirements

- Python 3.x
- The `Pillow` library for generating icons. Install it via:

    ```bash
    pip install pillow
    ```
