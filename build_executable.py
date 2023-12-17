import subprocess

def build_executable(entry_point_script="main.py", output_directory="dist"):
    try:
        print("Building the executable...")
        subprocess.run(["pyinstaller", "--onefile", "--distpath", output_directory, entry_point_script])
        print("Executable built successfully!")
    except Exception as e:
        print(f"An error occurred during the build process: {e}")

if __name__ == "__main__":
    build_executable()
