"""
receipt.py
-----------
Handles the receipt window for PizzaPy.
"""

import customtkinter as ctk


class ReceiptWindow(ctk.CTkToplevel):
    def __init__(self, parent, receipt_text):
        super().__init__(parent)

        self.title("🧾 PizzaPy Receipt")
        self.geometry("400x500")
        self.resizable(False, False)

        self.configure(fg_color="#FFF8E7")

        # -----------------------------
        # Title
        # -----------------------------

        title = ctk.CTkLabel(
            self,
            text="🧾 Order Receipt",
            font=("Arial", 28, "bold"),
            text_color="#E63946"
        )
        title.pack(pady=(25, 10))


        # -----------------------------
        # Receipt Box
        # -----------------------------

        receipt_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="white"
        )
        receipt_frame.pack(
            padx=30,
            pady=20,
            fill="both",
            expand=True
        )


        receipt_label = ctk.CTkLabel(
            receipt_frame,
            text=receipt_text,
            font=("Courier New", 14),
            justify="left",
            text_color="#2B2D42"
        )

        receipt_label.pack(
            padx=20,
            pady=20
        )


        # -----------------------------
        # Close Button
        # -----------------------------

        close_button = ctk.CTkButton(
            self,
            text="Close",
            font=("Arial", 15, "bold"),
            height=40,
            corner_radius=12,
            fg_color="#E63946",
            hover_color="#C1121F",
            command=self.destroy
        )

        close_button.pack(
            pady=(0,25)
        )


# -----------------------------
# Preview Test
# -----------------------------

if __name__ == "__main__":

    example_receipt = """
🍕 PizzaPy
==============================

Customer : Yuta

Large Pizza        $25
Pepperoni          $3
Extra Cheese       $1

------------------------------
TOTAL              $29

ETA: 20-30 Minutes

❤️ Thank you for choosing PizzaPy!
==============================
"""

    app = ctk.CTk()
    app.geometry("300x200")

    button = ctk.CTkButton(
        app,
        text="Show Receipt",
        command=lambda: ReceiptWindow(app, example_receipt)
    )

    button.pack(pady=50)

    app.mainloop()