# Command-History

Command History is a pice of code, wich allow you to extend your apllication with a command History similar to the command history in a bash.
If you are planing to use the arrow keys to scroll trough the command history (like it is implementet in a bash) bind the method `read_backward()` with the arrow up key and bind the method `read_forward()` with the arrow down key.

# Documentation

## Methods

`__init__(size)`

__Parameters__
size : _int_
Define the maximum number, of elements wich can be stored in the command history.
___

`add_item(item)`

Add a srtring item to the command history. If the given item is equal to the last stored item it will not be stored in the history. If the history is full the next item will overwrite the oldest item.

__Parameters__
item : _str_
item wich will be added
___

`read_backward()`

Going one time step backwards and returning the item (at this time step). The action of going backwards will stop if the oldest item in the history is reached. If the oldest item is reached the return value will be this item. If the hsitory is empty the methode will return an empty string.

__Returns__
_str_
Element at the specific time stamp.


___

`read_forward()`

Going on time step forward and returning the item (at this time step). The action of going forward will stop if the newest item is selected. If the newest item is selected the method will return an empty string. If the method read_backward() wasent called at least once before the methode will also return an empty string. And if the history is empty it will also return an empty string.

__Returns__
_str_
Element at the specific time stamp.

___

`clear()`

Clear the content of the history and reset all internal states of the class instance.

# Example

The follwing example implement a primitiv terminal with tkinter. If you extend the example with the modul pyserial you can use it as a simple serial terminal.

```python
from tkinter import*
from tkinter import ttk
import sys
sys.path.append("..")
from src import cmd_history

cmd_hist = cmd_history.CMD_History(5)

window = Tk()

scroll_frame = Frame(window)
scroll_frame.pack(side="top")
scroll_y = Scrollbar(scroll_frame)
scroll_y.pack(fill="y", side="right")
listbox = Listbox(scroll_frame, height=30, width=10)
listbox.pack(side="top")
scroll_y["command"] = listbox.yview
listbox["yscrollcommand"] = scroll_y.set
entry = Entry(window, width=10)
entry.pack()



def enter(para):
    listbox.insert(END, entry.get())
    cmd_hist.add_item(entry.get())
    entry.delete(0, END)

def arrow_up(para):
    item = cmd_hist.read_backward()
    if item != "":
        entry.delete(0, END)
        entry.insert(END, item)

def arrow_down(para):
    item = cmd_hist.read_forward()
    if item != "":
        entry.delete(0, END)
        entry.insert(END, item)

entry.bind("<Return>", enter)
entry.bind("<Up>", arrow_up)
entry.bind("<Down>", arrow_down)

window.mainloop()
```