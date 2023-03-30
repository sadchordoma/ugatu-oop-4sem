from tkinter import *

window = Tk()
window.title("laboratory_work4")
window.geometry("700x700")
# width, height
window.minsize(400, 250)
window.maxsize(1920, 1080)

# canvas - холст = rectangulaer area intended
# for drawing or other complex layouts
c = Canvas(window, width=1920, height=1080)
c.pack()

def print_coords(event):
    print(event.x, event.y)
all_circles = []
def draw_circle(event):
    all_circles.append(c.create_oval(event.x,event.y,event.x + 50, event.y + 50))
    print(f"created with {event.x}, {event.y}")
def select_circle(event):
    item = c.find_closest(event.x, event.y)
    current_color = c.itemcget(item, "fill")
    if current_color == "white":
        c.itemconfig(item[0], fill="black")
    else:
        c.itemconfig(item[0], fill="white")
    print(item)

window.bind("<Button-1>", draw_circle, add="+")
window.bind("<Button-1>", select_circle, add="+")



if __name__ == "__main__":
    window.mainloop()