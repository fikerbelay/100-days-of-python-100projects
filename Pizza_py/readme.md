PizzaPy

A modern pizza ordering desktop application built with **Python** and **CustomTkinter**.

PizzaPy allows users to customize their pizza, select toppings, choose delivery options, and receive a generated receipt through a beautiful modern interface.

---

#  Features

Modern graphical user interface  
Clean restaurant-style design  
Light/Dark mode support  
Real-time price calculation  
Custom pizza toppings  
Delivery option selection  
Automatic receipt generation  
Customer name input  
Fast and lightweight desktop application  
---

#  Technologies Used

- Python 3
- CustomTkinter
- Tkinter
- Pillow (Image Processing)

---

# 📂 Project Structure

```
PizzaPy/
│
├── main.py              # Application launcher

├── ui.py                # User interface

├── logic.py             # Pricing and order logic

├── receipt.py           # Receipt window
│
├── assets/

│   ├── pizza.png        # Pizza image

│   └── banner.png       # App images
│
├── screenshots/

│   └── home.png
│
├── requirements.txt

└── README.md
```

---

#  Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/PizzaPy.git
```

## 2. Open the project folder

```bash
cd PizzaPy
```

---

## 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 4. Install required packages

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install customtkinter pillow
```

---

# ▶️ Running the Application

Run:

```bash
python main.py
```

The PizzaPy application will launch.

---

# Dependencies

This project requires:

```
customtkinter
pillow
```

### CustomTkinter
Used to create the modern styled graphical interface.

### Pillow
Used for loading and displaying images inside the application.

---

#  How It Works

1. Enter your name
2. Choose pizza size
3. Add toppings
4. Select delivery option
5. View your total price
6. Place your order
7. Receive your receipt

---

#  Future Improvements

Possible future updates:

-  More pizza choices
-  Drinks and desserts menu
-  Payment simulation
-  Address input
-  Save previous orders
-  User accounts
-  Mobile version



#  Author

**Fiker Belay**

Computer Science Student

LinkedIn:
https://www.linkedin.com/in/fiker-belay/
part of the 100 days python
