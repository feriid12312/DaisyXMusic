# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Salam 👋 [{}](tg://user?id={})!**\n\n🤖 Telegram Qrupları və Kanallarının səsli söhbətlərində musiqi oxumaq üçün yaradılmış bir botam.\n\n✅ Mənə /help yazaraq ətraflı məlumat alın."
      HELP_MSG = [
        ".",
f"""
**Salam. 👋 Xoş gəldin {PROJECT_NAME}

⚪️ {PROJECT_NAME} qrup və kanalınızın səsli söhbətində musiqi çala bilir.
⚪️ Assistantın adı >> @{ASSISTANT_NAME}\n\nMəlumat üçün növbəti düyməni basın**
""",

f"""
**Ayarlamaq üçün məlumat**

1. Botu Grupa Əlavə edin
2. Botu Admin edin
3. Səsli söhbəti başladın
4. Adminlərdən biri mahnı adı yazmadan sadəcə /play göndərin 
- Bu zaman @{ASSISTANT_NAME} grupa qatılmalıdı əgər qatılmazsa əl ilə qatın
5. /play [Mahnı adı] Və asistan səsli söhbətdə mahnı oxumaga davam edəcəkdir!
**Commands**

**=>> Song Playing 🎧**

- /play: İstədiyiniz mahnı adını daxil edin.
- /play [Bir mahnıya yanıt]: Yanıt verdiyiniz mahnını oxuyur

**=>> ADMİN ⏯**

- /player: Musiqi idarə panelini açır
- /skip: Mahnılar arası keçid edir
- /pause: Mahnıya ara verir
- /resume: Ara verilən mahnıya davam edir
- /end: Mahnını dayandırır
- /current: Hazırda oxuyan mahnını göstərir
- /playlist: Hazırda tələb olunan mahnı siyası

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        
f"""
**=>> Kanal Muzik grulumu üçün irəli 🛠**

⚪️ For linked group admins only:

- /cplay: [Mahnı adı] 
- /cplayer: Musiqi idarə panelini açır
- /cskip: Mahnılar arası keçid edir
- /cpause: Mahnıya ara verir
- /cresume: Ara verilən mahnıya davam edir
- /cend: Mahnını dayandırır
- /ccurrent: Hazırda oxuyan mahnını göstərir
- /cplaylist: Hazırda tələb olunan mahnı siyası
- /userbotjoinchannel - Asistanı grupa əlavə et
channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**=>> Daha çox 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Grupda admin siyahısını yeniləyir
- /userbotjoin: @{ASSISTANT_NAME} grupa dəvət et



/play, /current  və /playlist Xaric digər əmrlər adminlər üçündür
""",
"""
👋 **Salam**\nMən Telegram gruplarında səsli söhbətdə musiqi dinləmək üçün yaradılan botam\nMəni grupa əlavə edərək admin hüquqları verin\nƏmrlər və daha ətraflı məlumat üçün /help.
"""
      ]
