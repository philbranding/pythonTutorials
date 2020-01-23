#reading a file
import requests  #works for python 2 only it will give an error for python3

def read_text():
    quotes = open("/Users/phil/WebDev/Udacity/00-Python/BasicPython/00-Projects/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
  connection = requests.get("http://www.wdylike.appspot.com/?q="+text_to_check)
  output = connection.text

  if output == 'true':
      output = 'YES, PLEASE CHOOSE YOUR WORDS CAREFULLY'
  else:
      output = 'NO, ALL GOOD MATE'

  print(" ")
  print("--------------------------------------------------------------------------------")
  print("Does your text contain Profane Words :  " +  output)
  print("--------------------------------------------------------------------------------")

  connection.close()

read_text()
