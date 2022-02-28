data = []
count = 0
with open('對話紀錄相關檔案/對話紀錄2/[LINE]Mr.梁川.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10 == 0:
			print(len(data))
print('檔案讀取完了，共有', len(data), '筆資料')
print(data[0])

ws = {}
for d in data:
	words = d.strip('\n').split(' ')
	for word in words:
		word
		if word in ws:
			ws[word] += 1
		else:
			ws[word] = 1
for i in ws:
	print(i,'共有出現', ws[i], '次')

while True:
	word = input('請輸入要查詢的字：')
	if word == 'q':
		break
	if word in ws:
		print(word, '出現次數為：', ws[word])
	else:
		print(word, '沒有出現過')

