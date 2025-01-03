import streamlit as st
import requests  


st.markdown(
    """
    <style>
    .stApp {
        background-color: #081f37;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.image("stack_logo.jpeg", width=500)

st.title("StackOverflow Tag Predictor")

predefined_texts = [
    "How to implement binary search in Python?",
    "What is the difference between list and tuple in Python?",
    "How can I deploy a Flask app on Azure?",
    "What is the time complexity of quicksort?",
    "How to use pandas for data analysis?",
    "What are Python decorators and how do they work?",
    "How to connect a database to a Django project?",
    "How to handle missing values in a dataset?",
    "What is the difference between GET and POST in HTTP?",
    "How to create a virtual environment in Python?",
]

# Create a horizontal row of buttons
st.markdown("### Predefined Questions:")
col_buttons = st.columns(len(predefined_texts))

# Use session state to persist the user input
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

for i, text in enumerate(predefined_texts):
    if col_buttons[i].button(f" {i + 1}"):
        st.session_state["user_input"] = text

# Text area for user input
user_input = st.text_area("Enter your text here:", value=st.session_state["user_input"], key="user_text")

#API_URL = "http://127.0.0.1:8000/predict"  
API_URL="https://openclassroomp5-e8a3bgckg7hzdsej.westeurope-01.azurewebsites.net/predict"

if st.button("Get API Response"):
    if user_input.strip():  # Ensure the input is not empty
        try:
            # Send POST request to the Flask API
            response = requests.post(API_URL, json={"text": user_input})
            if response.status_code == 200:
                prediction = response.json().get("prediction", [])
                print('debug: ', prediction)

                # Check if prediction is empty or contains only empty lists
                if not prediction or all(not tags for tags in prediction):
                    st.markdown(
                        """
                        <div style="margin-bottom: 10px;">
                            <span class="label no-tag">No tag predicted</span>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    for tag_list in prediction:
                        tag_labels = ''.join(
                            [f'<span class="label">{tag}</span>' for tag in tag_list]
                        )
                        st.markdown(
                            f"""
                            <div style="margin-bottom: 10px;">
                                {tag_labels}
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                
                # Add CSS for labels
                st.markdown(
                    """
                    <style>
                    .label {
                        display: inline-block;
                        background-color: #4CAF50;
                        color: white;
                        padding: 5px 10px;
                        margin: 2px;
                        border-radius: 5px;
                        font-size: 14px;
                    }
                    .no-tag {
                        background-color: #FFC107; /* Yellow background */
                        color: black; /* Black text */
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter text to get a prediction.")

st.markdown(
    "[Visit StackOverflow Question Site](https://stackoverflow.com/questions)",
    unsafe_allow_html=True,
)
