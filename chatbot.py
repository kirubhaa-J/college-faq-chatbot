faq = {
    "college timing": "The college runs from 9 AM to 4 PM.",
    "hod": "The current HOD is Dr. Suresh Kumar.",
    "fees": "Contact the admin office for fee details.",
    "location": "The college is located in Coimbatore.",
    "bye": "Thank you! Have a nice day 😊"
}

print("👩 Kirubhaa's College Chatbot 🤖")
print("----------------------------------")

while True:
    question = input("You: ").lower()
    if question in faq:
        print("Bot:", faq[question])
        if question == "bye":
            break
    else:
        print("Bot: Sorry, I don't know the answer to that.")