#!/usr/bin/env python3
"""
iam here
"""


def top_students(mongo_collection):
    """
    iam here
    """
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    return mongo_collection.aggregate(pipeline)
