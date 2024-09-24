import aiofiles
from aiocsv import AsyncWriter
from hikerapi import AsyncClient

columns = [
    "pk",
    "username",
    "full_name",
    "is_private",
    "is_verified",
    "media_count",
    "follower_count",
    "following_count",
    "biography",
    "external_url",
    "is_business",
    "public_email",
    "contact_phone_number",
]
ids = ["4037427350", "1726342880"]
cl = AsyncClient(token="AICzps7doHr9eACOjgD15meap99R6ylL")

def create_row(res: dict, columns: list) -> list:
    for key in res.copy():
        if key not in columns:
            del res[key]
    return list(res.values())

async def save_csv():
    print("Мы находимся здесь")    
    async with aiofiles.open("user_info.csv", "w") as f:
        writer = AsyncWriter(f)
        await writer.writerow(columns)
        for id_ in ids:
            res = await cl.user_by_id_v1(id_)
            row = create_row(res, columns)
            await writer.writerow(row)
