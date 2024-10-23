#!/usr/bin/env python3
"""
we are searching for certain topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    iam here
    """
    return mongo_collection.find({"topics": topic})
