import os

resources_path = input("Enter the full path to your resources folder: ").strip()

fxmanifest_template = """fx_version 'cerulean'
game 'gta5'

-- Files below are auto-imported from __resource.lua
"""

for root, dirs, files in os.walk(resources_path):
    if '__resource.lua' in files:
        old_path = os.path.join(root, '__resource.lua')
        new_path = os.path.join(root, 'fxmanifest.lua')

        print(f"[+] Converting: {old_path}")

        with open(old_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = fxmanifest_template + '\n' + content
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        os.remove(old_path)

        print(f"    => Converted to: {new_path}\n")

print("All __resource.lua files have been converted.")
