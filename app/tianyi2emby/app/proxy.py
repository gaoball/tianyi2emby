from fastapi.responses import StreamingResponse
import aiohttp

async def stream_from_tianyi(share_id: str, file_id: str):
    real_url = f"https://cloud.189.cn/shareStreamFake/{share_id}/{file_id}"
    session = aiohttp.ClientSession()
    response = await session.get(real_url)
    return StreamingResponse(response.content, media_type="video/mp4")