"""main.py

Author: Elijah Barrett
Date: July 11, 2019

This program's purpose is to plot each OMSCS course's Average Difficulty vs Average Rating and
Average Work vs Average Rating.

List = [(Course, Work, Difficulty, Rating)]

"""

import matplotlib.pyplot as plt

courses = [
    ('IIS', 8.763, 2.372, 3.913),
    ('GIOS', 17.645, 3.618, 4.442),
    ('AOS', 15.634, 4.141, 4.4),
    ('SCS', 0, 0, 0),
    ('CN', 8.268, 2.504, 3.634),
    ('NS', 12.829, 3.061, 2.902),
    ('ICPSS', 0, 0, 0),
    ('ISL', 0, 0, 0),
    ('HPCA', 12.415, 3.736, 4.061),
    ('ESO', 16.182, 3.727, 3.227),
    ('SDP', 8.982, 2.359, 3.679),
    ('SAD', 13.308, 2.959, 3.449),
    ('SAT', 12.482, 3.398, 3.291),
    ('DBSCD', 10.298, 2.583, 3.127),
    ('IHI', 6.473, 1.955, 3.023),
    ('ETF', 13.544, 2.797, 4.123),
    ('CP', 12.462, 2.907, 3.922),
    ('CV', 20.505, 4.027, 4.446),
    ('IGA', 19.754, 4.217, 4.261),
    ('AI', 23.22, 4.307, 4.273),
    ('HCI', 11.531, 2.594, 4.333),
    ('KBAI', 13.332, 3.2, 3.725),
    ('RAI', 12.841, 3.195, 3.802),
    ('CPD', 0, 0, 0),
    ('ML', 20.532, 4.22, 3.928),
    ('RL', 21.548, 4.087, 3.907),
    ('ML4T', 10.316, 2.514, 4.302),
    ('CTP', 27.571, 4.4, 4)
]

course_name = [w for (w, x, y, z) in courses]
average_work = [x for (w, x, y, z) in courses]
average_difficulty = [y for (w, x, y, z) in courses]
average_rating = [z for (w, x, y, z) in courses]

fig = plt.figure()
plt.scatter(average_rating, average_difficulty)
plt.plot([2, 3, 4, 5], [2, 3, 4, 5])
for i, txt in enumerate(course_name):
    plt.annotate(txt, (average_rating[i], average_difficulty[i]))
plt.title('Average Rating vs Average Difficulty')
plt.xlabel('Average Student Rating')
plt.ylabel('Average Difficulty')
fig.show()
#fig.savefig('rating_vs_difficulty.png')

fig2 = plt.figure()
plt.scatter(average_rating, average_work)
for i, txt in enumerate(course_name):
    plt.annotate(txt, (average_rating[i], average_work[i]))
plt.title('Average Rating vs Average Workload')
plt.xlabel('Average Student Rating')
plt.ylabel('Average Workload per week')
fig2.show()
#fig3.savefig('rating_vs_workload.png')

fig3 = plt.figure()
plt.scatter(average_difficulty, average_work)
for i, txt in enumerate(course_name):
    plt.annotate(txt, (average_difficulty[i], average_work[i]))
plt.title('Average Difficulty vs Average Workload')
plt.xlabel('Average Difficulty')
plt.ylabel('Average Workload per week')
fig3.show()
#fig4.savefig('difficulty_vs_workload.png')

