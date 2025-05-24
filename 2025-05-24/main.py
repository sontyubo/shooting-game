import asyncio

from server import server_app
from client import client_app


async def main():
    await asyncio.gather(server_app.start_server(), client_app.start_client())


if __name__ == "__main__":
    asyncio.run(main())
