import json
import asyncio
import websockets

from server.modules.board import PlayBoard

"""
J：左に進む
K：発車
L：右に進む
"""

HEIGHT = 15
WIDTH = 9

PB = PlayBoard(HEIGHT, WIDTH)


async def run_game(websocket):
    while True:
        try:
            message = await asyncio.wait_for(websocket.recv(), timeout=1.0)
            PB.update(message)
        except asyncio.TimeoutError:
            PB.update("")
            pass
        await websocket.send(json.dumps(PB.get_board_state()))
        await asyncio.sleep(0.1)


async def start_server():
    async with websockets.serve(run_game, "localhost", 8756):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(start_server())
