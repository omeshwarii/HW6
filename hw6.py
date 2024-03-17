# To Calculate  average velocityy
def calculate_velocity(previous_sprints_points):
    if not previous_sprints_points:
        return "No previous sprint points provided"
    return sum(previous_sprints_points) / len(previous_sprints_points)

# To Calculate effort-hour capacity per team and per person
def calculate_effort_capacity(sprint_days, team_members):
    total_effort_hours = 0
    for member in team_members:
        available_hours = member['hours_per_day'] * (sprint_days - member['days_off'] - member['days_for_ceremonies'])
        total_effort_hours += available_hours
        print(f"Available Effort-Hours for {member['name']}: {available_hours}")
    return total_effort_hours

# Prompts user to select Feature A or Feature B
selected_feature = input("Select Feature A or Feature B: ").lower()

if selected_feature == 'a':
    # Feature A:
    previous_sprints_points = input("Enter the number of previous sprints: ")

    if previous_sprints_points.isdigit():
        previous_sprints_points = int(previous_sprints_points)
        if previous_sprints_points > 0:
            sprint_points_list = []
            for i in range(previous_sprints_points):
                sprint_points = input(f"Enter points completed for sprint {i+1}: ")
                if sprint_points.isdigit():
                    sprint_points_list.append(int(sprint_points))
                else:
                    print("Invalid input for sprint points. Please enter numeric values.")
                    break
            else:
                average_velocity = calculate_velocity(sprint_points_list)
                print("Average Velocity:", average_velocity)
        else:
            print("There are no previous sprints to calculate velocity from.")
    else:
        print("Invalid input for the number of previous sprints. Please enter a valid numeric value.")

elif selected_feature == 'b':
    # Feature B: 
    sprint_days_input = input("Enter number of sprint days: ")
    if sprint_days_input.isdigit():
        sprint_days = int(sprint_days_input)
        if sprint_days > 0:
            num_team_members_input = input("Enter number of team members: ")
            if num_team_members_input.isdigit():
                num_team_members = int(num_team_members_input)
                if num_team_members > 0:
                    team_members = []
                    for _ in range(num_team_members):
                        member = {}
                        member['name'] = input("Enter name of team member: ")
                        hours_per_day_input = input(f"Enter hours per day for {member['name']}: ")
                        if hours_per_day_input.isdigit():
                            member['hours_per_day'] = float(hours_per_day_input)
                            member['days_off'] = int(input(f"Enter days off for {member['name']}: "))
                            member['days_for_ceremonies'] = int(input(f"Enter days committed to Sprint ceremonies for {member['name']}: "))
                            team_members.append(member)
                        else:
                            print(f"Invalid input for hours per day for {member['name']}. Please enter a valid numeric value.")
                            break
                    else:
                        available_effort_hours = calculate_effort_capacity(sprint_days, team_members)
                        print("Total Available Effort-Hours for Team:", available_effort_hours)
                else:
                    print("Number of team members must be greater than 0.")
            else:
                print("Invalid input for the number of team members. Please enter a valid numeric value.")
        else:
            print("Number of sprint days must be greater than 0.")
    else:
        print("Invalid input for sprint days. Please enter a valid numeric value.")

else:
    print("Invalid selection. Please select either Feature A or Feature B.")
