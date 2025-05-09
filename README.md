## 📦 Requirements

- Python 3.x

## 🚀 How to Use

1. Run the script using Python.
2. When prompted, enter the **full path to your resources folder**.
   Example:

3. The script will:
- Find all `__resource.lua` files,
- Convert them to `fxmanifest.lua` format,
- And remove the old files.

## ⚠️ Notes

- Make sure you have a backup of your files before running the script.
- This script assumes your `__resource.lua` files are compatible with `fxmanifest.lua`. Some manual adjustments might still be required.

## 🛠 Example

```bash
python convert_resources.py
# Enter your resource folder path when prompted.
