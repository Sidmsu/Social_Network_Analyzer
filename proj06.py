#Algorithm
# This project creates a Python program to analyze social network data, focusing on relationships between individuals on two platforms:
# X and Facebook. The analysis involves identifying the most mutual friends across platforms,
# calculating the percentage of people without shared friends, identifying individual social connections,
# and detecting triangular friendships within and between networks.
# Processing social network data from CSV and TXT files.
# Development of functions for opening files, reading and parsing social network data, and performing various analyses.
# Use data structures such as sets and dictionaries to manage data efficiently.
# An interactive menu allows users to select various types of social network analyses.
# Calculation of percentages and counts using social network connections.
# When the program runs, it will prompt you for the names of the files containing the social network data.
# Users can interact with the program using a menu to select the type of analysis to be performed.
# The program gracefully handles file reading errors, prompting the user to enter file names again if they cannot be found.
# The program also handles invalid user input, prompting the user to enter a valid choice.
# The program uses the following functions:
# open_file(prompt): Prompts the user for a file name and opens the file.
# read_names_file(): Reads a file containing names and assigns each name an ID.
# read_friends_file(network_name, names_to_ids): Reads a file containing friends and assigns each friend to a user ID.
# find_max_intersection(friends_data_x, friends_data_fb): Finds the maximum number of mutual friends between X and Facebook.
# calculate_no_shared_percentage(x_data, fb_data): Calculates the percentage of people with no shared friends between X and Facebook.
# display_individual_info(names_to_ids, ids_to_names, x_data, fb_data): Displays individual social connections.
# calculate_more_friends_percentage(x_data, fb_data): Calculates the percentage of people with more friends in X compared to Facebook.
# calculate_triangle_friendships(friends_data): Calculates the number of triangular friendships in a network.
# merge_friendships(x_data, fb_data): Merges friendships from X and Facebook into a single data structure.
# main(): The main function that runs the program and interacts with the user.
#after executing the program, the user will be prompted to enter a choice from the menu.
#The program will then perform the selected analysis and display the results.
#The program will continue to prompt the user for choices until the user chooses to exit the program.
#program ends with a thank you message.




#
# import sys
#
# def input( prompt=None ):
#     """
#         DO NOT MODIFY: Uncomment this function when submitting to Codio
#         or when using the run_file.py to test your code.
#         This function is needed for testing in Codio to echo the input to the output
#         Function to get user input from the standard input (stdin) with an optional prompt.
#         Args:
#             prompt (str, optional): A prompt to display before waiting for input. Defaults to None.
#         Returns:
#             str: The user input received from stdin.
#     """
#
#     if prompt:
#         print( prompt, end="" )
#     aaa_str = sys.stdin.readline()
#     aaa_str = aaa_str.rstrip( "\n" )
#     print( aaa_str )
#     return aaa_str


choices = '''
  Menu : 
     1: Max number of friends intersection between X and Facebook among all
     2: Percentage of people with no shared friends between X and Facebook
     3: Individual information
     4: Percentage of people with  more friends in X compared to Facebook
     5: The number of  triangle friendships in X
     6: The number of  triangle friendships on Facebook
     7: The number of  triangle friendships in X and Facebook together 
       Enter any other key(s) to exit

  '''
#
# "Input a choice ~:"
#
# "Error. File does not exist"
# "\nEnter a names file ~:"
# "\nEnter the X id file ~:"
# "\nEnter the facebook id file ~:"
#
# "The Max number intersection of friends between X and Facebook is: {}"
# "{}% of people have no friends in common on X and Facebook"
#
# "Enter a person's name ~:"
# print("-"*14+"\nFriends in X\n"+"*"*14)
# print("-"*20+"\nFriends in Facebook\n"+"*"*20)
# "Invalid name or does not exist"
#
# "{}% of people have more friends in X compared to Facebook"
#
# "The number of triangle friendships in X is: {}"
# "The number of triangle friendships in Facebook is: {}"
# "The number of triangle friendships in X merged with Facebook is:  {}"
# "Thank you"

import csv
def open_file(prompt):
    """
    Prompt for file name and open the file.

    """
    while True:
        filename = input(prompt)
        try:
            file = open(filename, 'r')
            return file
        except FileNotFoundError:
            print("Error. File does not exist")

def read_names_file()
    #write a description of what this function does
    """
    Read a file containing names and assigns each name an ID.
    #
    :return: 
    """
    #
    with open_file("\nEnter a names file ~:") as names_file:
        reader = csv.reader(names_file)
        names_to_ids = {row[0]: index for index, row in enumerate(reader)}
    ids_to_names = {index: name for name, index in names_to_ids.items()}
    return names_to_ids, ids_to_names



