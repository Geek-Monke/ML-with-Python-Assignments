import matplotlib.pyplot as plt
import numpy as np

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# a) Bar chart of the popularity of programming languages
fig, ax1 = plt.subplots(figsize=(2, 3))

colors = plt.cm.tab20.colors  # Get a set of colors from matplotlib
bars = ax1.bar(languages, popularity, color=colors[:len(languages)])
ax1.set_title('Popularity of Programming Languages')
ax1.set_xlabel('Programming Languages')
ax1.set_ylabel('Popularity (%)')
ax1.set_xticks(np.arange(len(languages)))
ax1.set_xticklabels(languages, rotation=45)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_edgecolor('black')
ax1.spines['bottom'].set_edgecolor('black')
#ax1.legend(bars, languages, title="Languages")

# Show the bar chart
plt.tight_layout()
plt.show()

# b) Grouped bar chart
# Grouping two consecutive elements
grouped_languages = ['Java & Python', 'PHP & JavaScript', 'C# & C++']
grouped_popularity = [
    popularity[0] + popularity[1],
    popularity[2] + popularity[3],
    popularity[4] + popularity[5]
]

fig, ax2 = plt.subplots(figsize=(2, 3))

# Create bar chart for the groups
bars = ax2.bar(grouped_languages, grouped_popularity, color=colors[:len(grouped_languages)])
ax2.set_title('Grouped Bar Chart of Programming Languages')
ax2.set_xlabel('Language Groups')
ax2.set_ylabel('Popularity (%)')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_edgecolor('black')
ax2.spines['bottom'].set_edgecolor('black')
#ax2.legend(bars, grouped_languages, title="Groups")

# Show the grouped bar chart
plt.tight_layout()
plt.show()

# c) Stacked bar chart for the groups
# Stacking the bars from grouped data
grouped_popularity_split = np.array([
    [popularity[0], popularity[1]],
    [popularity[2], popularity[3]],
    [popularity[4], popularity[5]]
])

fig, ax3 = plt.subplots(figsize=(2, 3))

# Create stacked bar chart
p1 = ax3.bar(grouped_languages, grouped_popularity_split[:, 0], color=colors[0], label='First in Group')
p2 = ax3.bar(grouped_languages, grouped_popularity_split[:, 1], bottom=grouped_popularity_split[:, 0], color=colors[1], label='Second in Group')

ax3.set_title('Stacked Bar Chart of Programming Languages Groups')
ax3.set_xlabel('Language Groups')
ax3.set_ylabel('Popularity (%)')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_edgecolor('black')
ax3.spines['bottom'].set_edgecolor('black')
ax3.legend(title="Group Components")

# Show the stacked bar chart
plt.tight_layout()
plt.show()
