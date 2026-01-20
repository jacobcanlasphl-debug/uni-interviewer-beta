import streamlit as st
import random

# -------------------------------
# Full CASPer Questions
# -------------------------------
casper_questions = [
    """You are an employee at a retail store, and you overhear an interaction between a customer and another employee at the cash register. The customer is here to return an item; however, he does not have a receipt for the purchased item and claims to have paid in cash. Despite assurances by the customer that he did buy the item at your store, your colleague informs the customer that, while he can provide store credit or an exchange, store policy does not allow refunds of more than $20 without a receipt. The customer informs your colleague that he really needs a refund given that this was a birthday purchase for his daughter, but now he desperately requires that money to buy his daughter’s prescription medication. You are the store manager, your colleague turns to you for advice. As the store manager, would you give this customer a refund? Why or why not?""",
    
    """You are friends with both Daphne and Natalie. They have planned to take a trip together, which is three months away. Daphne has started making the travel arrangements. After first confirming with Natalie, she put down a deposit on a rental house. One week later, she asked Natalie to contribute her share of the deposit. Natalie emailed her back and said that she was no longer able to take the trip. Since the trip was still three months away, Natalie stated she was confident that Daphne could find somebody to take her place and therefore would not contribute to the deposit. Daphne is upset by this response, and she turns to you for advice. What would you say to her?""",
    
    """Role: You are a co-worker. You work the opening shift at a coffee shop. Your co-worker, Matthew, is chronically late to work. Another co-worker, May, tells you she is frustrated that Matthew is not doing his fair share of work, especially because your mornings are so busy and the shop is already understaffed. Do you agree with May's frustration? Why or why not? What could your manager do to prevent similar situations from happening in the future? How important is punctuality in a workplace?""",
    
    """Role: You are a friend. Your friend Aaron is worried about his brother Nathan, who recently went through a divorce and lost his job. Aaron wants to visit Nathan across the country, but Aaron has a big work conference coming up. He’s afraid that missing the conference will exclude him from a promotion. No other family or friends are available to be with Nathan at this time, and Nathan can’t afford to travel himself. What advice would you offer your friend, whose brother is struggling? Explain your reasoning. Would you offer monetary assistance to help your friend’s brother? Why or why not? Imagine you learn that your friend’s brother has a gambling problem which contributed to his recent hardships. Would your response change? Explain your response.""",
    
    """You are a member of a study group and you observe members of your group having a heated conversation. Mike and John are confronting Sarah about her inconsistent contribution to the study group. Mike and John are upset that Sarah did not contribute to the study session today and accuse her of not being prepared. Sarah defends herself by saying that she has been busy writing an important paper. Mike and John inform her that they also had the same paper due and, despite that, were able to show up prepared for the session. They then accuse her of regularly coming to tutorials unprepared, suggesting that she’s only learning from the information that they have provided during the study sessions. Sarah informs them that she has been under a lot of stress and that they are not being fair to her. She prepares to leave due to their “negativity”.""",
    
    """You are sitting in on a conversation between Eric and Chloe, two volunteers under Mary, the volunteer coordinator. You are a colleague who also volunteers under Mary. Chloe and Eric receive thank‑you notes for their volunteer work; Mary’s note to Chloe contains cash with a message encouraging her to “get yourself a treat,” but Eric’s note contains only thanks. Both know that Eric put in most of the effort helping Mary the previous week. Chloe wonders whether Mary meant for her to share the money and says she could really use it. Eric later sees the cash and points out that he was the one who helped Mary the most. Chloe turns to you and asks what she should do in this situation. Mary, the volunteer coordinator, sent thank-you notes to both Chloe and Eric for their volunteering efforts, but only Chloe’s note included money. What, if anything, should Chloe do in this situation? Explain your reasoning."""
]

# -------------------------------
# Full KIRA Questions
# -------------------------------
kira_questions = [
    "Tell me about yourself.",
    "Why do you want to attend our program?",
    "Tell us about a time when you overcame a difficult challenge.",
    "Describe one of your favorite hobbies and why it is important to you.",
    "How do you work under pressure?",
    "What is your greatest strength and weakness?",
    "If we asked a close friend or family member to describe you, what would they say?",
    "What does 'leadership' mean to you?",
    "What professional skills do you excel in?",
    "What did you have for lunch/dinner?",
    "What is your best achievement?",
    "Describe a recent dream you had.",
    "Do you agree that most people act out of altruism rather than self interest?",
    "Tell me about something funny that happened to you recently.",
    "Tell us about a time you had to collaborate with others. What qualities do you think are needed for strong teamwork to take place?",
    "How do you effectively prioritize when faced with multiple important tasks at once?",
    "Tell us about a time when you had to defend an unpopular idea or opinion. How did you make your voice heard, and what was the outcome?",
    "Tell us something about yourself that isn’t in your application materials.",
    "What three terms would you use to define yourself?",
    "Who is your role model?",
    "Tell us about your greatest strength. How have you developed this strength and how has it helped you succeed?",
    "What factors contributed to your decision to apply for a seat in this program? Tell us about your top three.",
    "Please tell me about an experience where you led a team that consisted of a group of very different individuals. What did you do to lead the team to accomplish the objective, and what was the outcome?",
    "Outside of school and work, to what activity do you dedicate most of your time? Why is this important to you?",
    "Which do you prioritize, social responsibility or profit? Why do you think one should be prioritized over the other?",
    "Tell us about a time when you had to come to a compromise with a colleague.",
    "How would you explain social media (e.g., Instagram, Facebook, Twitter, etc.) to someone 80 years old?"
]

# -------------------------------
# Function to generate mock AI feedback
# -------------------------------
def generate_feedback(interview_type):
    if interview_type == "CASPer":
        quartile = random.randint(1, 4)
        improvements = [
            "Provide more detailed reasoning and ethical considerations.",
            "Consider multiple perspectives in your answer.",
            "Explain your decision-making process clearly.",
            "Include possible consequences for each action."
        ]
        feedback_text = f"Quartile Score: {quartile}/4\nFeedback: {random.choice(improvements)}"
    else:
        score = random.randint(1, 5)
        improvements = [
            "Be more specific with examples.",
            "Elaborate on how your skills helped in the situation.",
            "Use structured responses with clear beginning, middle, and end.",
            "Highlight measurable achievements."
        ]
        feedback_text = f"Score: {score}/5\nFeedback: {random.choice(improvements)}"
    return feedback_text

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("💡 Local Interview Practice: CASPer & KIRA")

interview_type = st.radio("Choose interview type:", ("CASPer", "KIRA"))

# Pick a random question
question = random.choice(casper_questions) if interview_type == "CASPer" else random.choice(kira_questions)
st.subheader("Question:")
st.write(question)

# User input
answer = st.text_area("Your Answer:", height=200)

# Submit button
if st.button("Submit Answer"):
    if not answer.strip():
        st.error("Please write an answer!")
    else:
        feedback = generate_feedback(interview_type)
        st.subheader("📝 AI Feedback")
        st.write(feedback)

