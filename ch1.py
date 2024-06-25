
import random

# Define a dictionary of malaria symptoms
malaria_symptoms = {
    "fever": "Have you had a fever in the past 24 hours?",
    "chills": "Have you experienced chills or felt cold recently?",
    "flu_like": "Have you had flu-like symptoms such as headache, muscle pain, or fatigue?",
    "nausea": "Have you experienced nausea or vomiting?",
    "diarrhea": "Have you had diarrhea recently?",
    "abdominal_pain": "Have you experienced abdominal pain or cramping?"
}

# Define a function to ask the user about their symptoms
def ask_symptoms():
    symptoms = []
    for symptom, question in malaria_symptoms.items():
        response = input(question + " (yes/no): ")
        if response.lower() == "yes":
            symptoms.append(symptom)
    return symptoms

# Define a function to diagnose malaria based on the user's symptoms
def diagnose_malaria(symptoms):
    if len(symptoms) >= 2:
        print("You may have malaria. Please seek medical attention immediately.")
    else:
        print("You do not appear to have malaria. However, it's always best to consult a doctor if you're experiencing symptoms.")

# Define a function to provide information about malaria
def about_malaria():
    print("Malaria is a serious disease caused by a parasite that is transmitted through the bite of an infected mosquito.")
    print("It can cause fever, chills, flu-like symptoms, nausea, diarrhea, and abdominal pain.")
    print("If left untreated, malaria can be life-threatening.")

# Define a function to provide information about the Against Malaria Foundation
def about_amf():
    print("The Against Malaria Foundation is a charity that works to prevent the spread of malaria by distributing insecticide-treated bed nets.")
    print("They have distributed over 82 million bed nets in the past 14 years, protecting millions of people from malaria.")
    print("You can help support their efforts by donating to their cause.")

# Define a function to handle user input
def handle_input(user_input):
    if user_input.lower() == "symptoms":
        symptoms = ask_symptoms()
        diagnose_malaria(symptoms)
    elif user_input.lower() == "about malaria":
        about_malaria()
    elif user_input.lower() == "about amf":
        about_amf()
    elif user_input.lower() == "donate":
        print("Thank you for your interest in donating to the Against Malaria Foundation!")
        print("Please visit their website to make a donation.")
    else:
        print("I didn't understand that. Please try again.")

# Run the chatbot
print("Welcome to the Malaria Symptom Detection Chatbot!")
while True:
    user_input = input("What would you like to do? (symptoms, about malaria, about amf, donate, or quit): ")
    if user_input.lower() == "quit":
        break
    handle_input(user_input)