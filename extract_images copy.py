import re, base64, pathlib

# Path to your manual.md
md_file = pathlib.Path("manual-extract/manual.md").read_text()

# Regex to capture base64 blocks
matches = re.findall(r"data:image/png;base64,([A-Za-z0-9+/=]+)", md_file)

# Save each match as step1.png, step2.png, ...
for i, b64 in enumerate(matches, start=1):
    img_data = base64.b64decode(b64)
    with open(f"manual-extract/images/step{i}.png", "wb") as f:
        f.write(img_data)

print(f"Extracted {len(matches)} images into ./images/")