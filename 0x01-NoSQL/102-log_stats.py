#!/usr/bin/env python3
"""
playground
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    coll = client.logs.nginx
    total_logs = coll.count_documents({})
    method_get = coll.count_documents({"method": "GET"})
    method_post = coll.count_documents({"method": "POST"})
    method_put = coll.count_documents({"method": "PUT"})
    method_patch = coll.count_documents({"method": "PATCH"})
    method_delete = coll.count_documents({"method": "DELETE"})
    status_check = coll.count_documents({"method": "GET", "path": "/status"})

    result = (
        "{} logs\nMethods:\n"
        "\tmethod GET: {}\n"
        "\tmethod POST: {}\n"
        "\tmethod PUT: {}\n"
        "\tmethod PATCH: {}\n"
        "\tmethod DELETE: {}\n"
        "{} status check"
    ).format(total_logs, method_get, method_post,
             method_put, method_patch, method_delete, status_check)
    print(result)

    ip_counts = coll.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    print("IPs:")
    for ip in ip_counts:
        print(f"\t{ip['_id']}: {ip['count']}")

