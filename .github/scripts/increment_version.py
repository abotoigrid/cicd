import semver
import os

VERSION_FILE = "VERSION"

def read_version():
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, "r") as f:
            return f.read().strip()
    else:
        return "0.1.0"  # Initial version

def write_version(version):
    with open(VERSION_FILE, "w") as f:
        f.write(version)

if __name__ == "__main__":
    current_version = read_version()
    new_version = semver.bump_minor(current_version)  # Always bump
    write_version(new_version)
    print(new_version)