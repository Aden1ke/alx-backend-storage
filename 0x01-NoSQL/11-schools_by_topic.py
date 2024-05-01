#!/usr/bin/env python3
""" finds schools by a topic """


def schools_by_topic(mongo_collection, topic):
    """ return the list of school having a specific topic """
    return mongo_collection.find({"topics": topic})
