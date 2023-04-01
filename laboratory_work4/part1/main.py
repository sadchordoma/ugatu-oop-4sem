import tkinter
from tkinter import Tk, Canvas, Checkbutton, X, Y

from tkinter import TOP, BOTTOM, BOTH

from CCircle import CCircle


window = Tk()
window.title("laboratory_work4")
window.geometry("700x700")
# width, height
window.minsize(400, 250)
window.maxsize(1920, 1080)


# whether is enabled ctrl or not
checkbox_is_enabled_ctrl = Checkbutton(text="Is enabled Ctrl")
# whether
checkbox_is_select_all_when_intersection = Checkbutton(window,
    text="Behavior when selecting\n"
    "intersected objects")
checkbox_is_enabled_ctrl.pack()
checkbox_is_select_all_when_intersection.pack()


# canvas - холст = rectangulaer area intended
# for drawing or other complex layouts
c = Canvas(window, width=1920, height=1080)
c.pack()


def print_coords(event):
    print(event.x, event.y)
all_circles = []


def create_circle(x, y, r, canvas, **kwargs):
    return canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)



def draw_circle(event, r = 25):
    found_closest = c.find_closest(event.x, event.y, r)
    print(found_closest)
    # print(found_closest)
    if not len(found_closest):
        new_circle = create_circle(event.x, event.y, r, c, fill="grey", outline="red", tag="circles")
        # print(new_circle)
        all_circles.append(new_circle)
        print(f"created with {event.x}, {event.y}")
    else:
        coords = c.coords(found_closest[0])
        x, y = coords[:2]   # get first 2 cords from (x1, y1, x2, y2)
        # print(cords)
        # print(x + r, y + r)
        x += r
        y += r
        print(x, y, event.x, event.y, x - event.x, y - event.y)
        print(abs(event.x - x), r)
        print(abs(event.y - y), r)
        if abs(event.x - x) < r and abs(event.y - y) < r:
            print("skipped")
        else:
            new_circle = create_circle(event.x, event.y, 25, c, fill="grey", outline="red", tag="circles")
            all_circles.append(new_circle)
            print(f"created with {event.x}, {event.y}")


# def select_circle(event):
#     item = c.find_closest(event.x, event.y)
#     current_color = c.itemcget(item, "fill")
#     if current_color == "none":
#         c.itemconfig(item[0], fill="black")
#     else:
#         c.itemconfig(item[0], fill=None)
#     print(item)


c.bind("<Button-1>", draw_circle, add="+")
# window.bind("<Button-1>", select_circle, add="+")

if __name__ == "__main__":
    window.mainloop()