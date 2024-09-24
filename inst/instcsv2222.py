import asyncio
import aiofiles
from aiocsv import AsyncWriter
from hikerapi import AsyncClient

columns = [
    "pk",
    "username",
    "full_name",
    "profile_pic_url",
    "is_verified",
    "is_private",
]

user_id = "1726342880"

cl = AsyncClient(token="RmQ5cfT0fhLh2gnEmhQhwXqrXVL19aVK")

async def csv():
    async with aiofiles.open("foll.csv", "a") as f:
        print("открыл файл")
        writer = AsyncWriter(f)
        await writer.writerow(columns)
        end_cursor = None

        while True:
            followers, end_cursor = await cl.user_followers_chunk_gql(user_id=user_id, end_cursor=end_cursor)
            for f in followers:
                await writer.writerow(f.values())
            if end_cursor == "" or end_cursor == None:
                break


if __name__=="__main__":
    asyncio.run(csv())

