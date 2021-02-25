# -*- coding: utf-8 -*-
"""

rcnobles
CPSC 223P-01
Mon Feb 22, 2021
rcnobles@csu.fullerton.edu

"""

import lists

# Print out all the school lunches on the menu, but substitute bratwurst 
# wherever you see hot dogs
# Use list comprehension. Just print the list directly so the output will
# include the brackets and quotations (['item 1', item 2' ... and so on])
new_school_lunches = [food_item if food_item != "hot dogs" else "bratwurst" for food_item in lists.school_lunches]
print(new_school_lunches)

# Use zip to iterate over two lists at the same time
# Print out questions and answers in a loop
# Format them: "What is your <question>? My <question> is <answer>."
#print(lists.questions)
#print(lists.answers)
q_and_a_tuple = tuple(zip(lists.questions, lists.answers))
for index in range(len(q_and_a_tuple)):
    print(f"What is your {q_and_a_tuple[index][0]}? My {q_and_a_tuple[index][0]} is {q_and_a_tuple[index][1]}")


# Manipulate the nested lists of sports teams to print all teams from New York
# and all teams from Los Angeles.  Just print the lists directly so the output will
# include the brackets and quotations (['team 1', team 2' ... and so on])
sports_teams = [lists.football_teams, lists.baseball_teams, lists.basketball_teams]
newyork_teams = [team for list in sports_teams for team in list if "New York" in team ]
lateams_teams = [team for list in sports_teams for team in list if "Los Angeles" in team ]
print(f"{newyork_teams}\n{lateams_teams}")
