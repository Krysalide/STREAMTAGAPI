
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

user_input = st.text_area("Enter your text here:")


#API_URL = "http://127.0.0.1:8000/predict"  
API_URL="https://openclassroomp5-e8a3bgckg7hzdsej.westeurope-01.azurewebsites.net/predict"


if st.button("Get API Response"):
    if user_input.strip():  # Ensure the input is not empty
        try:
            # Send POST request to the Flask API
            response = requests.post(API_URL, json={"text": user_input})
            if response.status_code == 200:
                prediction = response.json().get("prediction", [])
                
                if prediction:
                    #st.markdown("### Predicted Tags:")
                    
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
                        </style>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.warning("No prediction returned.")
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




