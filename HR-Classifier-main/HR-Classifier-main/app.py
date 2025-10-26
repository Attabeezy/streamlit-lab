import streamlit as st
import random
import numpy as np
import pickle
import pandas as pd

# Load the model and feature names
with open('decision_tree_model.pkl', 'rb') as file:
    model, feature_names = pickle.load(file)

# Define scenario-based questions for each trait (including the additional ones)
scenarios = {
    'DesireToTakeInitiative': [
        {
            "scenario": """
            You are leading a new project team that is falling behind schedule due to unclear roles. 
            What would you do next?
            """,
            "options": [
                "Take charge and assign roles immediately without consulting the team.",
                "Encourage the team to set up a meeting to discuss roles and responsibilities.",
                "Wait to see if the team resolves the issue on their own.",
                "Consult an external project manager for advice."
            ],
            "correct_option": 2,
            "feedback": {
                1: "Taking charge alone may reduce team collaboration.",
                2: "Encouraging discussion allows team input and promotes shared responsibility.",
                3: "Waiting could cause further delays.",
                4: "Consulting externally may be time-consuming in this scenario."
            }
        },
        {
        "scenario": """
        Your team is falling behind on a major project, and the deadline is quickly approaching. You notice that no one has taken the lead in resolving the issue yet. 
        How do you handle the situation?
        """,
        "options": [
            "Take the initiative and organize a team meeting to address the problem and set new deadlines.",
            "Wait for the project manager to step in and provide guidance on what should be done.",
            "Offer to help the team but let someone else take the lead in solving the issue.",
            "Ignore the situation and focus on your own tasks."
        ],
        "correct_option": 1,
        "feedback": {
            1: "Taking the lead shows initiative and responsibility. This is a key quality in a leader.",
            2: "Waiting for the manager may be easier, but taking initiative sets you apart as a proactive team member.",
            3: "Offering to help is good, but if no one takes the lead, the project may still fall behind.",
            4: "Ignoring the issue can cause delays and reflects a lack of responsibility."
        }
    },
    {
        "scenario": """
        You are in a meeting and realize there’s an opportunity to improve the company’s current process that no one has thought of. Everyone seems busy discussing other topics.
        What do you do?
        """,
        "options": [
            "Speak up and suggest the improvement even if it disrupts the current discussion.",
            "Wait for someone else to bring it up since you’re unsure if your idea will be well-received.",
            "Ask a colleague privately if they think it’s a good idea and then decide whether to share it.",
            "Ignore the idea and continue with the meeting as planned."
        ],
        "correct_option": 1,
        "feedback": {
            1: "Taking the initiative to speak up can result in valuable improvements and show that you're engaged.",
            2: "Waiting for others may mean missing out on the chance to drive change.",
            3: "Getting feedback from a colleague first is smart, but don’t be afraid to take the initiative if it’s a strong idea.",
            4: "Ignoring the opportunity for improvement can lead to stagnation and missed progress."
        }
    },
    {
        "scenario": """
        You are working on a long-term project, and the current strategy is not yielding expected results. You have a new approach in mind that could change the course of the project.
        What is your response?
        """,
        "options": [
            "Take the lead and present your new approach to the team, suggesting a major change in direction.",
            "Wait to see if someone else brings up a new strategy or solution.",
            "Discuss your idea informally with a few colleagues first to gauge their reaction before proposing it to the team.",
            "Stick with the current plan since it’s already in motion, even if you have doubts about its effectiveness."
        ],
        "correct_option": 1,
        "feedback": {
            1: "Taking the lead and suggesting a major change demonstrates strong initiative and leadership.",
            2: "Waiting for others might mean that the project continues to face challenges.",
            3: "Gauging reactions can help, but sometimes direct action is necessary to drive change.",
            4: "Remaining attached to an ineffective plan can hinder progress and shows a lack of confidence."
        }
    }
    ],
    'Competitiveness': [
        {
            "scenario": """
            You are participating in a sales competition at work. A colleague is performing better than you. 
            How do you respond?
            """,
            "options": [
                "Work harder to surpass your colleague’s performance.",
                "Congratulate your colleague and maintain your current approach.",
                "Ask your colleague for tips on how to improve.",
                "Ignore the competition and focus on your long-term goals."
            ],
            "correct_option": 1,
            "feedback": {
                1: "Striving to outperform can motivate you to achieve more.",
                2: "Congratulating them is good but might not help you improve.",
                3: "Seeking tips is helpful but may reduce your drive.",
                4: "Ignoring competition might lead to missed opportunities."
            }
        },
        {
        "scenario": """
        Your team is participating in an important competition that could earn the company a significant reward. During the initial stages, your team is slightly behind, but there is still a chance to catch up.
        How do you handle the situation?
        """,
        "options": [
            "Push yourself and your team to work extra hard, even if it means taking on additional tasks.",
            "Focus on maintaining your current pace, hoping the competition will catch up on their own.",
            "Discuss with your team the possibility of reducing effort to avoid burnout and focus on other projects.",
            "Let others lead, as you believe they have more experience in the competition."
        ],
        "correct_option": 1,
        "feedback": {
            1: "Taking the initiative and working harder to catch up is a strong display of competitiveness and determination.",
            2: "Hoping the competition will catch up may be less effective if others are pushing themselves harder.",
            3: "Reducing effort may relieve stress, but it can show a lack of competitive spirit.",
            4: "Letting others take charge may prevent you from showcasing your own strengths."
        }
    },
    {
        "scenario": """
        You’re in a work environment where several employees are competing for a prestigious role. While you feel confident in your abilities, your peers have more experience. However, you are motivated to show that you’re equally capable.
        What will you do?
        """,
        "options": [
            "Focus on improving your skills and find ways to outshine your peers in the application process.",
            "Support your colleagues and hope that your efforts are acknowledged, without actively competing.",
            "Give up on the role, as you believe the competition is too fierce for someone with less experience.",
            "Focus on your own growth and ignore the competition, trusting that things will work out."
        ],
        "correct_option": 1,
        "feedback": {
            1: "Taking proactive steps to improve your skills and differentiate yourself demonstrates competitiveness and drive.",
            2: "Supporting your colleagues is admirable, but competitive environments often require individuals to stand out.",
            3: "Giving up on the opportunity shows a lack of self-belief and drive to compete.",
            4: "Focusing on growth is important, but actively engaging with the competition can help you achieve your goals."
        }
    },
    {
        "scenario": """
        You are in a team where everyone has been asked to submit a report. There’s no official ranking or reward for the best report, but you feel that this task is a great chance to prove your capabilities.
        How do you approach it?
        """,
        "options": [
            "Go above and beyond to create a thorough, exceptional report to set yourself apart from your colleagues.",
            "Complete the task quickly with adequate quality, but don’t spend extra time improving it.",
            "Ask colleagues for input to make sure the final report is a team effort.",
            "Complete the report and rely on your colleagues' work to meet the expectations."
        ],
        "correct_option": 1,
        "feedback": {
            1: "Creating an exceptional report shows your competitive nature and desire to stand out.",
            2: "Completing the task quickly is efficient, but might not highlight your full potential.",
            3: "Collaborating with others is good, but a competitive approach often requires individual excellence.",
            4: "Relying on others’ work may be a more passive approach and might not reflect your capabilities."
        }
    }
    ],
    'SelfConfidence': [
        {
            "scenario": """
            You are asked to give a presentation to a senior executive team on short notice. 
            How do you handle the situation?
            """,
            "options": [
                "Decline the opportunity because you feel unprepared.",
                "Accept the challenge and rely on your existing knowledge to deliver a good presentation.",
                "Ask for additional time to prepare thoroughly.",
                "Request that someone else give the presentation on your behalf."
            ],
            "correct_option": 2,
            "feedback": {
                1: "Declining may suggest a lack of confidence in your abilities.",
                2: "Accepting the challenge shows confidence and adaptability.",
                3: "Asking for more time can be seen as a reasonable request but may reflect uncertainty.",
                4: "Requesting someone else to take over could harm your reputation."
            }
        },
        {
            "scenario": """
            After receiving critical feedback on a recent project, you are asked to lead the next team meeting. 
            What do you do?
            """,
            "options": [
                "Politely decline, as you feel unsure about your recent performance.",
                "Agree to lead the meeting and use it as an opportunity to show your resilience.",
                "Ask for help from a colleague to lead the meeting with you.",
                "Wait for more positive feedback before taking a leadership role again."
            ],
            "correct_option": 2,
            "feedback": {
                1: "Declining could signal a lack of confidence.",
                2: "Leading despite setbacks demonstrates self-confidence and resilience.",
                3: "Collaborating might help, but it could suggest hesitation in taking full responsibility.",
                4: "Waiting could limit your opportunities for growth."
            }
        },
        {
            "scenario": """
            You are in a job interview and the interviewer asks a difficult question that you did not expect. 
            How do you respond?
            """,
            "options": [
                "Admit that you don’t know the answer and move on to the next question.",
                "Pause briefly to collect your thoughts and provide the best response you can.",
                "Ask for more clarification to buy time before answering.",
                "Shift the conversation to a topic you are more comfortable with."
            ],
            "correct_option": 2,
            "feedback": {
                1: "Admitting you don't know may not reflect well on your confidence.",
                2: "Taking a moment to think shows composure and confidence under pressure.",
                3: "Asking for clarification might help, but should not appear as a stall tactic.",
                4: "Shifting topics can make you seem evasive."
            }
        }
    ],
    'Perseverance': [
        {
            "scenario": """
            You are working on a long-term project that is not progressing as expected due to repeated setbacks. 
            What do you do?
            """,
            "options": [
                "Abandon the project and shift your focus to more attainable goals.",
                "Take a break and return with a fresh perspective to find solutions.",
                "Continue working on the project as you believe persistence will eventually pay off.",
                "Consult a mentor or expert for advice on how to overcome the setbacks."
            ],
            "correct_option": 3,
            "feedback": {
                1: "Abandoning the project suggests a lack of perseverance.",
                2: "Taking a break can be helpful but should not delay progress indefinitely.",
                3: "Staying committed to the project shows perseverance and resilience.",
                4: "Consulting others for advice is wise, but it’s important to stay self-driven."
            }
        },
        {
            "scenario": """
            Your startup has faced several financial challenges and missed key targets. Investors are starting to lose confidence. 
            What’s your next move?
            """,
            "options": [
                "Shut down the business and return the remaining funds to investors.",
                "Push forward by adjusting your strategy and finding new ways to reach your targets.",
                "Blame external factors for the issues and assure investors everything will work out.",
                "Ask your investors for additional time and resources to turn things around."
            ],
            "correct_option": 2,
            "feedback": {
                1: "Shutting down might be premature without exploring all possible solutions.",
                2: "Adjusting strategy and pushing forward demonstrates perseverance.",
                3: "Blaming external factors can appear evasive and might damage credibility.",
                4: "Asking for more time could help, but perseverance is about making progress with existing resources."
            }
        },
        {
            "scenario": """
            You are halfway through a year-long research project when your hypothesis is proven wrong. 
            What do you do?
            """,
            "options": [
                "Abandon the project since the initial hypothesis is no longer valid.",
                "Reframe the project and continue testing new hypotheses.",
                "Seek support from colleagues to help salvage the project.",
                "Wait for new developments in the field that might support your hypothesis."
            ],
            "correct_option": 2,
            "feedback": {
                1: "Abandoning the project would waste the progress you've already made.",
                2: "Reframing the project shows perseverance and adaptability.",
                3: "Seeking support can help, but it’s important to keep driving the project.",
                4: "Waiting passively for new developments could delay potential breakthroughs."
            }
        }
    ],
    'SelfReliance': [
        {
            "scenario": """
            You are assigned a task at work but there are no clear instructions or guidance. 
            What is your first step?
            """,
            "options": [
                "Wait for your supervisor to provide more instructions.",
                "Research the task on your own and begin working based on your findings.",
                "Ask your coworkers for advice on how to proceed.",
                "Request that the task be reassigned to someone more experienced."
            ],
            "correct_option": 2,
            "feedback": {
                1: "Waiting may delay your progress and reflect a lack of self-reliance.",
                2: "Taking initiative and researching on your own shows self-reliance.",
                3: "Asking coworkers for advice can help, but over-reliance on others may slow your development.",
                4: "Reassigning the task could undermine your credibility."
            }
        },
        {
            "scenario": """
            Your team is facing a tight deadline, and everyone is busy with their tasks. 
            How do you ensure your part is completed on time?
            """,
            "options": [
                "Rely on your team members for help whenever you get stuck.",
                "Take ownership of your work and push through challenges on your own.",
                "Ask your manager for an extension to ensure quality.",
                "Delay your tasks to help others and request they do the same for you."
            ],
            "correct_option": 2,
            "feedback": {
                1: "Over-reliance on others may indicate a lack of self-reliance.",
                2: "Taking ownership and pushing through shows strong self-reliance.",
                3: "Asking for extensions frequently can reflect poorly on your ability to meet deadlines.",
                4: "Delaying your tasks could create bottlenecks and harm the overall team’s progress."
            }
        },
        {
            "scenario": """
            You are working remotely and encounter an issue with the project management software. 
            How do you handle the situation?
            """,
                        "options": [
                "Contact the IT department immediately for assistance.",
                "Try troubleshooting the issue yourself before seeking help.",
                "Ask your colleagues if they are experiencing the same problem.",
                "Give up and wait until someone else can help you."
            ],
            "correct_option": 2,
            "feedback": {
                1: "Contacting IT right away can be helpful, but attempting to resolve the issue first demonstrates self-reliance.",
                2: "Troubleshooting independently shows resourcefulness and self-reliance.",
                3: "Asking colleagues may be useful but should not replace your own initiative.",
                4: "Giving up isn’t a viable option in a professional setting."
            }
        }
    ]
}

