# Calculate average velocity
def calculate_velocity(previous_sprints_points):
    if not previous_sprints_points:
        return 0
    return sum(previous_sprints_points) / len(previous_sprints_points)

# Feature A: Allows user to input previous sprint points
previous_sprints_points = []
num_previous_sprints = int(input("Enter the number of previous sprints: "))
for i in range(num_previous_sprints):
    sprint_points = int(input(f"Enter points completed for sprint {i+1}: "))
    previous_sprints_points.append(sprint_points)


average_velocity = calculate_velocity(previous_sprints_points)
print("Average Velocity:", average_velocity)


# Feature B: Allows user to input number of sprint days and team member details
sprint_days = int(input("Enter number of sprint days: "))
team_members = []
num_team_members = int(input("Enter number of team members: "))

for _ in range(num_team_members):
    member = {}
    member['name'] = input("Enter name of team member: ")
    member['hours_per_day'] = float(input("Enter hours per day for team member: "))
    member['days_off'] = int(input("Enter days off for team member: "))
    member['days_for_ceremonies'] = int(input("Enter days committed to Sprint ceremonies: "))
    team_members.append(member)

