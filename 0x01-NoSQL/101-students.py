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
                'averageScore': {'$avg': '$topics.scores'}
            },
            'topics': 1
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
