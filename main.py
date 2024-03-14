import tkinter as tk
from datetime import datetime

class FoodKioskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Kiosk App")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        self.root.config(bg="#DC143C")

        # Left Frame to for Customer Name and Order
        self.left_frame = tk.Frame(root, bd=5, relief=tk.GROOVE, bg="#FFE4E1")  # Change background color
        self.left_frame.place(x=20, y=20, width=370, height=460)

        # Right Frame to for Receipt
        self.right_frame = tk.Frame(root, bd=0, relief=tk.GROOVE, bg="#FFE4E1")  # Change background color
        self.right_frame.place(x=410, y=20, width=370, height=460)

        self.customer_name = tk.StringVar()
        self.order_quantities = {
            "Coffee": tk.IntVar(),
            "Croissant": tk.IntVar(),
            "Carbonara": tk.IntVar()
        }
        self.discount = tk.IntVar()

        # Left Frame: Customer Name Entry and Order Checkbuttons
        tk.Label(self.left_frame, text="Welcome to:", font=("Arial", 14), anchor="center", bg="#FFE4E1").place(x=10, y=10, width=350)  # Change font and background color
        tk.Label(self.left_frame, text="TINDAHAN NI SHERWIN", font=("Arial", 14, "bold"), anchor="center", bg="#FFE4E1").place(x=10, y=40, width=350)  # Change font and background color

        tk.Label(self.left_frame, text="Customer Name:", bg="#FFE4E1").place(x=10, y=80)
        tk.Entry(self.left_frame, textvariable=self.customer_name, bg="white").place(x=130, y=80, width=200)  # Change entry background color

        tk.Label(self.left_frame, text="Menu:", anchor="center", bg="#FFE4E1").place(x=10, y=120, width=350)

        self.create_food_item("Coffee", "₱125.00", 140)
        self.create_food_item("Croissant", "₱85.00", 170)
        self.create_food_item("Carbonara", "₱250.00", 200)

        tk.Label(self.left_frame, text="Discount:", anchor="center", bg="#FFE4E1").place(x=10, y=260, width=350)
        tk.Radiobutton(self.left_frame, text="0%", variable=self.discount, value=0, bg="#FFE4E1").place(x=80, y=280)
        tk.Radiobutton(self.left_frame, text="5%", variable=self.discount, value=5, bg="#FFE4E1").place(x=130, y=280)
        tk.Radiobutton(self.left_frame, text="10%", variable=self.discount, value=10, bg="#FFE4E1").place(x=180, y=280)
        tk.Radiobutton(self.left_frame, text="15%", variable=self.discount, value=15, bg="#FFE4E1").place(x=230, y=280)

        # Right Frame: Receipt
        self.receipt_text = tk.Text(self.right_frame, height=30, width=40, state='disabled')
        self.receipt_text.place(x=5, y=5)
        self.receipt_text.insert(tk.END, "Welcome to Food Kiosk App\n\n")

        # Calculate Button
        tk.Button(self.left_frame, text="Check out", font=("Arial", 12, "bold"), command=self.calculate_total, bg="#39FF14", fg="black").place(x=140, y=400)  # Change button color

        # Start changing background color
        self.change_bg_color()

    def create_food_item(self, item_name, price, y_position):
        tk.Label(self.left_frame, text=f"{item_name} {price}", anchor="w", bg="#FFE4E1").place(x=60, y=y_position)  # Change background color
        tk.Button(self.left_frame, text="-", command=lambda: self.decrease_quantity(item_name), anchor="w", bg="#FF3131").place(x=200, y=y_position)  # Change background color
        tk.Label(self.left_frame, textvariable=self.order_quantities[item_name], bg="#FFE4E1").place(x=230, y=y_position)  # Change background color
        tk.Button(self.left_frame, text="+", command=lambda: self.increase_quantity(item_name), anchor="w", bg="#39FF14").place(x=260, y=y_position)  # Change background color

    def increase_quantity(self, item_name):
        current_quantity = self.order_quantities[item_name].get()
        self.order_quantities[item_name].set(current_quantity + 1)

    def decrease_quantity(self, item_name):
        current_quantity = self.order_quantities[item_name].get()
        if current_quantity > 0:
            self.order_quantities[item_name].set(current_quantity - 1)

    def calculate_total(self):
        total_cost = 0
        pre_total_cost = 0
        discount_to = f"Discount({self.discount.get()}%):"
        discounted_total_cost = 0

        for item_name, quantity in self.order_quantities.items():
            if quantity.get() > 0:
                if item_name == "Coffee":
                    total_cost += quantity.get() * 125.00
                elif item_name == "Croissant":
                    total_cost += quantity.get() * 85.00
                elif item_name == "Carbonara":
                    total_cost += quantity.get() * 250.00


        #easy to call sa receipt
        discount_percentage = self.discount.get() / 100
        pre_total_cost = total_cost
        total_cost -= total_cost * discount_percentage
        discounted_total_cost = pre_total_cost - total_cost


        #Start ng receipt
        customer_name = self.customer_name.get()
        receipt = f"\n{'TINDAHAN NI SHERWIN':^40}\n{'UPHSL Mac Lab u':^40}\n{'Tel: #87000':^40}\n\n{'  Customer Name:':<15}{customer_name:>20}\n\n"

        receipt += "-" * 40 + "\n"  # Line separator
        receipt += f"{'CASH RECEIPT':^40}\n"
        receipt += "-" * 40 + "\n"  # Line separator

        for item_name, quantity in self.order_quantities.items():
            if quantity.get() > 0:
                receipt += f"{'  ' + item_name:<17} { '₱{:.2f}'.format(quantity.get() * self.get_item_price(item_name)): >20}\n"

        total_cost = (f"₱{total_cost:.2f}")
        pre_total_cost = (f"₱{pre_total_cost:.2f}")
        discounted_total_cost = (f"₱{discounted_total_cost:.2f}")

        receipt += "-" * 40 + "\n"  # Line separator

        receipt += f"  {discount_to: <18}{discounted_total_cost: >18}\n"
        receipt += f"{'  Sub total:':<18}{pre_total_cost: >20}\n"

        receipt += "-" * 40 + "\n"  # Line separator
        
        receipt += f"\n{'  Total Cost:':<18}{total_cost: >20}\n\n\n"
        receipt += f"{'ARIGATHANKS SA PAG SHOPPING W/ US!':^40}\n\n"
        receipt += f"{'█ ██ █  ██████ █ █ ███████ █ ████':^40}\n"  # kunyare bar code
        
        # Add date and time sa dulo ng receipt
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        receipt += f"{date_time:^40}\n\n"
        receipt += f"{'*** CUSTOMER COPY ***':^40}"



        # Enable receipt_text to insert
        self.receipt_text.config(state='normal')
        self.receipt_text.delete(1.0, tk.END)
        self.receipt_text.insert(tk.END, receipt)
        
        # Disable receipt_text to make it uneditable
        self.receipt_text.config(state='disabled')

    #price ng menu
    def get_item_price(self, item_name):
        if item_name == "Coffee":
            return 125.00
        elif item_name == "Croissant":
            return 85.00
        elif item_name == "Carbonara":
            return 250.00


    #Para iba iba kulay ng backgruond
    def change_bg_color(self):
        colors = ['#DC143C', '#FFA500', '#00FFFF', '#FF69B4', '#00FF7F', '#FFD700']  # List of colors to cycle through
        self.root.config(bg=colors[0])  # Initial background color

        def next_color(index):
            self.root.config(bg=colors[index])
            index = (index + 1) % len(colors)
            self.root.after(1000, next_color, index)  # Change color every 1000 milliseconds (1 second)

        next_color(1)

root = tk.Tk()
app = FoodKioskApp(root)
root.mainloop()
