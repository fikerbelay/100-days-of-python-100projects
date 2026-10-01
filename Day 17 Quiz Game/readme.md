
# Day 17 — Quiz Game 🧠

A command-line True/False quiz game built in Python as part of the **100 Days of Python** challenge.

The game pulls a set of True/False trivia questions from a local dataset, presents them one at a time, and tracks whether the player's answer is correct.

---

## 📁 Project Structure

```
Day 17 Quiz Game/
├── main.py              # Entry point — starts the quiz
├── quiz_brain.py        # Core game logic (ProcessQuestion class)
├── question_model.py    # Question class (holds text + answer)
├── data.py              # question_data list (the trivia questions)
└── README.md
```

---

## 🚀 How to Run

Make sure you have **Python 3.7+** installed.

```bash
# From the project folder
python main.py
```

You'll be prompted with questions like:

```
Q.1: A slug's blood is green. (True/False): True
correct
Q.2: The loudest animal is the African Elephant. (True/False): False
correct
...
```

Type `True` or `False` and press **Enter** for each question.

---

## 🧩 How It Works

### `question_model.py`
Defines a `Question` class that stores a question and its correct answer.

```python
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def Ask(self, number, process):
        user_answer = input(f"Q.{number}: {self.question} (True/False): ")
        process.check_answer(user_answer, self.answer)
```

### `quiz_brain.py`
Contains the `ProcessQuestion` class that drives the quiz — it iterates through the data, creates `Question` objects, and checks answers.

```python
class ProcessQuestion:
    def __init__(self):
        self.number = 0

    def fetch(self):
        for q_and_a in question_data:
            self.number += 1
            qua = question_model.Question(q_and_a['text'], q_and_a['answer'])
            qua.Ask(self.number, self)

    def check_answer(self, u_answer, answer):
        if u_answer == answer:
            print("correct")
        else:
            print("wrong")
```

### `data.py`
Holds `question_data`, a list of dictionaries in the form:

```python
{"text": "A slug's blood is green.", "answer": "True"}
```

### `main.py`
The entry point:

```python
from quiz_brain import ProcessQuestion

process = ProcessQuestion()
process.fetch()
```

---

## 💡 Notes on the Design

- **Data is separated from logic.** Want to add more questions? Just edit `data.py` — no code changes required.
- **Single responsibility per file.** Each file does one thing:
  - `data.py` → data
  - `question_model.py` → the question object
  - `quiz_brain.py` → the quiz flow
  - `main.py` → wiring it together

---

## 🛠 Possible Improvements

- [ ] Track and display a **score** at the end (e.g. `You scored 8/12`).
- [ ] Shuffle questions using `random.shuffle()` for replayability.
- [ ] Accept `true/false`, `t/f`, `1/0` as valid inputs (case-insensitive).
- [ ] Move questions to an external JSON file.
- [ ] Add a GUI version using **Tkinter** (this is what the course does next!).

---

## 📚 Part of

[100 Days of Code — The Complete Python Pro Bootcamp] **Day 17: Quiz Game**

---

iz_brain.py`, and `question_model.py` and I'll tweak the README so the code snippets match exactly what's on disk.
