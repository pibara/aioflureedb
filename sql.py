#!/usr/bin/python3
import sys
import asyncio
import aioflureedb

async def sql_demo():
    print("Connecting to FlureeDB")
    async with aioflureedb.FlureeClient(port=8090) as flureeclient:
        print("Waiting till Fluree is ready")
        await flureeclient.health.ready()
        print("Looking up database")
        db = await flureeclient["dla/base"]
    print("Opening database")
    async with db() as database:
        print("SQL query")
        result = await database.sql("select name from _predicate")
        print(result)

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(sql_demo())
