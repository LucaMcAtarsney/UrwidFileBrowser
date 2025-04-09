import os
import urwid as u

PALETTE = [
    ("normal","white","black"),
    ("highlighted","black","yellow"),
    ("bg","white","black")
]

def handleinput(key):
    if key == "esc":
        path = os.path.dirname(current_path)
        open_directory(path)



def on_item_chosen(button,full_path):

    if os.path.isdir(full_path):
        open_directory(full_path)
    else:
        pass

def list_directory(path):

    # read in list of directories at path, handle permission error
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        items = []

    # create text and divider widget (top part)
    widgets = [u.Text(f"📁 {path}"), u.Divider()]

    # add button for each item
    for item in items:

        #joins item name to path with a /
        full_path = os.path.join(path,item)

        label = f"📁 {item}" if os.path.isdir(full_path) else f"📄 {item}"

        widgets.append(u.AttrMap(u.Button(label,on_press=on_item_chosen,user_data=full_path),"normal","highlighted"))

    # wraps the widgets in a listbox
    return u.ListBox(u.SimpleFocusListWalker(widgets))

def open_directory(path):
    global current_path

    body = u.LineBox(list_directory(path))
    padded = u.AttrMap(u.Padding(body,left=2,right= 2),"bg")
    current_path = path

    main_placeholder.original_widget = padded

current_path = "/Users/luca"
main_placeholder = u.WidgetPlaceholder(u.SolidFill(" "))
open_directory(current_path)
u.MainLoop(main_placeholder,palette=PALETTE,unhandled_input=handleinput).run()