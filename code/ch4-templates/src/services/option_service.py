from typing import List


def get_options() -> List:
    return [
        {'id': 'Create Order Table', 'summary': "Create an order table (from postgres)"},
        {'id': 'Settings', 'summary': "Choose the options for your download"},
    ]
