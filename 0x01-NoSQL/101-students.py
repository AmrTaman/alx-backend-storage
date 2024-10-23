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
                'name': 1,
                'averageScore': {'$avg': '$scores'}
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
