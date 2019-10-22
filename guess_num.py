# generate a random integer (don't print)
# let user enter integer repeatedly to guess
# correct print "finally correct!"
# wrong tell user larger/lower than answer

import random # 載入模組 才能產生隨機數
start = input('Please decide random number start: ')
start = int(start)
end = input('Please decide random number end: ')
end = int(end)

#r = random.randint(1, 100)
r = random.randint(start, end)  # replace as variables
count = 0
while True:
	count += 1	# count = count + 1
	#num = input('Please guess a number within 1 to 100: ')
	num = input('Please guess a number within %d to %d: ' %(start, end))
	num = int(num)	# casting is important
	if num == r:
		print("Finally correct!")
		print("This is your %d times" %count)
		break
	elif num > r:
		print("Guess is larger than answer")
	else:
		print("Guess is lower than answer")
	print("This is your %d times" %count)	# 寫在這 避免重複寫三次 避免重複性太高的問題 
											# 但是這樣就不會算到猜中這次

