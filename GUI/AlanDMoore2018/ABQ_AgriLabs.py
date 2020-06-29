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

    # def grid(self, sticky=(tk.W + tk.E), **kwargs):
    #     super.grid(sticky=sticky, **kwargs)
    #
    # def get(self):
    #     try:
    #         if self.variable:
    #             return self.variable.get()
    #         elif type(self.input) == tk.Text:
    #             return self.input.get('1.0', tk.END)
    #         else:
    #             return self.input.get()
    #     except (TypeError, tk.TclError):
    #         return ''

class DataRecord(tk.Frame):
    """
    DocString goes here
    """


class Application(tk.TK):
    """
    Application root window
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello Tkinter")  # change the window title
        self.geometry("800x600")  # set the window size in pixels, in the format width x height
        self.resizable(width=False, height=False)  # setting to False any dimension, the window won't be resizable in
        # that dimension.


if __name__ == "__main__":
    app = Application()
    app.mainloop()