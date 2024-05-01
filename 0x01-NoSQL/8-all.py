#!/usr/bin/env python3
""" List the documents in a collection """


def list_all(mongo_collection):
    """ lists the documents in a collection """
    return mongo_collection.find()
