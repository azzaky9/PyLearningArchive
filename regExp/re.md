Regular Expressions (RegEx) are powerful tools for pattern matching and text processing. In this workshop, we'll focus on practical applications of RegEx in Python, covering essential concepts through hands-on exercises.

```python
import re

# Basic pattern matching
pattern = r"python"
text = "I love python programming"
match = re.search(pattern, text)
print(f"Match found: {match.group() if match else 'No match'}")

# Case-insensitive matching
pattern = r"PYTHON"
match = re.search(pattern, text, re.IGNORECASE)
print(f"Case-insensitive match: {match.group() if match else 'No match'}")
```

Exercise 1: Create a Python script that asks the user for a word to search for and a sentence, then searches for the word in the sentence (case-insensitive) and prints whether the word was found and its position.

```python
import re

word = input("Enter a word to search for: ")
sentence = input("Enter a sentence: ")

pattern = re.compile(word, re.IGNORECASE)
match = pattern.search(sentence)

if match:
    print(f"'{word}' found at position {match.start()}")
else:
    print(f"'{word}' not found in the sentence")
```

Now let's explore character classes and quantifiers:

```python
# Digit matching
pattern = r"\d+"
text = "I have 3 apples and 2 oranges"
matches = re.findall(pattern, text)
print(f"Numbers found: {matches}")

# Word boundary
pattern = r"\bcat\b"
text = "I have a cat and a caterpillar"
matches = re.findall(pattern, text)
print(f"Whole word 'cat' occurrences: {matches}")
```

Exercise 2: Extend your script to ask the user for a phone number, validate if it's in the format XXX-XXX-XXXX (X being digits), and extract the area code if valid.

```python
phone_number = input("Enter a phone number (XXX-XXX-XXXX): ")

pattern = r"^(\d{3})-\d{3}-\d{4}$"
match = re.match(pattern, phone_number)

if match:
    print("Valid phone number")
    print(f"Area code: {match.group(1)}")
else:
    print("Invalid phone number format")
```

Let's move on to grouping and capturing:

```python
# Capturing groups
pattern = r"(\w+),(\w+)"
text = "Doe,John"
match = re.match(pattern, text)
if match:
    print(f"Last name: {match.group(1)}, First name: {match.group(2)}")

# Named groups
pattern = r"(?P<last>\w+),(?P<first>\w+)"
match = re.match(pattern, text)
if match:
    print(f"Last name: {match.group('last')}, First name: {match.group('first')}")
```

Exercise 3: Modify your script to ask the user for a date in the format YYYY-MM-DD, extract and print the year, month, and day separately, and validate that the date is between 2000-01-01 and 2099-12-31.

```python
date = input("Enter a date (YYYY-MM-DD): ")

pattern = r"^(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
match = re.match(pattern, date)

if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")
    if "2000-01-01" <= date <= "2099-12-31":
        print("Date is within valid range")
    else:
        print("Date is out of valid range")
else:
    print("Invalid date format")
```

Finally, let's look at some practical applications:

```python
# Email validation
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email = "user@example.com"
print(f"Valid email: {bool(re.match(email_pattern, email))}")

# URL extraction
url_pattern = r"https?://[^\s]+"
text = "Visit our website at https://www.example.com or http://example.org"
urls = re.findall(url_pattern, text)
print(f"URLs found: {urls}")
```

Exercise 4: Finalize your script by asking the user for a paragraph of text, then extracting and printing all email addresses found in the text.

```python
paragraph = input("Enter a paragraph of text: ")

email_pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
emails = re.findall(email_pattern, paragraph)

if emails:
    print("Email addresses found:")
    for email in emails:
        print(email)
else:
    print("No email addresses found")
```

This workshop covered essential RegEx concepts including basic matching, character classes, quantifiers, grouping, capturing, and practical applications like email and URL parsing. Continue practicing with different patterns and texts to improve your RegEx skills.
