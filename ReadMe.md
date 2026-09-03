# 🎓 AI Study Coach Using Gemini Prompting Techniques

An AI-powered **Study Coach** built with Python, FastAPI, and Google Gemini API that generates personalized study plans based on a student's academic situation.

This project demonstrates and compares three **Prompt Engineering techniques**:

* 🔵 Zero-Shot Prompting
* 🟣 Few-Shot Prompting
* 🟢 Structured Reasoning

---

## 📌 Project Overview

The **AI Study Coach** is a simple Generative AI application designed to help students prepare for exams.

The application takes information about the student's learning situation and uses Google Gemini to generate a personalized, day-by-day study plan.

The user provides:

* Student Name
* Subject
* Weak Topics
* Days Remaining Before Exam
* Available Study Hours Per Day
* Current Skill Level
* Prompting Technique

The project focuses on demonstrating how different prompting techniques can guide an LLM to produce useful and structured responses.

---

## 🎯 Objectives

The main objectives of this project are:

1. Build an AI-powered study planning application.
2. Integrate Google Gemini API with Python.
3. Implement three different prompting techniques.
4. Compare Zero-Shot, Few-Shot, and Structured Reasoning.
5. Generate personalized day-by-day study plans.
6. Build a simple and interactive web interface using FastAPI.
7. Understand the role of prompt design when working with LLMs.

---

# 🧠 Prompting Techniques

## 🔵 1. Zero-Shot Prompting

Zero-Shot Prompting provides the model with instructions and student information **without providing examples**.

The prompt asks Gemini to:

* Identify weak areas
* Prioritize important topics
* Create a day-by-day schedule
* Recommend suitable study activities

**Purpose:**
To see how Gemini performs when it receives only instructions and student information.

---

## 🟣 2. Few-Shot Prompting

Few-Shot Prompting provides the model with **multiple examples** before asking it to generate a study plan for a new student.

The examples demonstrate how study plans can be created for different subjects such as:

* SQL
* Python
* Finance

**Purpose:**
To guide Gemini toward a desired response structure using examples.

---

## 🟢 3. Structured Reasoning

Structured Reasoning asks Gemini to analyze the student's situation systematically.

The prompt considers:

1. Weak topics
2. Topic priorities
3. Days remaining
4. Available study hours
5. Suitable learning activities
6. Final day-by-day study plan
7. Short justifications for recommendations

The application does not request hidden chain-of-thought. Instead, it asks the model to provide concise explanations and justifications.

**Purpose:**
To generate a more organized and logically structured study plan.

---

# 👨‍🎓 Example Student

The application can be tested with the following example:

| Information       | Example                     |
| ----------------- | --------------------------- |
| Student Name      | Ahmed                       |
| Subject           | Python                      |
| Weak Topics       | Loops, Functions, Debugging |
| Days Remaining    | 5                           |
| Study Hours / Day | 2                           |
| Skill Level       | Beginner                    |

### Expected Study Focus

| Day   | Focus                      |
| ----- | -------------------------- |
| Day 1 | Loops                      |
| Day 2 | Functions                  |
| Day 3 | Combined Loops & Functions |
| Day 4 | Debugging                  |
| Day 5 | Mock Exam & Final Revision |

The actual study plan is generated dynamically by Gemini.

---

# 📸 Results

The following screenshots show the outputs generated using the three prompting techniques.

### 🔵 Zero-Shot Prompting

![Zero-Shot](screenshots/zero_shot.png)

### 🟣 Few-Shot Prompting

![Few-Shot](screenshots/few_shot.png)

### 🟢 Structured Reasoning

![Structured Reasoning](screenshots/structured_reasoning.png)

---

# 🖥️ Application Features

* 🎓 AI-powered personalized study planning
* 🤖 Google Gemini integration
* 🧠 Three Prompt Engineering techniques
* 📝 Student information form
* 🎯 Skill-level selection
* 📅 Day-by-day study planning
* ⏱️ Study-hour based recommendations
* 📚 Personalized learning activities
* ✨ Interactive web interface
* 🧹 Clear All functionality
* ⏳ Loading indicator
* ⚠️ Error handling
* 📱 Responsive design

