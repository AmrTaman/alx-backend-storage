#!/usr/bin/env python3
"""
iam here doing updates to documents
"""


def update_topics(mongo_collection, name, topics):
    """
    iame here
    """
    mongo_collection.update_one({'name': name}, {"$set": {'topics': topics}})
