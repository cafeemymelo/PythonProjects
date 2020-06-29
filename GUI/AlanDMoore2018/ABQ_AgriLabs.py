import tkinter as tk
import tkinter.ttk as ttk


# Start coding here

class LabelInput(tk.Frame):
    """A widget containing a label and input together"""

    def __init__(self, parent, label="", input_class=ttk.Entry, input_var=None, input_args=None, label_args=None,
                 *args, **kwargs):
        super.__init__(master=parent, *args, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = input_var

        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
            input_args["text"] = label
            input_args["variable"] = input_var
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
            input_args["textvariable"] = input_var

        self.input = input_class(self, **input_args)
        self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))

        self.columnconfigure(0, weight=1)

    def grid(self, sticky=(tk.W + tk.E), **kwargs):
        super.grid(sticky=sticky, **kwargs)

    def get(self):
        try:
            if self.variable:
                return self.variable.get()
            elif type(self.input) == tk.Text:
                return self.input.get('1.0', tk.END)
            else:
                return self.input.get()
        except (TypeError, tk.TclError):
            return ''


class DataRecordForm(tk.Frame):
    """
    DocString goes here
    """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.inputs = {}  # dictionary to keep track of input widgets
        # this label frame will be the container for each group of widgets! All of then will be in the same parent
        # frame and appear at the same time in the same window but separated into smaller groups.
        recordinfo = tk.LabelFrame(self, text="Record Information")  # this label will be passed as parent widget to all
        # the inputs in the record information group
        # Line 1
        self.inputs['Date'] = LabelInput(recordinfo, "Date", input_var=tk.StringVar())
        self.inputs['Date'].grid(row=0, column=0)

        self.inputs['Time'] = LabelInput(recordinfo, "Time", input_class=ttk.Combobox, input_var=tk.StringVar(),
                                         input_args={"values": ["8:00", "12:00", "16:00", "20:00"]})
        self.inputs['Time'].grid(row=0, column=1)

        self.inputs['Technician'] = LabelInput(recordinfo, "Technician", input_var=tk.StringVar())
        self.inputs['Technician'].grid(row=0, column=2)
        # Line 2
        self.inputs['Lab'] = LabelInput(recordinfo, "Lab", input_class=ttk.Combobox, input_var=tk.StringVar(),
                                        input_args={"values": ["A", "B", "C", "D", "E"]})
        self.inputs['Lab'].grid(row=1, column=0)
        self.inputs['Plot'] = LabelInput(recordinfo, "Plot", input_class=ttk.Combobox, input_var=tk.StringVar(),
                                         input_args={"values": list(range(1, 21))})
        self.inputs['Plot'].grid(row=1, column=1)
        self.inputs['Seed Sample'] = LabelInput(recordinfo, "Seed Sample", input_var=tk.StringVar())
        self.inputs['Seed Sample'].grid(row=1, column=2)

        recordinfo.grid(row=0, column=0, sticky=(tk.W + tk.E))

        # Environment Data
        environmentinfo = tk.LabelFrame(self, text="Environment Data")
        self.inputs['Humidity'] = LabelInput(environmentinfo, "Humidity (g/m³)", input_class=ttk.Spinbox,
                                             input_var=tk.DoubleVar(),
                                             input_args={"from_": 0.5, "to": 52.0, "increment": 0.01})
        self.inputs['Humidity'].grid(row=0, column=0)
        self.inputs['Equipment Fault'] = LabelInput(environmentinfo, "Equipment Fault", input_class=ttk.Combobox,
                                                    input_var=tk.BooleanVar())
        self.inputs['Equipment Fault'].grid(row=1, column=0, columnspan=3)

        # plant information
        plantinfo = tk.LabelFrame(self, text="Plant Data")
        self.inputs['Plants'] = LabelInput(plantinfo, "Plants", input_class=ttk.Spinbox, input_var=tk.IntVar(),
                                           input_args={"from_": 0, "to": 20})
        self.inputs['Plants'].grid(row=0, column=0)

        self.inputs['Blossoms'] = LabelInput(plantinfo, "Blossoms", input_class=ttk.Spinbox, input_var=tk.IntVar(),
                                             input_args={"from_": 0, "to": 1000})
        self.inputs['Blossoms'].grid(row=0, column=1)

        self.inputs['Fruit'] = LabelInput(plantinfo, "Fruit", input_class=ttk.Spinbox, input_var=tk.IntVar(),
                                          input_args={"from_": 0, "to": 1000})
        self.inputs['Fruit'].grid(row=0, column=2)
        self.inputs['Min height'] = LabelInput(plantinfo, "Min height", input_class=ttk.Spinbox,
                                               input_var=tk.DoubleVar(),
                                               input_args={"from_": 0, "to": 1000})
        self.inputs['Min height'].grid(row=1, column=0)
        self.inputs['Max height'] = LabelInput(plantinfo, "Max height", input_class=ttk.Spinbox,
                                               input_var=tk.DoubleVar(),
                                               input_args={"from_": 0, "to": 1000})
        self.inputs['Max height'].grid(row=1, column=0)
        self.inputs['Median height'] = LabelInput(plantinfo, "Median height", input_class=ttk.Spinbox,
                                                  input_var=tk.DoubleVar(),
                                                  input_args={"from_": 0, "to": 1000})
        self.inputs['Median height'].grid(row=1, column=0)

        # Note section
        self.inputs['Notes'] = LabelInput(self, "Notes", input_class=tk.Text, input_args={"width": 75, "height": 10})
        self.inputs['Notes'].grid(sticky=tk.W, row=3, column=0)
        self.reset()

    def get(self):
        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def reset(self):
        for widget in self.inputs.values():
            widget.set('')


class Application(tk.TK):
    """
    Application root window
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("ABQ Data Entry Application")  # change the window title
        self.resizable(width=False, height=False)  # setting to False any dimension, the window won't be resizable in
        # that dimension.
        ttk.Label(self, text="ABQ Data Entry Application", font=("TkDefaultFont", 16)).grid(row=0)
        self.recordform = DataRecordForm(self)
        self.recordform.grid(row=1, padx=10)
        self.savebutton = ttk.Button(self, text="Save", command=self.on_save)
        self.savebutton.grid(sticky=tk.E, row=2, padx=10)

        # status bar
        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self, textvariable=self.status)
        self.statusbar.grid(sticky=(tk.W + tk.E), row=3, padx=10)

    def on_save(self):
        pass


if __name__ == "__main__":
    app = Application()
    app.mainloop()
