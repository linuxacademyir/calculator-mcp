# client.py
import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def call_calculator(expression: str, url="http://127.0.0.1:8500"):
    async with streamablehttp_client(url) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool("calculate", arguments={"payload": expression})
            print("Response:", result)

if __name__ == "__main__":
    asyncio.run(call_calculator("sqrt(25) + 2**3"))
