from datetime import datetime

now = datetime.now()
wedding_day = datetime(2011, 10, 1)
wedding_days = now - wedding_day
print(f"우리 결혼한지 +{wedding_days.days}일째")
