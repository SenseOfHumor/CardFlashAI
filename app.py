import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from NLP import askGemini
from TOOLS import get_dict
import PyPDF2 as pdf
import random

load_dotenv()

st.title("CARDIFY.AI 🂡")
st.caption("An AI-powered flashcard generator")
response = ""

def input_pdf_data(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += str(page.extract_text())
    return text

input_pdf = st.file_uploader("Upload your notes as pdf", type=["pdf"])

question_answer = []

if st.button("Generate Flashcards",use_container_width=True):
    ## st.caption("Please wait while we generate the flashcards...")
    if input_pdf is not None:
        text = input_pdf_data(input_pdf)
        response = askGemini(text)
        response_store = get_dict(response)
        
        for q, a in response_store.items():
            question_answer.append([q, a])
        
        # # Debug: Check if question_answer is populated
        # st.write("Flashcards generated:", question_answer)
        
        # Store question_answer in session state to persist it across interactions
        st.session_state.question_answer = question_answer
    else:
        st.write("Please upload a PDF file")

if response:
    st.caption("Flashcards generated successfully!")
    st.toast("Flashcards generated successfully!")

st.caption("The tool may sometimes run into issues due to the complexity of the input. Please try again if you encounter any errors.")
tab1, tab2, tab3 = st.tabs(["Flashcards", "About Me", "Copyright"])

with tab1:

    col1, col2 = st.columns(2)
    # Session state initialization
    if "show_question" not in st.session_state:
        st.session_state.show_question = False

    if "show_answer" not in st.session_state:
        st.session_state.show_answer = False

    if "current_qa" not in st.session_state:
        st.session_state.current_qa = None

    if "question_answer" not in st.session_state:
        st.session_state.question_answer = []

    def draw_question():
        if st.session_state.question_answer:
            st.session_state.current_qa = random.choice(st.session_state.question_answer)
            st.session_state.show_question = True
            st.session_state.show_answer = False

    def show_answer():
        st.session_state.show_answer = True

    with col1:
        if st.button("Draw question", use_container_width=True):
            draw_question()

    if st.session_state.show_question and st.session_state.current_qa:
        st.markdown("### Question 🧠")
        st.markdown(f"{st.session_state.current_qa[0]}")

    with col2:
        if st.button("Show answer", use_container_width=True):
            show_answer()

    if st.session_state.show_answer and st.session_state.current_qa:
        st.markdown("### Answer 📚")
        st.write(st.session_state.current_qa[1])


with tab2:
    st.markdown("""
    # About Me

    ## 👋 Hi there!

    My name is **Swapnil** and I'm a Computer Science major at NJIT. I have a passion for building programs involving generative AI that solve real-world problems. Currently, I'm working on my SaaS product and learning full stack development using ReactJS and NextJS.

    Feel free to connect with me on my social platforms:

    - [LinkedIn](https://www.linkedin.com/in/swapnil-deb-3096b2207/)
    - [GitHub](https://github.com/SenseOfHumor)
    - [Devpost](https://devpost.com/swa2314?ref_content=user-portfolio&ref_feature=portfolio&ref_medium=global-nav)

    ---

    ### 🔧 I'm Currently Working On:
    - **SaaS Product Development:** Developing a software as a service product aimed at addressing real-world challenges.
    - **Full Stack Development:** Learning and building projects using ReactJS and NextJS to enhance my skills in full stack development.

    ---

    Thank you for visiting my profile! Feel free to reach out if you have any questions or collaboration ideas.

    """)

    
with tab3:
    st.markdown("### Copyright")
    st.markdown("""# CARDIFY 🂡

## Copyright and Fair Use Disclaimer

**CARDIFY 🂡** (the "Tool") is developed and maintained by Swapnil Deb. All rights reserved. 

---

### 📜 Fair Use Notice:
This Tool is intended solely for educational and informational purposes. The Tool is provided "as is" without any warranties or guarantees of any kind, express or implied. By using this Tool, you agree that the developer is not responsible for ensuring academic integrity or preventing any form of misuse.

---

### 🎓 Academic Integrity:
Users of this Tool are responsible for adhering to their respective institutions' policies on academic integrity and plagiarism. The developer assumes no liability for any actions taken by users that violate such policies.

---

### 🚫 Misuse:
The developer disclaims any responsibility for any misuse of the Tool. Users are solely responsible for how they use the Tool and for any consequences arising from its use.

---

By using this Tool, you acknowledge that you have read, understood, and agree to abide by this disclaimer.

                """)