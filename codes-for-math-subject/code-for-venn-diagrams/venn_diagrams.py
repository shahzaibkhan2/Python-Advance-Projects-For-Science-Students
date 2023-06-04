# Import necessary modules
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define the sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}

# Create the Venn diagram
venn = venn3([set1, set2, set3], set_labels=('Set 1', 'Set 2', 'Set 3'))

# Customize the diagram and its optional
venn.get_label_by_id('100').set_text('Set 1')
venn.get_label_by_id('010').set_text('Set 2')
venn.get_label_by_id('001').set_text('Set 3')

# Display the diagram
plt.title("Venn Diagram")
plt.show()
