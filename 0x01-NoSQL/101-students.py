#!/usr/bin/env python3
"""
iam here
"""


def top_students(mongo_collection):
    # Aggregate to calculate average score for each student
    pipeline = [
        {
            '$project': {
                'name': 1,  # Include the student's name
                'averageScore': { '$avg': '$scores' }  # Calculate average score
            }
        },
        {
            '$sort': {
                'averageScore': -1  # Sort by average score in descending order
            }
        }
    ]
    
    return list(mongo_collection.aggregate(pipeline))
