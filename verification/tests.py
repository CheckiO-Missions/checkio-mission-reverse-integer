"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": [1234], "answer": 4321},
        {"input": [0], "answer": 0},
        {"input": [-123], "answer": -321},
        {"input": [5], "answer": 5},
        {"input": [-9], "answer": -9},
        {"input": [100], "answer": 1},
        {"input": [-100], "answer": -1},
        {"input": [54321], "answer": 12345},
        {"input": [1111], "answer": 1111},
        {"input": [987654321], "answer": 123456789}
    ],
    "Extra": [
        {"input": [10**8], "answer": 1},
        {"input": [-(10**8 + 7)], "answer": -700000001}
    ]
}

