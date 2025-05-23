import json
import asyncio
from aioconsole import ainput

import websockets


async def input_loop(ws):
    while True:
        cmd = await ainput("")
        await ws.send(cmd)


async def receive_loop(ws):
    while True:
        try:
            res = await ws.recv()
            data = json.loads(res)
            render(data)
        except websockets.ConnectionClosed:
            print("Disconnected.")
            break


def render(data):
    field = data["field"]
    print()
    for line in field:
        print(*line)


async def start_client():
    async with websockets.connect("ws://localhost:8756") as ws:
        input("Press any key to start!")
        await asyncio.gather(input_loop(ws), receive_loop(ws))


if __name__ == "__main__":
    asyncio.run(start_client())
