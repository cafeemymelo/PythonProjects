"""Creatiing a better hello using tkninter. OOP example"""
import tkinter as tk
import tkinter.ttk as ttk


class HelloView(tk.Frame):  # the HelloView class is an inheritance of the tk.Frame class. It is subclassed from
    # tk.Frame! The tk.Frame class is used as container to the widgets! It is consider good practice to have only on
    # tk.TK instance and then only add child to this unique tk.TK instance as tk.Frames and tk.TopLevel.
    """
    GUI class for a simple hello world!
    """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(master=parent, *args, **kwargs)  # super constructor from Frame class! this way our HelloView class can
        # take the same arguments as the tk.Frame class! parent is passed here to bound the label to the tk.TK instance
        # (root window)
        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hello World!!")
        # creating the widgets

        name_label = ttk.Label(master=self, text="Name: ")
        name_entry = ttk.Entry(master=self, textvariable=self.name)  # the name_entry is bound to self.name variable!
        # every the ttk.Entry is altered, self.name is updated.

        ch_button = ttk.Button(master=self, text="Change", command=self.on_change)  # the command argument takes as
        # reference a Python function or method. The method or function passed this way is called callback.
        # The callback is called only when the button is clicked.

        hello_label = ttk.Label(self, textvariable=self.hello_string, font=("TkDefaultFont", 64), wraplength=600)
        # wraplength argument is used to specify the text length before it gets wraps to the next line

        # placing the widgets in the frame

        name_label.grid(row=0, column=0, sticky=tk.W)  # 'sticky' specify which side of the cell the widget should stick
        name_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        ch_button.grid(row=0, column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)
        # columnspan specify how many columns grid the widget will span.

        self.columnconfigure(1, weight=1)
        # specify to weight column 1 more the others

    def on_change(self):
        if self.name.get().strip():
            self.hello_string.set("Hello " + self.name.get())
        else:
            self.hello_string.set("Hello World!!")
            # I have to set the original back in the self.hello_string


class MyApplication(tk.Tk):
    """
    This class is created to be the base window for the application. This is not considered a good practice because
    should only exist one root window (unique tk.TK instance) and this way we could create many tk.TK instances in our
    main application
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello Tkinter")  # change the window title
        self.geometry("800x600")  # set the window size in pixels, in the format width x height
        self.resizable(width=False, height=False)  # setting to False any dimension, the window won't be resizable in
        # that dimension.

        HelloView(parent=self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
