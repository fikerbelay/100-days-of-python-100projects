"""
ui.py
------
Main user interface for PizzaPy.
"""

import customtkinter as ctk
from logic import create_receipt, format_receipt, calculate_bill
from receipt import ReceiptWindow


class PizzaApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # -----------------------------
        # Window Settings
        # -----------------------------

        self.title("🍕 PizzaPy")
        self.geometry("600x750")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.configure(fg_color="#FFF8E7")

        # -----------------------------
        # Variables
        # -----------------------------

        self.size = ctk.StringVar(value="M")
        self.pepperoni = ctk.BooleanVar(value=False)
        self.cheese = ctk.BooleanVar(value=False)
        self.delivery = ctk.BooleanVar(value=False)

        # Trace variables to auto-update
        self.size.trace('w', lambda *args: self.update_total())
        self.pepperoni.trace('w', lambda *args: self.update_total())
        self.cheese.trace('w', lambda *args: self.update_total())

        # -----------------------------
        # Build UI
        # -----------------------------

        self.create_header()
        self.create_customer_section()
        self.create_size_section()
        self.create_extra_section()
        self.create_order_section()

        # Initialize total
        self.update_total()


    # -----------------------------
    # Header
    # -----------------------------

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="🍕",
            font=("Arial", 70)
        )

        title.pack(
            pady=(20,0)
        )


        heading = ctk.CTkLabel(
            self,
            text="PizzaPy",
            font=("Arial",32,"bold"),
            text_color="#E63946"
        )

        heading.pack()


        subtitle = ctk.CTkLabel(
            self,
            text="Fresh • Hot • Delicious",
            font=("Arial",15)
        )

        subtitle.pack(
            pady=(0,20)
        )


    # -----------------------------
    # Customer Section
    # -----------------------------

    def create_customer_section(self):

        frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        frame.pack(
            fill="x",
            padx=40,
            pady=10
        )


        label = ctk.CTkLabel(
            frame,
            text="👤 Customer Name",
            font=("Arial",17,"bold")
        )

        label.pack(
            anchor="w",
            padx=20,
            pady=(15,5)
        )


        self.name_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Enter your name",
            height=40
        )

        self.name_entry.pack(
            padx=20,
            pady=(0,15),
            fill="x"
        )


    # -----------------------------
    # Size Section
    # -----------------------------

    def create_size_section(self):

        frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        frame.pack(
            fill="x",
            padx=40,
            pady=10
        )


        label = ctk.CTkLabel(
            frame,
            text="🍕 Choose Size",
            font=("Arial",17,"bold")
        )

        label.pack(
            anchor="w",
            padx=20,
            pady=(15,10)
        )


        size_frame = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        size_frame.pack(
            padx=20,
            pady=(0,15),
            fill="x"
        )


        sizes = [
            ("S", "Small ($15)"),
            ("M", "Medium ($20)"),
            ("L", "Large ($25)")
        ]

        for i, (value, label_text) in enumerate(sizes):

            radio = ctk.CTkRadioButton(
                size_frame,
                text=label_text,
                variable=self.size,
                value=value,
                font=("Arial",14)
            )

            radio.grid(
                row=0,
                column=i,
                padx=10,
                pady=5
            )


    # -----------------------------
    # Extra Section
    # -----------------------------

    def create_extra_section(self):

        frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        frame.pack(
            fill="x",
            padx=40,
            pady=10
        )


        label = ctk.CTkLabel(
            frame,
            text="🧀 Extras",
            font=("Arial",17,"bold")
        )

        label.pack(
            anchor="w",
            padx=20,
            pady=(15,10)
        )


        self.pepperoni_check = ctk.CTkCheckBox(
            frame,
            text="Pepperoni ($2-3)",
            variable=self.pepperoni,
            font=("Arial",14)
        )

        self.pepperoni_check.pack(
            anchor="w",
            padx=20,
            pady=(0,5)
        )


        self.cheese_check = ctk.CTkCheckBox(
            frame,
            text="Extra Cheese ($1)",
            variable=self.cheese,
            font=("Arial",14)
        )

        self.cheese_check.pack(
            anchor="w",
            padx=20,
            pady=(0,5)
        )


        self.delivery_check = ctk.CTkCheckBox(
            frame,
            text="🚀 Delivery (ETA: 20-30min)",
            variable=self.delivery,
            font=("Arial",14)
        )

        self.delivery_check.pack(
            anchor="w",
            padx=20,
            pady=(0,15)
        )


    # -----------------------------
    # Order Section
    # -----------------------------

    def create_order_section(self):

        frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        frame.pack(
            fill="x",
            padx=40,
            pady=10
        )


        self.total_label = ctk.CTkLabel(
            frame,
            text="💵 Total: $20",
            font=("Arial",20,"bold"),
            text_color="#2B2D42"
        )

        self.total_label.pack(
            pady=(15,5)
        )


        order_button = ctk.CTkButton(
            frame,
            text="🍕 Place Order",
            font=("Arial",18,"bold"),
            height=50,
            corner_radius=12,
            fg_color="#E63946",
            hover_color="#C1121F",
            command=self.place_order
        )

        order_button.pack(
            padx=20,
            pady=(5,15),
            fill="x"
        )


        dark_mode_button = ctk.CTkButton(
            frame,
            text="🌙 Dark Mode",
            font=("Arial",14),
            height=35,
            corner_radius=10,
            fg_color="#2B2D42",
            hover_color="#1A1A2E",
            command=self.toggle_mode
        )

        dark_mode_button.pack(
            padx=20,
            pady=(0,15),
            fill="x"
        )


    # -----------------------------
    # Update Total (Optimized)
    # -----------------------------

    def update_total(self):
        """Update the total price display"""
        try:
            total = calculate_bill(
                self.size.get(),
                self.pepperoni.get(),
                self.cheese.get()
            )

            self.total_label.configure(
                text=f"💵 Total: ${total}"
            )

            # Update the window title to show total
            self.title(f"🍕 PizzaPy - ${total}")

        except Exception as e:
            # Handle any errors gracefully
            self.total_label.configure(
                text=f"⚠️ Error: {str(e)}"
            )


    # -----------------------------
    # Place Order (Optimized)
    # -----------------------------

    def place_order(self):
        """Place the order and show receipt"""
        try:
            # Get customer name
            name = self.name_entry.get().strip()
            if not name:
                name = "Guest"

            # Create receipt
            receipt = create_receipt(
                name=name,
                size=self.size.get(),
                pepperoni=self.pepperoni.get(),
                cheese=self.cheese.get(),
                delivery=self.delivery.get()
            )

            # Format receipt
            receipt_text = format_receipt(receipt)

            # Show receipt window
            ReceiptWindow(
                self,
                receipt_text
            )

        except Exception as e:
            # Show error in a message box
            from tkinter import messagebox
            messagebox.showerror(
                "Error",
                f"Failed to place order:\n{str(e)}"
            )


    # -----------------------------
    # Dark Mode (Optimized)
    # -----------------------------

    def toggle_mode(self):
        """Toggle between light and dark mode"""
        try:
            if ctk.get_appearance_mode() == "Light":
                ctk.set_appearance_mode("dark")
                self.configure(fg_color="#222222")
            else:
                ctk.set_appearance_mode("light")
                self.configure(fg_color="#FFF8E7")
        except Exception as e:
            print(f"Error toggling mode: {e}")


# -----------------------------
# Run Test
# -----------------------------

if __name__ == "__main__":
    app = PizzaApp()
    app.mainloop()