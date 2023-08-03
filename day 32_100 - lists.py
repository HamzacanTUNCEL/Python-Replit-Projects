import random
def randomDice():
  randNum=random.randint(0,11)
  return randNum
language=["Turkish","Spanish","French","German","Italian","Japanese","Korean","Portuguese","Hindi","Russian","Vietnamese","Polish"]
greetings=["merhaba!","hola!","bonjour!","guten Tag!","salve!","こんにちは(konnichiwa)!","안녕하세요(annyeonghaseyo)!","olá!","नमस्ते(namaste)!","здравствуйте(zdravstvuyte)!","xin chào!","dzień dobry!"]
while True:
  print(greetings[randomDice()])
