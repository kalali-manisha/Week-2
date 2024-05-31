Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def count_words(text):
...     """
...     This function counts the number of words in the given text.
...     :param text: str, input text
...     :return: int, word count
...     """
...     # Split the text by spaces and filter out empty strings
...     words = text.split()
...     return len(words)
... 
... def main():
...     # Prompt the user to enter a sentence or paragraph
...     user_input = input("Enter a sentence or paragraph: ").strip()
...     
...     # Check if the input is empty
...     if not user_input:
...         print("Input cannot be empty. Please enter a valid sentence or paragraph.")
...     else:
...         # Count the words and display the result
...         word_count = count_words(user_input)
...         print(f"Word count: {word_count}")
... 
... if __name__ == "__main__":
...     main()
