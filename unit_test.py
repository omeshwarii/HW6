import unittest
from hw6 import calculate_effort_capacity, calculate_velocity

class TestEffortCapacityCalculation(unittest.TestCase):
#unit testing for feature A  
    def test_calculate_velocity(self):
        # Testing with inputs
        previous_sprints_points = [10, 20, 15]

        expected_velocity = sum(previous_sprints_points) / len(previous_sprints_points)

        # Calling the method 
        actual_velocity = calculate_velocity(previous_sprints_points)

        # Printing test case details
        print("\nTest Case: Calculating velocity method with valid input")
        print("Input: previous_sprints_points =", previous_sprints_points)
        print("Expected Output:", expected_velocity)
        print("Actual Output:", actual_velocity)

        # Checking if the actual result matches the expected result
        self.assertEqual(actual_velocity, expected_velocity)
        print("Result: PASS")
        print("-" * 70)

    def test_calculate_velocity_negative_points(self):       
        previous_sprints_points = [-10, 20, -30, 40, -50]
        expected_velocity = sum(previous_sprints_points) / len(previous_sprints_points)
        actual_velocity = calculate_velocity(previous_sprints_points)
        
        print("\nTest Case: Calculating velocity method with negative points")
        print("Input: previous_sprints_points =", previous_sprints_points)
        print("Expected Output:", expected_velocity)
        print("Actual Output:", actual_velocity)

        self.assertEqual(actual_velocity, expected_velocity)
        print("Result: PASS")
        print("-" * 70)

    def test_calculate_velocity_zero_points(self):
        previous_sprints_points = [0, 0, 0, 0, 0]
        expected_velocity = 0
        actual_velocity = calculate_velocity(previous_sprints_points)

        print("\nTest Case: test_calculate_velocity_zero_points")
        print("Input: previous_sprints_points =", previous_sprints_points)
        print("Expected Output:", expected_velocity)
        print("Actual Output:", actual_velocity)

        # Assert that the actual result matches the expected result
        self.assertEqual(actual_velocity, expected_velocity)
        print("Result: PASS")
        print("-" * 70)

#unit testing for feature B
    def test_effort_capacity_calculation(self):
        # Define test input data
        sprint_days = 10
        team_members = [
            {'name': 'John Doe', 'hours_per_day': 8, 'days_off': 2, 'days_for_ceremonies': 1},
            {'name': 'Jane Smith', 'hours_per_day': 7, 'days_off': 1, 'days_for_ceremonies': 2},
            {'name': 'Alice Johnson', 'hours_per_day': 9, 'days_off': 0, 'days_for_ceremonies': 1}
        ]

        expected_effort_hours = (8 * (sprint_days - 2 - 1)) + (7 * (sprint_days - 1 - 2)) + (9 * (sprint_days - 0 - 1))

        # Calling the method 
        actual_effort_hours = calculate_effort_capacity(sprint_days, team_members)

        # Print test case details
        print("\nTest Case: Testing effort capacity calculation for a team of 3 members")
        print("Input: sprint_days =", sprint_days)
        print("Input: team_members =", team_members)
        print("Expected Output:", expected_effort_hours)
        print("Actual Output:", actual_effort_hours)

        # checking if the actual result matches the expected result
        self.assertEqual(actual_effort_hours, expected_effort_hours)
        print("Result: PASS")
        print("-" * 70)

    def test_zero_hours_per_day(self):
        sprint_days = 5
        team_members = [{'name': 'Jane Smith', 'hours_per_day': 0, 'days_off': 0, 'days_for_ceremonies': 0}]
        expected_effort_hours = 0
        actual_effort_hours = calculate_effort_capacity(sprint_days, team_members)

        print("\nTest Case: Testing for zero hours per day")
        print("Input: sprint_days =", sprint_days)
        print("Input: team_members =", team_members)
        print("Expected Output:", expected_effort_hours)
        print("Actual Output:", actual_effort_hours)

        self.assertEqual(actual_effort_hours, expected_effort_hours)
        print("Result: PASS")
        print("-" * 70)

    def test_single_team_member(self):
        sprint_days = 5
        team_members = [{'name': 'John Doe', 'hours_per_day': 8, 'days_off': 1, 'days_for_ceremonies': 2}]
        expected_effort_hours = 8 * (sprint_days - 1 - 2)
        actual_effort_hours = calculate_effort_capacity(sprint_days, team_members)

        print("\nTest Case: Testing for single team member")
        print("Input: sprint_days =", sprint_days)
        print("Input: team_members =", team_members)
        print("Expected Output:", expected_effort_hours)
        print("Actual Output:", actual_effort_hours)

        self.assertEqual(actual_effort_hours, expected_effort_hours)
        print("Result: PASS")
        print("-" * 70)

if __name__ == '__main__':
    unittest.main()
