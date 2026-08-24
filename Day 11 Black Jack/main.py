# main.py
import sys
import subprocess
import tkinter as tk
import os
import traceback


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


def test_tkinter():
    """Test if tkinter is working"""
    try:
        print("Testing tkinter...")
        test_root = tk.Tk()
        test_root.title("Test Window")
        test_root.geometry("300x200")
        test_root.configure(bg='lightblue')

        label = tk.Label(test_root, text="Tkinter is working!", font=('Arial', 20), bg='lightblue')
        label.pack(expand=True)

        # Force window to show
        test_root.deiconify()
        test_root.lift()
        test_root.focus_force()
        test_root.update()

        # Close after 1 second
        test_root.after(1000, test_root.destroy)
        test_root.mainloop()
        return True
    except Exception as e:
        print(f"Tkinter test failed: {e}")
        return False


def main():
    print("=" * 60)
    print("♠️ BLACKJACK CASINO ♠️")
    print("=" * 60)
    print("Loading game...")
    print(f"Current directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")
    print("=" * 60)

    # Check for required packages
    if not check_requirements():
        print("Installing required packages...")
        if install_packages():
            print("Packages installed successfully!")
            print("Please restart the game.")
            input("Press Enter to exit...")
            return
        else:
            print("Failed to install required packages.")
            print("Please install Pillow manually: pip install Pillow")
            input("Press Enter to exit...")
            return

    # Test tkinter
    if not test_tkinter():
        print("Tkinter test failed! Please check your installation.")
        input("Press Enter to exit...")
        return

    print("Tkinter test passed!")

    # Import and run GUI
    try:
        print("\nImporting GUI module...")
        from gui import run_gui

        print("\nStarting Blackjack GUI...")
        print("The game window should appear now.")
        print("If it doesn't, check your taskbar or minimize other windows.")
        print("=" * 60)

        # Run the GUI with error catching
        try:
            run_gui()
        except Exception as e:
            print(f"ERROR in GUI execution: {e}")
            traceback.print_exc()
            input("Press Enter to exit...")

    except ImportError as e:
        print(f"Error importing modules: {e}")
        print("Please make sure all files are in the correct location.")
        print("Required files:")
        print("  - main.py (this file)")
        print("  - gui.py")
        print("  - game_logic.py")
        print("  - card_utils.py")
        print("  - constants.py")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
        input("Press Enter to exit...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
    except Exception as e:
        print(f"Fatal error: {e}")
        traceback.print_exc()
        input("Press Enter to exit...")