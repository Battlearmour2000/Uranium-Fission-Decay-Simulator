import tkinter as tk
from tkinter import ttk
import random
import math

class FissionVisualizer:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=800, height=600, bg="#f0f0f5")
        self.canvas.pack()

        self.uranium_atoms = []
        self.neutrons = []
        self.collision_count = 0  # Track the number of collisions

        self.create_controls()
        
        # Start the animation loop
        self.animate()

    def create_controls(self):
        # Apply modern theme for visual appeal
        style = ttk.Style(self.master)
        style.theme_use('clam')

        control_frame = ttk.Frame(self.master, padding="10")
        control_frame.pack()

        # Labels for neutron and collision count
        self.neutron_label = ttk.Label(control_frame, text="Neutrons: 0", font=("Arial", 10, "bold"))
        self.neutron_label.pack(side=tk.LEFT, padx=10)
        
        self.collision_label = ttk.Label(control_frame, text="Collisions: 0", font=("Arial", 10, "bold"))
        self.collision_label.pack(side=tk.LEFT, padx=10)
        
        # Input fields for number of atoms and layout options
        ttk.Label(control_frame, text="Number of Uranium Atoms:").pack(side=tk.LEFT, padx=5)
        self.atom_count_entry = ttk.Entry(control_frame, width=5)
        self.atom_count_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(control_frame, text="Layout:").pack(side=tk.LEFT, padx=5)
        self.layout_var = tk.StringVar(value="random")
        layout_options = ["random", "grid", "circle"]
        self.layout_menu = ttk.OptionMenu(control_frame, self.layout_var, *layout_options, command=self.update_layout_options)
        self.layout_menu.pack(side=tk.LEFT, padx=5)
        
        # Grid and Circle layout customization options
        self.grid_spacing_label = ttk.Label(control_frame, text="Grid Spacing:", font=("Arial", 8))
        self.grid_spacing_slider = ttk.Scale(control_frame, from_=20, to=100, orient=tk.HORIZONTAL)
        
        self.circle_radius_label = ttk.Label(control_frame, text="Circle Radius:", font=("Arial", 8))
        self.circle_radius_slider = ttk.Scale(control_frame, from_=50, to=300, orient=tk.HORIZONTAL)

        # Buttons for placing atoms and releasing neutron
        self.place_atoms_btn = ttk.Button(control_frame, text="Place Atoms", command=self.place_atoms)
        self.place_atoms_btn.pack(side=tk.LEFT, padx=10)
        
        self.release_btn = ttk.Button(control_frame, text="Release Neutron", command=self.release_neutron)
        self.release_btn.pack(side=tk.LEFT, padx=10)

    def update_layout_options(self, layout_type):
        # Display controls based on layout type
        self.grid_spacing_label.pack_forget()
        self.grid_spacing_slider.pack_forget()
        self.circle_radius_label.pack_forget()
        self.circle_radius_slider.pack_forget()

        if layout_type == "grid":
            self.grid_spacing_label.pack(side=tk.LEFT, padx=5)
            self.grid_spacing_slider.pack(side=tk.LEFT, padx=5)
        elif layout_type == "circle":
            self.circle_radius_label.pack(side=tk.LEFT, padx=5)
            self.circle_radius_slider.pack(side=tk.LEFT, padx=5)

    def update_labels(self):
        # Update neutron and collision count labels
        self.neutron_label.config(text=f"Neutrons: {len(self.neutrons)}")
        self.collision_label.config(text=f"Collisions: {self.collision_count}")

    def place_atoms(self):
        # Clear existing atoms and neutrons from the canvas
        self.canvas.delete("all")
        self.uranium_atoms.clear()
        self.neutrons.clear()
        self.collision_count = 0  # Reset collision count

        # Get atom count from the entry
        try:
            count = int(self.atom_count_entry.get())
        except ValueError:
            count = 0

        layout_type = self.layout_var.get()
        if layout_type == "random":
            self.place_random(count)
        elif layout_type == "grid":
            self.place_grid(count)
        elif layout_type == "circle":
            self.place_circle(count)
        
        # Update labels
        self.update_labels()

    def place_random(self, count):
        for _ in range(count):
            x, y = random.randint(50, 750), random.randint(50, 550)
            atom = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="dark blue", outline="blue")
            self.uranium_atoms.append({'id': atom, 'x': x, 'y': y, 'reacted': False})

    def place_grid(self, count):
        spacing = int(self.grid_spacing_slider.get())
        cols = int(math.sqrt(count))
        start_x, start_y = 50, 50

        for i in range(count):
            row, col = divmod(i, cols)
            x = start_x + col * spacing
            y = start_y + row * spacing
            if x > 750 or y > 550:
                break  # Stop if we go out of bounds
            atom = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="dark blue", outline="blue")
            self.uranium_atoms.append({'id': atom, 'x': x, 'y': y, 'reacted': False})

    def place_circle(self, count):
        radius = int(self.circle_radius_slider.get())
        center_x, center_y = 400, 300

        for i in range(count):
            angle = 2 * math.pi * i / count
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            atom = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="dark blue", outline="blue")
            self.uranium_atoms.append({'id': atom, 'x': x, 'y': y, 'reacted': False})

    def release_neutron(self):
        neutron_x, neutron_y = random.randint(50, 750), random.randint(50, 550)
        angle = random.uniform(0, 2 * math.pi)  # Random direction
        neutron = self.canvas.create_oval(neutron_x-2, neutron_y-2, neutron_x+2, neutron_y+2, fill="gray")
        self.neutrons.append({'id': neutron, 'x': neutron_x, 'y': neutron_y, 'angle': angle})

        # Update neutron count label
        self.update_labels()

    def animate(self):
        self.move_neutrons()
        self.master.after(50, self.animate)

    def move_neutrons(self):
        new_neutrons = []
        
        for neutron in self.neutrons:
            neutron['x'] += 3 * math.cos(neutron['angle'])
            neutron['y'] += 3 * math.sin(neutron['angle'])

            if not (0 <= neutron['x'] <= 800 and 0 <= neutron['y'] <= 600):
                self.canvas.delete(neutron['id'])
                continue  # Skip to the next neutron

            self.canvas.coords(neutron['id'], neutron['x']-2, neutron['y']-2, neutron['x']+2, neutron['y']+2)

            for atom in self.uranium_atoms:
                if not atom['reacted'] and self.check_collision(neutron, atom):
                    self.react_atom(atom)
                    self.canvas.delete(neutron['id'])
                    self.collision_count += 1  # Increment collision count
                    new_neutrons.extend(self.spawn_neutrons(atom['x'], atom['y']))
                    break
            else:
                new_neutrons.append(neutron)

        self.neutrons = new_neutrons
        self.update_labels()

    def check_collision(self, neutron, atom):
        distance = math.sqrt((neutron['x'] - atom['x'])**2 + (neutron['y'] - atom['y'])**2)
        return distance < 8

    def react_atom(self, atom):
        atom['reacted'] = True
        self.canvas.itemconfig(atom['id'], fill="light blue", outline="light blue")

    def spawn_neutrons(self, x, y):
        new_neutrons = []
        for _ in range(3):
            angle = random.uniform(0, 2 * math.pi)
            neutron = self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="gray")
            new_neutrons.append({'id': neutron, 'x': x, 'y': y, 'angle': angle})
        return new_neutrons

root = tk.Tk()
root.title("Uranium Fission Decay Simulator")
app = FissionVisualizer(root)
root.mainloop()
