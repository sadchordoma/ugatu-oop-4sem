from tkinter import Tk, Canvas, Checkbutton, BooleanVar

from CCircle import CCircle, R


window = Tk()
window.title("laboratory_work4")
# width, height
window.geometry("700x700")
window.minsize(400, 250)
window.maxsize(1920, 1080)

def state_checkbox_ctrl():
    checkbox_is_enabled_ctrl["text"] = "Ctrl is pressed"
    if var_checkbox_ctrl.get():
        checkbox_is_enabled_ctrl.select()
        return True
    checkbox_is_enabled_ctrl.deselect()
    return False

def state_checkbox_intersection():
    checkbox_is_select_all_when_intersection["text"] = "Select all when there are\n" \
                                                       "crossed elements"
    if var_checkbox_intersection.get():
        checkbox_is_select_all_when_intersection.select()
        return True
    checkbox_is_select_all_when_intersection.deselect()
    return False


var_checkbox_ctrl = BooleanVar()
var_checkbox_ctrl.set(False)
# whether is enabled ctrl or not
checkbox_is_enabled_ctrl = Checkbutton(
    text="Is pressed Ctrl", variable=var_checkbox_ctrl,
    onvalue=1, offvalue=0, command=state_checkbox_ctrl
)

var_checkbox_intersection = BooleanVar()
var_checkbox_intersection.set(False)
# whether
checkbox_is_select_all_when_intersection = Checkbutton(
    text="Behavior when selecting""\n""intersected objects",
    variable=var_checkbox_intersection,
    onvalue=1, offvalue=0, command=""
)
checkbox_is_enabled_ctrl.grid(column=0, row=0, ipadx=10, ipady=10)
checkbox_is_select_all_when_intersection.grid(row=0, column=1, ipadx=10, ipady=10)

# canvas - холст = rectangulaer area intended
# for drawing or other complex layouts
canvas = Canvas(window, width=1920, height=1080)
canvas.grid(row=1, column=0, rowspan=2, columnspan=2)


def print_cords(event):
    print(event.x, event.y)


all_circles = []
last_added_element_ind = 0


def validation(event, canvas):
    found_closest = canvas.find_closest(event.x, event.y)
    if not found_closest:
        return False
    else:
        cords = canvas.coords(found_closest[0])
        x, y = cords[:2]  # get first 2 cords from (x1, y1, x2, y2)
        x += R
        y += R
        if abs(event.x - x) < R and abs(event.y - y) < R:
            print("skipped")
            return found_closest
        # else
        return False


def select(found_closest, canvas):
    canvas.itemconfig(found_closest, outline="red", tag="selected")


def select_or_disselect(found_closest, canvas):
    if canvas.itemcget(found_closest, "outline") == "red":
        diselect(found_closest, canvas)
    else:
        select(found_closest, canvas)


def diselect(found_closest, canvas):
    canvas.itemconfig(found_closest, outline="", tag="not_selected")


def select_or_draw(event, canvas=canvas):
    found_closest = validation(event, canvas)
    # Block new drawings while ctrl or interselection
    if state_checkbox_ctrl():
        select_while_ctrl(event, canvas)
        return
    if state_checkbox_intersection():
        select_while_ctrl(event, canvas)
        return
    if found_closest:
        # if i wanna have opportunity to draw new circle while was selecting
        # if state_checkbox_ctrl():
        #     select_while_ctrl(event, canvas)
        #     return
        # if state_checkbox_intersection():
        #     select_while_ctrl(event, canvas)
        #     return
        select_or_disselect(found_closest, canvas)
    else:
        canvas.itemconfigure("selected", tag="not_selected", outline="")
        new_circle = CCircle(event.x, event.y)
        new_circle.draw(event, canvas)
        all_circles.append(new_circle)

def select_diselect_while_ctrl(event, canvas=canvas):
    list_found_closest = canvas.find_enclosed(
        event.x - 3 * R, event.y - 3 * R, event.x + 3 * R, event.y + 3 * R
    )
    for item in list_found_closest:
        select_or_disselect(item, canvas)
def select_while_ctrl(event, canvas=canvas):
    list_found_closest = canvas.find_enclosed(
        event.x - 3 * R, event.y - 3 * R, event.x + 3 * R, event.y + 3 * R
    )
    for item in list_found_closest:
        select(item, canvas)

def diselect_while_ctrl(event, canvas=canvas):
    list_found_closest = canvas.find_enclosed(
        event.x - 3 * R, event.y - 3 * R, event.x + 3 * R, event.y + 3 * R
    )
    for item in list_found_closest:
        diselect(item, canvas)

def prints(event):
    print(event)
    print(dir(event))
def delete_selected_circles(event):
    canvas.delete("selected")

def get_data(event):
    print(state_checkbox_intersection())
    print(state_checkbox_ctrl())


window.bind("<Button-1>", select_or_draw)
window.bind("<Delete>", delete_selected_circles)
window.bind("<Button-3>", get_data)
window.bind("<Control-Button-1>", select_while_ctrl)
window.mainloop()
# window.bind("<Button-1>", select_circle, add="+")