# Streamlit app structure and aesthetics
st.set_page_config(page_title="Trait Assessment Quiz", layout="wide")

# Display the landscape image above the title
st.image("business-meeting.jpg", use_container_width=True)

# Title and header with Markdown
st.title("🎯 Trait Assessment Quiz")
st.markdown("This quiz helps assess your entrepreneurial traits based on scenario-based questions. Choose the best response for each scenario below.")

# Sidebar with instructions
with st.sidebar:
    st.header("Instructions")
    st.write("1. Read each scenario carefully.")
    st.write("2. Choose the response that best matches how you would react in the given situation.")
    st.write("3. After completing the quiz, click 'Predict' to receive feedback.")
    st.image("diversity-hands.jpg", caption="Entrepreneurship Traits", width=240)

# Re-randomizing the selected scenarios each time the app is rerun
if 'selected_scenarios' not in st.session_state or st.button("Randomize Questions"):
    st.session_state.selected_scenarios = []
    # Randomly select one question from each trait
    for trait, scenario_list in scenarios.items():
        selected_scenario = random.choice(scenario_list)
        st.session_state.selected_scenarios.append(selected_scenario)

# Display scenarios with dropdown for answers
user_answers = []
for index, scenario in enumerate(st.session_state.selected_scenarios):
    st.subheader(f"🔍 Scenario {index + 1} - Trait: {list(scenarios.keys())[index]}")
    st.write(scenario['scenario'])
    
    # Add dropdown for answers with stylish elements
    user_answer = st.selectbox("Choose your answer:", scenario['options'], key=index, help="Select the best response from the list.")
    user_answers.append(user_answer)

# Progress Bar (Optional)
progress = len(user_answers) / len(st.session_state.selected_scenarios)
st.progress(progress)  # Normalize the progress to be between 0.0 and 1.0

# When the user clicks the "Predict" button
if st.button("🧠 Evaluate"):
    st.markdown("### Feedback Summary")
    
    # Calculate and provide feedback
    for index, (scenario, answer) in enumerate(zip(st.session_state.selected_scenarios, user_answers)):
        selected_option_index = scenario['options'].index(answer)
        feedback_message = scenario['feedback'].get(selected_option_index + 1, "No feedback available.")
        st.write(f"**Scenario {index + 1} Feedback:** {feedback_message}")

    # Stylish feedback with color
    st.success("Quiz Completed! Review your feedback above.")

# Add some spacing for visual appeal
st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("Made with ❤️ by Rejoice Osei. All rights reserved.", unsafe_allow_html=True)
