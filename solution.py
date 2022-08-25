"""
Name: Ari Cerrahyan
Date: August 24, 2021
"""

class Actor:
    # Actor class to store actor's name and stats
    def __init__(self, name:str, movies:int, rating:float):
        self.name:str = name
        self.total_movies:int = movies
        self.total_rating:float = rating

class Node:
    # Node class for linked list
    def __init__(self, data:Actor):
        self.data:Actor = data
        self.next:Node = None

class LinkedList:  
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data:Actor):
        # Append new node to end of linked list
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.size += 1
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
            self.size += 1
            
    def actor_in_list(self, actor_name:str):
        # Check if an actor is in the list
        current_node = self.head
        while current_node != None:
            if current_node.data.name == actor_name:
                return True
            current_node = current_node.next
        return False
    
    def update_actor(self, actor_name:str, rating:float):
        # Update actor's rating and total movies
        current_node = self.head
        while current_node != None:
            if current_node.data.name == actor_name:
                current_node.data.total_movies += 1
                current_node.data.total_rating += rating
            current_node = current_node.next
            
    def sort_list(self):
        # Sort the list by total movies in ascending order using bubble sort
        end = None
        
        while end != self.head.next:
            curr = self.head
            while curr.next != end:
                next = curr.next
                if curr.data.total_movies > next.data.total_movies:
                    curr.data, next.data = next.data, curr.data
                curr = curr.next
            end = curr
                        
    def print_list(self):
        # Print the list
        current_node = self.head
        while current_node != None:
            if current_node.data.total_movies < 2:
                current_node = current_node.next
                continue
            else:
                name = current_node.data.name
                total_movies = current_node.data.total_movies
                average_rating = current_node.data.total_rating / total_movies
                print(f"Star Name: {name}" + f" "*(25-len(name)) + f" | Movies: {total_movies}" +
                    " | AVG Rating: {:0.2f}".format(average_rating))
                current_node = current_node.next
        
import json

data = json.load(open('data.json'))
# load data from json file

link_list = LinkedList()
# create linked list

for movie in data:
    rating = float(movie['rating'])
    
    for star in [name.lstrip() for name in movie['stars'].split(',')]:
        # each star in list of stars split by comma and lstrip to remove whitespace
        
        if link_list.actor_in_list(star):
            link_list.update_actor(star, rating)
        else:
            actor = Actor(star, 1, rating)
            link_list.append(actor)
            
link_list.sort_list()
link_list.print_list()