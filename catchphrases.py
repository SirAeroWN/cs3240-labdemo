def catchphrase(num):
	phrases = ["Wubbalubbadubdub!","Rikitikitavi, b****!","And that's the wayyyyyy the news goes!","Hit the sack, Jack!","Uh ohhhh! Somersoult jump!","And that's why I always say, 'Shumshumschilpiddydah!'","GRASSSSS... tastes bad!","No jumping in the sewer.","BURGERTIME!","Rubber baby buggy bumpers!","Lick, lick, lick, a lollipop!"]
	if num < 0:
		num = num * -1
	if num >= len(phrases):
		num = num % len(phrases)
	return phrases[num]

if __name__ == '__main__':
	print(catchphrase(5))