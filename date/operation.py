from datetime import datetime, timedelta

now = datetime.now()

deadline = now + timedelta(days=10)
created_at = now - timedelta(days=5)

future_month = now + timedelta(weeks=4)

print("Deadline is to be ", deadline)

print("Product created at ", created_at)

print("Product created at ", future_month)
