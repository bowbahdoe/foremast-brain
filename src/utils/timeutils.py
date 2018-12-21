from datetime import datetime, timezone
from dateutil.parser import parse

def getNow():
    return datetime.now(timezone.utc).astimezone()

def getNowStr():
    return parse(str(getNow()))



def isPast(timeToCompareStr, biasInSeconds=30):
    timeToCompare = parse(timeToCompareStr)
    td = timeToCompare- getNow()
    diffsec = int(round(td.total_seconds()))
    if diffsec < -biasInSeconds:
        return True
    return False

def canProcess(startTimeStr, endTimeStr, past=0.2):
   startTime = parse(startTimeStr)
   endTime = parse(endTimeStr)
   tdInterval = endTime - startTime
   interval = int(round(tdInterval.total_seconds()))
   tdNowInterval = getNow()-startTime
   nowInterval = abs(int(round(tdNowInterval.total_seconds())))
   if (nowInterval >= 60):
       return True
   pct = nowInterval/interval
   if pct <= past:
       return False
   return True

def rateLimitCheck(lastModifiedTimeStr, past=5):
   lastModified = parse(lastModifiedTimeStr)
   tdNowInterval = getNow()-lastModified
   nowInterval = abs(int(round(tdNowInterval.total_seconds())))
   if (nowInterval >= past):
       return True
   return False
