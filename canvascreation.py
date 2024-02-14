import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Canvas Example")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg= 'yellow')
canvas.pack()

# Draw a line on the canvas
canvas.create_line(50, 50, 200, 50, fill="blue", width=2)

# Draw a rectangle on the canvas
canvas.create_rectangle(50, 100, 150, 200, fill="green")

# Draw an oval on the canvas
canvas.create_oval(200, 100, 300, 200, fill="red")

# Add text to the canvas
canvas.create_text(250, 250, text="Hello, Canvas!", fill="black", font=("Helvetica", 14))

# Start the main event loop
root.mainloop()
  

  ###########################
import tkinter as tk

class MyCanvas:
    def __init__(self, width, height, bg_color="white"):
        self.root = tk.Tk()
        self.root.title("Canvas Example")

        self.width = width
        self.height = height
        self.bg_color = bg_color

        # Create a Canvas widget
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg=self.bg_color)
        self.canvas.pack()

    def draw_rectangle(self, x1, y1, x2, y2, fill_color="blue"):
        # Draw a rectangle on the canvas
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

    def run(self):
        # Start the main event loop
        self.root.mainloop()

# Example usage
if __name__ == "__main__":
    # Create an instance of MyCanvas with width=400, height=300, and background color "lightgray"
    canvas_instance = MyCanvas(width=400, height=300, bg_color="lightgray")

    # Draw a rectangle on the canvas
    canvas_instance.draw_rectangle(50, 50, 150, 150, fill_color="green")

    # Start the GUI application
    canvas_instance.run()
