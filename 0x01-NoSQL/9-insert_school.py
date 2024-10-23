#!/usr/bin/env python3
"""
we are inserting things here
"""


def insert_school(mongo_collection, **kwargs):
    """
    iam here
    """
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
