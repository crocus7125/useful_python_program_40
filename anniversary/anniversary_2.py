from datetime import datetime

now = datetime.now()
wedding_day = datetime(2011, 10, 1)
ubin_birth = datetime(2012, 11, 27)

wedding_days = now - wedding_day
ubin_days = now - ubin_birth

print(f"우리 결혼한지 +{wedding_days.days}일째")
print(f"우빈 태어난지 +{ubin_days.days}일째")