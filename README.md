# Text Analyzer – Engeto Project

**First project** for the **Engeto Online Academy – Python for Data Analysts**  

---

## Project Description

This project is a beginner-friendly **text analyzer** written in Python.  
The program allows the user to log in, select one of three predefined texts, and then displays basic statistics about the selected text.

---

## What the program does

- Verifies user login (based on predefined usernames and passwords)
- Allows selection of 1 of 3 hardcoded texts
- Analyzes the selected text and displays:
  - Number of words
  - Number of titlecase words
  - Number of uppercase words
  - Number of lowercase words
  - Number of numeric strings
  - Sum of all numbers
- Displays a simple horizontal bar chart (word length frequencies)

---

## Example Output

```
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 1
----------------------------------------
There are 54 words in the selected text.
There are 12 titlecase words.
There is 1 uppercase word.
There are 38 lowercase words.
There are 3 numeric strings.
The sum of all numbers is 8510
----------------------------------------
LEN| OCCURRENCES  |NR.
  1|*             |1
  2|*********     |9
  3|******        |6
  4|***********   |11
  5|************  |12
  6|***           |3
  7|****          |4
  8|*****         |5
  9|*             |1
 10|*             |1
 11|*             |1
```

If the user is not registered:

```
username: marek
password: 123
Unregistered user, terminating the program...
```

---

## Login Credentials

| Username | Password    |
|----------|-------------|
| bob      | 123         |
| ann      | pass123     |
| mike     | password123 |
| liz      | pass123     |

---

## File Structure

```
projekt_1.py           # Main script
texts/ (optional)      # Folder with text data (if separated)
```

---

## Requirements

No external libraries required – runs with standard Python 3.x installation.

You can run the script with:

```bash
python projekt_1.py
```

---

## 👩‍💻 Author

- **Romana Bělohoubková**  
- 📧 [romanabelohoubkova@gmail.com](mailto:romanabelohoubkova@gmail.com)  
- 💬 Discord: Romana.B


