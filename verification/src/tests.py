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
        {
            "input": [
                [0, 0, 1, 0],
                [1, 0, 1, 0],
		[1, 1, 1, 0],
		[1, 1, 1, 1]
	    ],
            "answer": [3, 4]
        },
        {
            "input": [
        	[0, 0, 0, 0],
        	[0, 0, 0, 0],
        	[0, 0, 0, 0],
        	[0, 0, 0, 1]
	    ],
            "answer": [4, 1]
        }
    ],
    "Extra": [
        {
            "input": [
        	[1, 0, 0, 0, 0],
        	[1, 1, 0, 0, 0],
        	[1, 1, 1, 0, 0],
        	[1, 1, 1, 1, 0],
        	[1, 1, 1, 1, 1]
	    ],
            "answer": [1, 5]
        },
        {
            "input": [
        	[0, 0, 0, 1, 0, 0, 0],
        	[0, 0, 1, 1, 1, 0, 0],
        	[0, 1, 1, 1, 1, 1, 0],
        	[1, 1, 1, 1, 1, 1, 1],
        	[1, 1, 1, 1, 1, 1, 1],
        	[1, 1, 1, 1, 1, 1, 1]
	    ],
            "answer": [4, 6]
        }
    ]
}
