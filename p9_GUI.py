# Program: P9_GUI.py
# Name: Min Kim
# Date: April 22, 2026
# Description: Tkinter GUI for managing room measurements using the Measurement class.

import tkinter as tk
from Measurement import Measurement

current_m = Measurement()


def update_data():
    try:
        name = ent_name.get()
        f = int(ent_f.get())
        i = int(ent_i.get())

        current_m.set_label(name)
        current_m.set_feet(f)
        current_m.set_inches(i)

    
        lbl_res.config(text=str(current_m))
    except:
        lbl_res.config(text="Error: Enter valid data")

def show_meas_str():
    lbl_res.config(text=current_m.getMeasurementString())

def show_full():
    lbl_res.config(text=str(current_m))

def do_add_inch():
    current_m.addInches(1)
    lbl_res.config(text=str(current_m))

def show_total():
    val = current_m.getTotalInches()
    lbl_res.config(text=str(val))

def show_cm():
    val = current_m.getCentimeters()
    lbl_res.config(text=str(val))

def show_metric():
    lbl_res.config(text=current_m.getMetricString())


root = tk.Tk()
root.title("P9 Measurement GUI")
root.geometry("400x500")


tk.Label(root, text="Room Label:").pack(pady=2)
ent_name = tk.Entry(root)
ent_name.pack(pady=2)

tk.Label(root, text="Feet:").pack(pady=2)
ent_f = tk.Entry(root)
ent_f.pack(pady=2)

tk.Label(root, text="Inches:").pack(pady=2)
ent_i = tk.Entry(root)
ent_i.pack(pady=2)


lbl_res = tk.Label(root, text="Ready", fg="blue", pady=10)
lbl_res.pack()


tk.Button(root, text="Update Measurement", command=update_data).pack(fill="x", padx=50)
tk.Button(root, text="Show Measurement String", command=show_meas_str).pack(fill="x", padx=50)
tk.Button(root, text="Show Full Measurement", command=show_full).pack(fill="x", padx=50)
tk.Button(root, text="Add 1 Inch", command=do_add_inch).pack(fill="x", padx=50)
tk.Button(root, text="Show Total Inches", command=show_total).pack(fill="x", padx=50)
tk.Button(root, text="Show Centimeters", command=show_cm).pack(fill="x", padx=50)
tk.Button(root, text="Show Metric String", command=show_metric).pack(fill="x", padx=50)

root.mainloop()