def read_friends_file(network_name, names_to_ids=None):
    friends_file = open_file(f"\nEnter the {network_name} id file ~:")
    friends_data = {}

    for index, line in enumerate(friends_file):
        line = line.strip()
        if line:
            if network_name == 'facebook':
                friends = {names_to_ids.get(friend, None) for friend in line.split(',') if friend.strip()}
            else:
                friends = {int(friend_id) for friend_id in line.split(',') if friend_id.strip()}
        else:
            friends = set()

        friends_data[index] = friends

    friends_file.close()
    return friends_data




def find_max_intersection(friends_data_x, friends_data_fb):
    max_intersection = 0
    for user_id in friends_data_x:
        friends_x = friends_data_x[user_id]
        friends_fb = friends_data_fb.get(user_id, set())
        intersection_size = len(friends_x.intersection(friends_fb))
        max_intersection = max(max_intersection, intersection_size)
    return max_intersection



def calculate_no_shared_percentage(x_data, fb_data):
    total_users = len(x_data)
    no_shared_count = sum(1 for user_id, x_friends in x_data.items()
                          if not x_friends.intersection(fb_data.get(user_id, set())))
    return (no_shared_count / total_users) * 100

def display_individual_info(names_to_ids, ids_to_names, x_data, fb_data):
    while True:
        name = input("Enter a person's name ~:").strip().title()
        user_id = names_to_ids.get(name)

        if user_id is not None:
            x_friends_ids = x_data.get(user_id, set())
            fb_friends_ids = fb_data.get(user_id, set())

            x_friends = "\n".join(sorted(ids_to_names.get(friend_id, '') for friend_id in x_friends_ids))
            fb_friends = "\n".join(sorted(ids_to_names.get(friend_id, '') for friend_id in fb_friends_ids))

            print("--------------")
            print("Friends in X")
            print("**************")
            if x_friends:
                print(x_friends)
            else:
                print("No friends in X.")
            print("--------------------")
            print("Friends in Facebook")
            print("********************")
            if fb_friends:
                print(fb_friends)
            else:
                print()
            break
        else:
            print("Invalid name or does not exist")

def calculate_more_friends_percentage(x_data, fb_data):
    more_friends_count = 0
    total_users = len(x_data)
    for user_id in x_data:
        x_friends = x_data[user_id]
        fb_friends = fb_data.get(user_id, set())
        # print (len(x_friends), len(fb_friends))
        if len(x_friends) > len(fb_friends):
            more_friends_count += 1
    return (more_friends_count / total_users) * 100


def calculate_triangle_friendships(friends_data): #Function to calculate the number of triangular friendships in a network.
    triangle_sets = set()
    user_ids = list(friends_data.keys())

    for i in range(len(user_ids)):
        user_friends = friends_data[user_ids[i]]
        for friend_id in user_friends:
            if friend_id > user_ids[i]:
                mutual_friends = user_friends.intersection(friends_data.get(friend_id, []))
                for mutual_friend in mutual_friends:

                    if mutual_friend > friend_id:

                        triangle_sets.add((user_ids[i], friend_id, mutual_friend))

    return len(triangle_sets)

def merge_friendships(x_data, fb_data): #Function to merge friendships from X and Facebook into a single data structure.
    merged_data = {}
    for user_id in set(x_data) | set(fb_data):  # Union of keys from both dictionaries
        merged_friends = x_data.get(user_id, set()) | fb_data.get(user_id, set())
        merged_data[user_id] = merged_friends
    return merged_data

def main(): #The main function that runs the program and interacts with the user.
    names_to_ids, ids_to_names = read_names_file()
    x_data = read_friends_file("twitter", names_to_ids)
    fb_data = read_friends_file("facebook", names_to_ids)

    while True:
        print(choices)
        choice = input("Input a choice ~:")

        if choice == '1':
            # inside main function
            max_intersection = find_max_intersection(x_data, fb_data)

            print(f"The Max number intersection of friends between X and Facebook is: {max_intersection}")
        elif choice == '2':
            no_shared_percentage = calculate_no_shared_percentage(x_data, fb_data)
            print(f"{round(no_shared_percentage)}% of people have no friends in common on X and Facebook")
        elif choice == '3':
            # name = input("Enter a person's name ~: ")
            display_individual_info(names_to_ids, ids_to_names, x_data, fb_data)
        elif choice == '4':
            more_friends_percentage = calculate_more_friends_percentage(x_data, fb_data)
            print(f"{round(more_friends_percentage)}% of people have more friends in X compared to Facebook")
        elif choice == '5':
            triangle_count_x = calculate_triangle_friendships(x_data)
            print(f"The number of triangle friendships in X is: {triangle_count_x}")

        elif choice == '6':
            triangle_count_fb = calculate_triangle_friendships(fb_data)
            print(f"The number of triangle friendships in Facebook is: {triangle_count_fb}")

        elif choice == '7':
            merged_data = merge_friendships(x_data, fb_data)
            triangle_count_merged = calculate_triangle_friendships(merged_data)
            print(f"The number of triangle friendships in X merged with Facebook is:  {triangle_count_merged}")

        else:
            print("Thank you")
            break

if __name__ == "__main__":
    main()
