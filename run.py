
import os 
from prompt_toolkit import prompt 
from dotenv import load_dotenv  
import google.generativeai as genai


load_dotenv()


Google_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=Google_API_KEY) 

# text  → actual customer transcript
# prompt → LLM ko instruction
def generate_gemini_content(student_info, technique_prompt): 
    model = genai.GenerativeModel("gemini-3.6-flash")
    if technique_prompt == "zero_shot":
       
       prompt = f"""
       You are an AI Study Coach.

Analyze the following student's academic situation and create a
personalized study plan.

Student name: {student_info['name']}
Subject: {student_info['subject']}
Weak Topics: {student_info['weak_topics']}
Days Lefts in Exams: {student_info['days_left']}
Study Hours Per Day: {student_info['hours']}
Skill Level: {student_info['skill_level']}

Please:
1. Identify the student's weak areas.
2. Prioritize the important topics.
3. Create a day-by-day study schedule.
4. Recommend suitable study activities.

Give the final answer in a clear and easy-to-follow format.
"""
    elif technique_prompt == "few_shot":
        prompt = f"""
    You are an AI Study Coach.
    
    Here are some examples of how study plans should be created.
    
    Example 1:

Student:
A student has an SQL exam in 3 days and struggles mainly with SQL joins.

Recommended Plan:
Day 1: Study INNER, LEFT, RIGHT, and FULL joins.
Day 2: Practice SQL join queries.
Day 3: Complete a mock test and review mistakes.

Example 2:

A student has a Python exam in 7 days and struggles with Object-Oriented Programming. 

Recommended Plan:
Day 1-2: Study classes and objects.
Day 3-4: Study inheritance and polymorphism.
Day 5-6: Practice coding exercises.
Day 7: Final revision and mock test.

Example 3:

A students has a Finance exam in 5 days and struggles with Time Value of Money concepts.

Recommended Plan:
Day 1-2: Study the basics of Time Value of Money.
Day 3-4: Practice calculations and applications.
Day 5: Review and take a mock test.

noe create a personalized study plan for the following student:
Student name: {student_info['name']}
Subject: {student_info['subject']}
Weak Topics: {student_info['weak_topics']}
Days Lefts in Exams: {student_info['days_left']}
Study Hours Per Day: {student_info['hours']}
Skill Level: {student_info['skill_level']}

Create a personalized study plan based on the above information. Please provide a clear and easy-to-follow format.
"""

    elif technique_prompt == "Chain_of_thoughts":
        prompt = f"""
    You are an AI Study Coach.
    Analyze the student's situation systematically.
    
    Student name: {student_info['name']}
    Subject: {student_info['subject']}
    Weak topics: {student_info['weak_topics']}
    Days left in exams: {student_info['days_left']}
    Study hours per day: {student_info['hours']}
    Skill level: {student_info['skill_level']}
    
    1. Identify the student's weak topics.
2. Determine which topics are most important.
3. Consider how many days remain before the exam.
4. Consider how many hours the student can study each day.
5. Recommend suitable learning activities.
6. Generate a final day-by-day study plan.
7. Give a short explanation for why each activity was selected.

Do not reveal hidden chain-of-thought or internal reasoning.
Only provide concise explanations and justifications for the
recommendations.

Format the final answer clearly with:
- Weak Areas
- Topic Priorities
- Day-by-Day Study Plan
- Short Justification
"""

    else:
        raise ValueError("Invalid technique_prompt. Please choose from 'zero_shot', 'few_shot', or 'Chain_of_thoughts'.")

    response = model.generate_content(prompt)
    return response.text    

