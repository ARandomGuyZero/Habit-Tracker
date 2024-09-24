"""
Habit Tracker

Author: ALan
Date: September 24th 2024

This script contains the functions needed to use the pixela API.
Pixela allows the user to store data as pixes to track their habits frequency and data.
This code has the most used functions in order to make it work, you are free to modify it.
Pixela: https://pixe.la/
"""

import requests
from datetime import datetime

USERNAME = "your username"
TOKEN = "your token (make it up)"
GRAPH_ID = "graph1"

# Endpoint
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

def create_user():
    """
    Creates a new user
    :return:
    """

    # Parameters to login
    user_parameters = {
        "username": USERNAME,
        "token": TOKEN,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
    print(response.text)

def create_graph():
    """
    Creates a new graph
    :return:
    """
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

    graph_configuration = {
        "id": "graph1", # ID, very important
        "name": "Cycling Graph", # Name
        "unit": "Km", # How are you measuring it
        "type": "float", # Type of data
        "color": "shibafu" # Color
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)

def create_pixel():
    """
    Creates a new pixel with the new data
    :return:
    """
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

    today = datetime.now()

    pixel_configuration = {
        "date": today.strftime("%Y%m%d"),
        "quantity": "14",
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.post(url=graph_endpoint, json=pixel_configuration, headers=headers)
    print(response.text)

def modify_pixel():
    """
    Modifies the pixel data of the graph
    :return:
    """
    today = datetime.now()
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

    pixel_configuration = {
        "quantity": "13.2",
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.put(url=graph_endpoint, json=pixel_configuration, headers=headers)
    print(response.text)

def delete_pixel():
    """
    Deletes the pixel of the graph
    :return:
    """
    today = datetime.now()
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.delete(url=graph_endpoint, headers=headers)
    print(response.text)

delete_pixel()
