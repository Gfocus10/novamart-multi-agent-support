
import os
import zipfile

# The folder you are submitting
project_folder = "."

# Save the ZIP in the current starter directory
zip_name = "Novamart_submission.zip"

# Folders that should not be submitted
skip_dirs = {
    "venv",
    ".venv",
    "__pycache__",
    "node_modules",
    "build",
    ".git",
    "cdk.out",
    "logs",
    ".cache",
}

with zipfile.ZipFile(
    zip_name, "w", compression=zipfile.ZIP_DEFLATED
) as z:
    for root, dirs, files in os.walk(project_folder):
        # Do not enter unnecessary folders
        dirs[:] = [
            d for d in dirs
            if d not in skip_dirs
        ]

        for filename in files:
            # Do not include the ZIP file itself
            if filename == zip_name or filename.endswith(".zip"):
                continue

            filepath = os.path.join(root, filename)

            # Keep paths relative to the starter directory
            arcname = os.path.join(
                "starter",
                os.path.relpath(filepath, project_folder)
            )

            z.write(filepath, arcname)

print("ZIP file created successfully.")
print("File:", zip_name)
