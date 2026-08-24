# main.py
import sys
import subprocess


def check_requirements():
    """Check if required packages are installed"""
    try:
        import PIL
        return True
    except ImportError:
        return False


def install_packages():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
        return True
    except Exception as e:
        print(f"Failed to install packages: {e}")
        return False


def main():
    print("♠️ Blackjack Casino ♠️")
    print("Loading game...")

    # Check for required packages
    if not check_requirements():
        print("Installing required packages...")
        if install_packages():
            print("Packages installed successfully!")
            print("Please restart the game.")
            return
        else:
            print("Failed to install required packages.")
            print("Please install Pillow manually: pip install Pillow")
            return

    # Import and run GUI
    try:
        from gui import run_gui
        run_gui()
    except ImportError as e:
        print(f"Error importing modules: {e}")
        print("Please make sure all files are in the correct location.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()