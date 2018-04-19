now = int(input("Time now: "))
wait = int(input("Time to wait: "))
print((now+wait)%24)
print(str((now+wait)%12)+"am" if (now+wait)%24 < 12 else str((now+wait)%12)+"pm")
