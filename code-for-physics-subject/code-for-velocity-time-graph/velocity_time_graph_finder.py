# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Function for plotting velocity time graph
def plot_velocity_time_graph(time, velocity):
    plt.plot(time, velocity)
    plt.title('Velocity-Time Graph')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.show()

# Example for data
time = [0, 1, 4, 3, 5, 7]  # Time values
velocity = [0, 11, 21, 25, 5, 10]  # Velocity values

# Generate velocity-time graph
plot_velocity_time_graph(time, velocity)
