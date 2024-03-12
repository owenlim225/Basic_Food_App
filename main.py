import tkinter as tk
from datetime import datetime

class FoodKioskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Kiosk App")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        self.root.config(bg="#DC143C")

        # Left Frame for Customer Name and Order
        left_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
        left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Right Frame for Receipt
        right_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
        right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.customer_name = tk.StringVar()
        self.order_coffee = tk.IntVar()
        self.order_croissant = tk.IntVar()
        self.order_carbonara = tk.IntVar()
        self.discount = tk.IntVar()

        # Left Frame: Customer Name Entry and Order Checkbuttons
        tk.Label(left_frame, text="Welcome to:", font=("Arial", 14)).grid(row=0, column=0, pady=5)
        tk.Label(left_frame, text="TINDAHAN NI SHERWIN", font=("Arial", 14, "bold")).grid(row=0, column=1, pady=5)
        
        tk.Label(left_frame, text="Customer Name:").grid(row=1, column=0, sticky=tk.W)
        tk.Entry(left_frame, textvariable=self.customer_name).grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        tk.Label(left_frame, text="Order:").grid(row=2, column=0, sticky=tk.W)
        tk.Checkbutton(left_frame, text="Coffee (₱125.00)", variable=self.order_coffee).grid(row=3, column=0, sticky=tk.W)
        tk.Checkbutton(left_frame, text="Croissant (₱85.00)", variable=self.order_croissant).grid(row=4, column=0, sticky=tk.W)
        tk.Checkbutton(left_frame, text="Carbonara (₱250.00)", variable=self.order_carbonara).grid(row=5, column=0, sticky=tk.W)

        tk.Label(left_frame, text="Discount:").grid(row=7, column=0, sticky=tk.W)
        tk.Radiobutton(left_frame, text="5%", variable=self.discount, value=5).grid(row=8, column=0, sticky=tk.W)
        tk.Radiobutton(left_frame, text="10%", variable=self.discount, value=10).grid(row=8, column=1, sticky=tk.W)
        tk.Radiobutton(left_frame, text="15%", variable=self.discount, value=15).grid(row=8, column=2, sticky=tk.W)

        # Right Frame: Receipt
        self.receipt_text = tk.Text(right_frame, height=30, width=40, state='disabled')
        self.receipt_text.pack(padx=1, pady=1)
        self.receipt_text.insert(tk.END, "Welcome to Food Kiosk App\n\n")

        # Calculate Button
        tk.Button(left_frame, text="Calculate", command=self.calculate_total).grid(row=10, column=0, columnspan=2, pady=10)

    def calculate_total(self):
        total_cost = 0
        pre_total_cost = 0
        discount_to = f"Discount({self.discount.get()}%):"
        discounted_total_cost = 0

        if self.order_coffee.get():
            total_cost += 125.00
        if self.order_croissant.get():
            total_cost += 85.00
        if self.order_carbonara.get():
            total_cost += 250.00

        discount_percentage = self.discount.get() / 100
        pre_total_cost = total_cost
        total_cost -= total_cost * discount_percentage
        discounted_total_cost = pre_total_cost - total_cost
        

        customer_name = self.customer_name.get()    
        receipt = f"\n{'TINDAHAN NI SHERWIN':^40}\n{'UPHSL Mac Lab u':^40}\n{'Tel: #87000':^40}\n\n{'  Customer Name:':<15}{customer_name:>20}\n\n"

        receipt += "-" * 40 + "\n"  # Line separator
        receipt += f"{'CASH RECEIPT':^40}\n"
        receipt += "-" * 40 + "\n"  # Line separator
        
        if self.order_coffee.get():
            receipt += f"{'  Coffee': <17} { '₱125.00': >20}\n"
        if self.order_croissant.get():
            receipt += f"{'  Croissant': <17} { '₱ 85.00': >20}\n"
        if self.order_carbonara.get():
            receipt += f"{'  Carbonara': <17} { '₱250.00': >20}\n"
        
        total_cost = (f"₱{total_cost:.2f}")
        pre_total_cost = (f"₱{pre_total_cost:.2f}")
        discounted_total_cost = (f"₱ {discounted_total_cost:.2f}")
        
        
        receipt += "-" * 40 + "\n"  # Line separator
        
        
        receipt += f"  {discount_to: <18}{discounted_total_cost: >18}\n"
        receipt += f"{'  Sub total:':<18}{pre_total_cost: >20}\n"
        
        receipt += "-" * 40 + "\n"  # Line separator
        receipt += f"\n{'  Total Cost:':<18}{total_cost: >20}\n\n\n\n\n"
        receipt += f"{'ARIGATHANKS SA PAG BILI SAKIN!':^40}\n\n"
        receipt += f"{'█ ██ █ ██████ █ █ ███████ █ ████':^40}\n"  # ASCII barcode representation
        
        # Add date and time
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

root = tk.Tk()
app = FoodKioskApp(root)
root.mainloop()
