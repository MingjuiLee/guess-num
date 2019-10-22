# generate a random integer (don't print)
# let user enter integer repeatedly to guess
# correct print "finally correct!"
# wrong tell user larger/lower than answer

import random # 載入模組 才能產生隨機數

r = random.randint(1, 100)
while True:
	num = input('Please guess a number within 1 to 100: ')
	num = int(num)	# casting is important
	if num == r:
		print("Finally correct!")
		break
	elif num > r:
		print("Guess is larger than answer")
	else:
		print("Guess is lower than answer")
	