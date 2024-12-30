import logging
import os
import sys
from time import sleep
from typing import Literal
import fastapi
import aiohttp
import httpx

app = fastapi.FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


async def send_request(mode: Literal["aiohttp", "httpx"], request_id: int):
    try:
        if mode == "httpx":
            async with httpx.AsyncClient(timeout=1) as client:
                await client.get("http://example.com")
        elif mode == "aiohttp":
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(1)
            ) as session:
                async with session.get("http://example.com") as response:
                    await response.text()
        else:
            raise ValueError(f"Invalid mode: {mode}")
    except Exception as e:
        logging.error(f"{request_id} fail: {type(e).__module__}.{type(e).__name__}")
    else:
        logging.info(f"{request_id} success")


cnt = 0
mode: Literal["aiohttp", "httpx"] = "aiohttp"


@app.get("/")
async def root():
    global cnt
    cnt += 1

    request_id = cnt

    logging.info(f"{request_id} waiting")
    sleep(1)

    logging.info(f"{request_id} requesting")
    await send_request(mode, request_id)


if __name__ == "__main__":
    import uvicorn

    if (args := sys.argv) and len(args) > 1:
        mode = args[1]
    logging.info(f"mode: {mode}")
    uvicorn.run(app, port=int(os.getenv("PORT", 5006)))
