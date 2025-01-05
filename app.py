import streamlit as st
import requests  


# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #081f37;
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
st.markdown(
    """
    <style>
    .stApp {
        background-color: #081f37;
        color: white;
    }
    button[aria-pressed="true"] {
        background-color: #008CBA !important; /* Couleur initiale */
        color: white !important; /* Texte en blanc */
        border: none !important; /* Suppression de la bordure */
    }
    button[aria-pressed="true"]:hover {
        background-color: #007B9A !important; /* Couleur au survol */
    }
    .stButton > button {
        min-width: 150px; /* Largeur minimale */
        width: auto; /* Laissez les boutons s'adapter à leur contenu */
        white-space: normal; /* Permet aux noms longs de se répartir sur plusieurs lignes */
        word-wrap: break-word; /* Ajoute un retour à la ligne si nécessaire */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.image("stack_logo.jpeg", width=500)

st.title("StackOverflow Tag Predictor")




# predefined_texts = [
#     "ECMAScript 6 introduced the let declaration keyword. I've heard that it's described as a local variable, but I'm still not quite sure how it behaves differently than the var keyword. What are the differences? When should let be used instead of var?",
#     "What is the difference between using angle brackets and quotes in an include directive? #include <filename> #include \"filename\"",
#     "How can I change the class of an HTML element in response to an onclick or any other events using JavaScript?",
#     "I have a Unicode string in Python, and I would like to remove all the accents (diacritics). I found on the web an elegant way to do this (in Java): convert the Unicode string to its long normalized form (with a separate character for letters and diacritics) and remove all the characters whose Unicode type is \"diacritic\". Do I need to install a library such as pyICU or is this possible with just the Python standard library? And what about python 3? Important note: I would like to avoid code with an explicit mapping from accented characters to their non-accented counterpart.",
#     "TypeScript 3.0 introduces unknown type, according to their wiki: unknown is now a reserved type name, as it is now a built-in type. Depending on your intended use of unknown, you may want to remove the declaration entirely (favoring the newly introduced unknown type), or rename it to something else. What is difference between unknown and any? When should we use unknown over any?",
#     "AWS Cloud Map allows you to set up some namespace for your VPC, and then assign names within that namespace to individual services. The names can either be A) privately discoverable only by API calls, B) discoverable via API calls or via DNS privately within the VPC, or C) discoverable via public DNS and by API calls. ECS can interact with Cloud Map to automatically register services. All this is referred to in AWS ECS as Service Discovery. AWS ECS also has a relatively new thing called Service Connect. It leverages Cloud Map but also adds a sidecar \"proxy\" container to your ECS service, effectively creating an automatic service mesh.",
#     "I am trying to insert some text data into a table in SQL Server 9. The text includes a single quote '. How do I escape that? I tried using two single quotes, but it threw me some errors. eg. insert into my_table values('hi, my name''s tim.');",
#     "I have the following DataFrame (df):\n\nimport numpy as np\nimport pandas as pd\n\ndf = pd.DataFrame(np.random.rand(10, 5))\n\nI add more column(s) by assignment:\ndf['mean'] = df.mean(1)\n\nHow can I move the column mean to the front, i.e. set it as first column leaving the order of the other columns untouched?"
# ]

predefined_texts = [
    "ECMAScript 6 introduced the let declaration keyword. I've heard that it's described as a local variable, but I'm still not quite sure how it behaves differently than the var keyword. What are the differences? When should let be used instead of var?",
    "I worked on an embedded system this summer written in straight C. It was an existing project that the company I work for had taken over. I have become quite accustomed to writing unit tests in Java using JUnit but was at a loss as to the best way to write unit tests for existing code (which needed refactoring) as well as new code added to the system.\n\nAre there any projects out there that make unit testing plain C code as easy as unit testing Java code with JUnit? Any insight that would apply specifically to embedded development (cross-compiling to arm-linux platform) would be greatly appreciated.",
    "How can I change the class of an HTML element in response to an onclick or any other events using JavaScript?",
    "I have a Unicode string in Python, and I would like to remove all the accents (diacritics). I found on the web an elegant way to do this (in Java): convert the Unicode string to its long normalized form (with a separate character for letters and diacritics) and remove all the characters whose Unicode type is \"diacritic\". Do I need to install a library such as pyICU or is this possible with just the Python standard library? And what about python 3? Important note: I would like to avoid code with an explicit mapping from accented characters to their non-accented counterpart.",
    "TypeScript 3.0 introduces unknown type, according to their wiki: unknown is now a reserved type name, as it is now a built-in type. Depending on your intended use of unknown, you may want to remove the declaration entirely (favoring the newly introduced unknown type), or rename it to something else. What is difference between unknown and any? When should we use unknown over any?",
    "AWS Cloud Map allows you to set up some namespace for your VPC, and then assign names within that namespace to individual services. The names can either be A) privately discoverable only by API calls, B) discoverable via API calls or via DNS privately within the VPC, or C) discoverable via public DNS and by API calls. ECS can interact with Cloud Map to automatically register services. All this is referred to in AWS ECS as Service Discovery. AWS ECS also has a relatively new thing called Service Connect. It leverages Cloud Map but also adds a sidecar \"proxy\" container to your ECS service, effectively creating an automatic service mesh.",
    "I am trying to insert some text data into a table in SQL Server 9. The text includes a single quote '. How do I escape that? I tried using two single quotes, but it threw me some errors. eg. insert into my_table values('hi, my name''s tim.');",
    "I have the following DataFrame (df):\n\nimport numpy as np\nimport pandas as pd\n\ndf = pd.DataFrame(np.random.rand(10, 5))\n\nI add more column(s) by assignment:\ndf['mean'] = df.mean(1)\n\nHow can I move the column mean to the front, i.e. set it as first column leaving the order of the other columns untouched?"
]


button_labels = [
    "javascript",
    "C++ C",
    "CSS",
    "Python",
    "TypeScript",
    "AWS",
    "SQL",
    "Pandas"
]
assert len(predefined_texts) == len(button_labels), "Number of predefined texts and button labels should be the same."

# Create a horizontal row of buttons
st.markdown("### Predefined Questions:")
col_buttons = st.columns(len(predefined_texts))


if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

cols_line1 = st.columns(4)
for i in range(4):
    if cols_line1[i].button(button_labels[i]):
        st.session_state["user_input"] = predefined_texts[i]

# Second row of 4 buttons
cols_line2 = st.columns(4)
for i in range(4, 8):
    if cols_line2[i - 4].button(button_labels[i]):
        st.session_state["user_input"] = predefined_texts[i]

# Text area for user input
user_input = st.text_area("Enter your text here:", value=st.session_state["user_input"], key="user_text")

#API_URL = "http://127.0.0.1:8000/predict"  
API_URL="https://openclassroomp5-e8a3bgckg7hzdsej.westeurope-01.azurewebsites.net/predict"

if st.button("Get API Response"):
    if user_input.strip():  
        try:
            # Send POST request to the Flask API
            response = requests.post(API_URL, json={"text": user_input})
            if response.status_code == 200:
                
                prediction = response.json().get("prediction", [])
                print('Model prediction: ', prediction)
                #st.write("Debug: ", prediction) # use in dev mode only

                
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
        st.warning("Please enter text to get a prediction. You can also use the predefined questions.")

st.markdown(
    "[Visit StackOverflow Question Site to load some questions](https://stackoverflow.com/questions)",
    unsafe_allow_html=True,
)