---

# 🏗️ Project Structure

```text
Class_Test_LLM/
│
├── main.py
├── run.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── zero_shot.png
│   ├── few_shot.png
│   └── structured_COT.png
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

### File Description

| File / Folder          | Purpose                                                  |
| ---------------------- | -------------------------------------------------------- |
| `main.py`              | FastAPI application and API endpoints                    |
| `run.py`               | Gemini API integration and prompting logic               |
| `templates/index.html` | Web application interface                                |
| `static/style.css`     | Frontend styling                                         |
| `screenshots/`         | Output screenshots for the three techniques              |
| `.env`                 | Stores the Gemini API key                                |
| `requirements.txt`     | Python dependencies                                      |
| `.gitignore`           | Prevents sensitive/unnecessary files from being uploaded |
| `README.md`            | Project documentation                                    |

---

# ⚙️ Technologies Used

* **Python**
* **FastAPI**
* **Google Gemini API**
* **Prompt Engineering**
* **Large Language Models (LLMs)**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Jinja2**

---

# 🔄 Application Workflow

```text
Student enters academic information
              ↓
Selects prompting technique
              ↓
FastAPI receives the request
              ↓
Prompt is generated
              ↓
Google Gemini processes the prompt
              ↓
Personalized study plan is generated
              ↓
Study plan displayed in the web interface
```

---

# 📊 Prompt Engineering Comparison

| Technique               |      Examples | Approach                          |
| ----------------------- | ------------: | --------------------------------- |
| 🔵 Zero-Shot            |          ❌ No | Direct instructions               |
| 🟣 Few-Shot             |         ✅ 2–3 | Uses examples to guide the output |
| 🟢 Structured Reasoning | ❌ No examples | Systematic and organized analysis |

### Summary

**Zero-Shot:**
The model receives direct instructions without examples.

**Few-Shot:**
The model receives examples that demonstrate the expected style and structure.

**Structured Reasoning:**
The prompt organizes the task into specific steps and asks for concise justifications.

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2. Navigate to the Project

```bash
cd Class_Test_LLM
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Configure Gemini API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

⚠️ **Never upload your API key to GitHub.**

---

# ▶️ Run the Application

Start the FastAPI server using:

```bash
python -m uvicorn main:app --reload
```

Then open the local address provided by Uvicorn in your browser.

---

# 🔐 Security

The Gemini API key is stored in an environment variable instead of being written directly in the source code.

Example `.gitignore`:

```text
.env
venv/
.venv/
__pycache__/
*.pyc
```

This prevents sensitive information and unnecessary files from being uploaded to GitHub.

---

# 🎓 Learning Outcomes

Through this project, the following concepts were practiced:

* Large Language Models (LLMs)
* Generative AI
* Prompt Engineering
* Zero-Shot Prompting
* Few-Shot Prompting
* Structured Prompting
* Gemini API integration
* FastAPI
* REST API development
* Frontend and backend integration
* Environment variable management

---

# 🔮 Future Improvements

Possible future improvements include:

* 📈 Student progress tracking
* 📚 Study-plan history
* 💾 Saving generated study plans
* 📊 Progress dashboard
* 🔔 Study reminders
* 📅 Calendar integration
* 💬 AI-powered study assistant
* 🔄 Automatic study-plan adjustment based on progress

---

# 👩‍💻 Author

**Palwasha Mushtaq**

**M.Phil in Finance | Data Science & AI Learner**

This project was developed as part of an AI and Prompt Engineering assignment to explore practical applications of Large Language Models and different prompting techniques.

---

# ⭐ Conclusion

The **AI Study Coach** demonstrates a practical application of Generative AI and Prompt Engineering.

By implementing and comparing **Zero-Shot, Few-Shot, and Structured Reasoning** techniques, this project shows how prompt design can influence the structure and usefulness of LLM-generated responses.

The application combines **Google Gemini, Python, FastAPI, and a responsive web interface** to create a personalized AI-powered study assistant.

````

**Bas screenshots folder mein ye 3 files rakhna:**

```text
screenshots/
├── zero_shot.png
├── few_shot.png
└── structured_COT.png
````
