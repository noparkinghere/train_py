import re

def AnalyseCode(fileName):
  commentLines = 0
  allLines = 0
  with open(fileName, 'r', encoding='utf-8') as f:
    lines = f.readlines()
  allLines = len(lines)

  print(re.search(r'\n$', lines[1]))
  if re.search(r'random$', lines[1]) is not None:
    print('match')
  pos = 0
  while pos < allLines:
    if re.match(r"^\s*#", lines[pos]) is not None:
      a = re.match(r"^\s*#", lines[pos])
      commentLines += 1

    if re.match(r"^\s*'''", lines[pos]) is not None:
      commentLines += 1
      # if re.match(r"^\s*'''.+'''", lines[pos]) is not None:     # ''' 在同行
      #   pos += 1
      #   continue
      # pos += 1
      while re.match(r".*'''$", lines[pos]) is None:
        commentLines += 1
        pos += 1
      else:
        commentLines += 1
    pos += 1

  return allLines, commentLines

if __name__ == '__main__':
  a, b = AnalyseCode('gen_code.txt')
  print(a)
  print(b)