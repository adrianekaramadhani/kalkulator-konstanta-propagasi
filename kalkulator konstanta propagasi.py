import tkinter as tk
from tkinter import ttk
import math
import cmath
from convertKomponen import*

class ConstantsCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalkulator Konstanta Pada Saluran Transmisi")
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.master, text="Enter Component Values:")
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.entries = {}
        self.units = {}

        components = ["Induktansi", "Panjang Saluran", "Resistor", "Kapasitansi", "Konduktansi", "Frekuensi"]
        units_options = {
            "Induktansi":["pH", "nH", "uH", "mH", "H", "kH", "MH", "GH", "TH"],
            "Panjang Saluran":["km", "m", "cm", "mm"],
            "Resistor":["pΩ", "nΩ", "uΩ", "mΩ", "Ω", "kΩ", "MΩ", "GΩ", "TΩ"],
            "Kapasitansi":["pF", "nF", "uF", "mF", "F", "kF", "MF", "GF", "TF"],
            "Konduktansi":["pS", "nS", "uS", "mS", "S", "kS", "MS", "GS", "TS"],
            "Frekuensi":["pHz", "nHz", "uHz", "mHz", "Hz", "kHz", "MHz", "GHz", "TH"],
            }

        for i, component in enumerate(components):
            label = ttk.Label(self.master, text=f"{component}:")
            label.grid(row=i+1, column=0, padx=10, pady=5, sticky=tk.W)

            entry = ttk.Entry(self.master)
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.entries[component] = entry

            unit_combobox = ttk.Combobox(self.master, values=units_options[component])
            unit_combobox.grid(row=i+1, column=2, padx=10, pady=5)
            unit_combobox.set(units_options[component][0])
            self.units[component] = unit_combobox

        self.calculate_button = ttk.Button(self.master, text="Calculate", command=self.calculate_constants)
        self.calculate_button.grid(row=len(components)+1, column=0, columnspan=3, pady=10)

        self.result_frame = ttk.LabelFrame(self.master, text="Results")
        self.result_frame.grid(row=len(components)+2, column=0, columnspan=3, pady=10)

        self.result_table = ttk.Label(self.result_frame, text="")
        self.result_table.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)

    def calculate_constants(self):
        try:
            values = {}
            for component in self.entries:
                value = float(self.entries[component].get())
                unit = self.units[component].get()
                values[component] = (value, unit)

            convertRaks = convertResistor(*values["Resistor"])
            convertCaks = convertCapasitor(*values["Kapasitansi"])
            convertLaks = convertInduktor(*values["Induktansi"])
            convertGaks = convertKonduktansi(*values["Konduktansi"])
            convertF = convertFrekuensi(*values["Frekuensi"])
            convertS = convertKabel(*values["Panjang Saluran"])

            Laks = convertLaks / convertS
            Caks = convertCaks / convertS
            Gaks = convertGaks / convertS
            Raks = convertRaks / convertS
            omega = 2 * 3.14 * convertF

            if (omega * Caks > Gaks) and (omega * Laks > Raks):
                category = "Frekuensi Tinggi"
                zo = round(math.sqrt(Laks / Caks), 5)
                alpha = round((0.5 * (Raks * (math.sqrt((Caks / Laks))))) + (0.5 * (Gaks * (math.sqrt((Laks / Caks))))), 5)
                beta = round(omega * math.sqrt(Laks * Caks), 5)
            elif (Raks > omega * Laks and Gaks < 0.001):
                category = "Frekuensi Rendah"
                zo = cmath.sqrt(Raks / complex(omega * Caks))
                alpha = round(math.sqrt(omega * Caks * Raks / 2), 5)
                beta = round(math.sqrt(omega * Caks * Raks / 2), 5)
            else:
                category = "No Matching Category"
                zo = cmath.sqrt(complex(Raks , omega * Laks) / complex(Gaks , omega * Caks))
                if (Raks == 0 and Gaks == 0): 
                    alpha = 0
                else:
                    alpha = omega * math.sqrt(Laks + Caks)
                beta = omega * math.sqrt(Laks * Caks)
            
            gamma = cmath.sqrt(complex(Raks , omega * Laks) * complex(Gaks , omega * Caks))

            result_text = f"Category: {category}\nImpedansi Gelombang: {zo}\nKonstanta Peredaman: {alpha}\nKonstanta Phasa: {beta}\nKonstanta Propagasi: {gamma}"
            self.result_table.config(text=result_text)
        except ValueError:
            self.result_table.config(text="Invalid input. Please enter numeric values.")

def main():
    root = tk.Tk()
    app = ConstantsCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
