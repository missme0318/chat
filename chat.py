def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f :
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines, person1, person2):
	chat = []
	person = None  #預設為空值，避免讀取的檔案第一行沒有人名而產生錯誤(與第18行一組)
	for line in lines:
		if person1 == line:
			person = line
			continue
		elif person2 == line:
			person = line
			continue
		if person: #可理解為如果person有值，才執行....(與第10行一組)
			chat.append(str(person + ': ' + line))
	return chat

def output_file(filename,convertor):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in convertor:
			f.write(line + '\n')



def main():
	lines = read_file('對話紀錄相關檔案/對話紀錄1/input.txt')
	convertor = convert(lines, 'Allen', 'Tom')
	save_file = output_file('對話紀錄相關檔案/對話紀錄1/output.txt', convertor)

main()
