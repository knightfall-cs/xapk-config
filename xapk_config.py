import json

def add_obbs(pkg_name, version_code, num_obbs):
    obbs = []
    if num_obbs == 1:
        obb_file = f"main.{version_code}.{pkg_name}.obb"
        obb_path = f"Android/obb/{pkg_name}/{obb_file}"
        obb_install_path = obb_path
        obbs.append({"file": obb_path, "install_location": "EXTERNAL_STORAGE", "install_path": obb_install_path})
    else:
        for i in range(num_obbs):
            obb_file = input(f"Enter OBB file name {i + 1}: ")
            obb_path = f"Android/obb/{pkg_name}/{obb_file}"
            obb_install_path = obb_path
            obbs.append({"file": obb_path, "install_location": "EXTERNAL_STORAGE", "install_path": obb_install_path})
    return obbs

def add_split_apks(num_apks):
    split_apks = []
    for i in range(num_apks):
        apk_file = input(f"Enter APK file name {i + 1}: ")
        apk_id = "base" if num_apks == 1 else input(f"Enter APK ID for {apk_file}: ")
        split_apks.append({"file": apk_file, "id": apk_id})
    return split_apks

print("XAPK JSON Generator")
print("-------------------")

# Prompt user for XAPK information
xapk_version = int(input("XAPK version: "))
pkg_name = input("Package name: ")
name = input("App name: ")
version_code = input("Version code: ")
version_name = input("Version name: ")
icon = input("Icon filename: ")

# Prompt user for the number of OBB files and APKs
num_obbs = int(input("Number of OBB files: "))
num_apks = int(input("Number of APK files: "))

print("\nAdding expansion OBB files:")
print("--------------------------")
# Create XAPK data dictionary
xapk_data = {
    "xapk_version": xapk_version,
    "package_name": pkg_name,
    "name": name,
    "version_code": version_code,
    "version_name": version_name,
    "icon": icon,
    "expansions": add_obbs(pkg_name, version_code, num_obbs),
    "split_apks": add_split_apks(num_apks)
}

# Write the XAPK data to a JSON file
output_file_name = "manifest.json"
with open(output_file_name, "w") as json_file:
    json.dump(xapk_data, json_file, indent=4)

print("\nXAPK JSON file 'manifest.json' created successfully.")