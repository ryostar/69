"""
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  ZauteKm <https://telegram.dog/ZauteKm>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://www.youtube.com/watch?v=yoZy2E17-50")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '1087968824')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '6340775'))
    CHAT = int(os.environ.get("CHAT", "-1001140954081"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001318155972")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "Y")
    ARQ_API=os.environ.get("ARQ_API", "TKWTIF-BBLIKJ-YFHTCA-DPETDC-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 30))
    API_HASH = os.environ.get("API_HASH", "2265a0bd8c0a63b25eb330205426698d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1659408866:AAFtM1pG7IU3CFY-IAg_7Tbi_iTiqvLcvI4") 
    SESSION = os.environ.get("SESSION_STRING", "SESSION")
    playlist=[]
    msg = {}
