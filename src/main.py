from calculator import add,subtract,multiply,divide
from text_analyzer import word_count,character_count,sentence_count,unique_word_count,most_common_word
from dotenv import load_dotenv
import os

load_dotenv()

print("App Name:",os.getenv("APP_NAME"))
print("API Key:",os.getenv("API_KEY"))

print("Calculator Module")
print("Add:",add(10,5))
print("Subtract:",subtract(10,5))
print("Multiply:",multiply(10,5))
print("Divide:",divide(10,5))

text="Artificial intelligence is changing the world. AI is powerful."

print("\nText Analyzer")
print("Word count:",word_count(text))
print("Character count:",character_count(text))
print("Sentence count:",sentence_count(text))
print("Unique word count:",unique_word_count(text))
print("Most common word:",most_common_word(text))