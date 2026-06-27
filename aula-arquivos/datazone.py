import datetime as d
from zoneinfo import ZoneInfo

agora = d.datetime.now(ZoneInfo("America/Sao_Paulo"))
print(agora)