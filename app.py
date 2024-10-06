import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
from tensorflow.keras.models import load_model

# Function to convert image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Path to your image
background_image_path = 'imgs/bgimgg.jpg'

# Convert the image to base64
base64_image = get_base64_of_bin_file(background_image_path)


# CSS to inject
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{base64_image}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""
st.set_page_config(
    page_title="DVD Rental Deep Learning",
    page_icon='imgs/dl.png'
)

# Inject CSS with markdown
st.markdown(page_bg_img, unsafe_allow_html=True)

model = load_model('DL_Algo.h5')

# Set page configuration


# Apply CSS styling
st.markdown("""
<style>
h1 {
    color:	#black; /* Change to your desired color */
    font-size: 34px;
}
</style>
""", unsafe_allow_html=True)

def about_the_developer():
    st.header("Developer Details")
    st.image("imgs/saro.jpg", caption="Saravana Kumar T", width=250)
    st.subheader("Contact Details")
    st.write("Email: saromaddymca@gmail.com")
    st.write("Phone: 8940574870")
    st.write("[LinkedIn ID](https://www.linkedin.com/in/sarokumar/)")
    st.write("[github.com](https://github.com/saromaddy)")


def skills_take_away():
    st.header("Skills Take Away From This Project")
    st.caption("Data Cleaning and Preprocessing")
    st.caption("Feature Engineering for Neural Networks")
    st.caption("Building and Training Artificial Neural Networks")
    st.caption("Model Evaluation and Optimization")
    st.caption("Postgre SQL")
    st.caption("Deploying Deep learning models using AWS and Streamlit")
    st.caption("Documentation and Reporting")

def objective():
    st.header("Objective")
    st.write("To Develop a streamlit application to predict the prices movies from DVD rental sample database using Deep Learning")

def prerequisites():
    st.header("Prerequisites")
    st.write("1. Python Environment: Install Python on your system.")
    st.write("2. Pandas, Scikit-learn, Matplotlib, Seaborn, Numpy, Tensorflow")

def main():
    option = st.sidebar.radio("Navigation", ["Home", "App Page","About Developer"])
    if option == "Home":
        st.title("DVD Rental - Postgre SQL - Deep Learning")
        st.write("""
        The DVD Rental sample dataset is a PostgreSQL database designed for learning and practicing SQL queries and database management concepts.
        It contains information related to a fictional DVD rental store, with tables representing customers, films, rentals, staff, and inventory.

        The database includes 16 tables that model the store's business operations, such as rental transactions, payments, and film categories. 
        Each table is interconnected through foreign keys, facilitating complex queries like joining customer information with rental history or inventory details. 
        
        This dataset is ideal for practicing database normalization, indexing, and SQL query optimization. 
        It’s commonly used in educational contexts to demonstrate relational database principles.

        By using this sample dataset, this project attempts to predict the amount of rental using Deep Learning
        """)
    
    elif option == "App Page":
        st.title("DVD Rental Deep Learning Project")
        
        
        # rental_duration = st.selectbox("Rental Duration",["Select Rental Duration"]+[3,4,5,6,7])
        rental_rate =st.slider("Rental_rate", min_value=0, max_value=10)
        length = st.slider("Length of the movie", min_value = 45, max_value=185)
        replacement_cost = st.selectbox("Replacement Cost",["Select Replacement Cost"]+[9.99, 10.99, 11.99, 12.99, 13.99, 14.99, 15.99, 16.99, 17.99, 18.99, 19.99, 20.99, 21.99, 22.99, 23.99, 24.99, 25.99, 26.99, 27.99, 28.99, 29.99])
        rating = st.selectbox("Rating",["Select Rating"]+['PG-13','NC-17','PG','R','G'])
        category = st.selectbox("Category",['Select Category']+['Horror', 'Documentary', 'New', 'Classics', 'Games', 'Sci-Fi',
       'Foreign', 'Family', 'Travel', 'Music', 'Sports', 'Comedy',
       'Drama', 'Action', 'Children', 'Animation'])
        active = st.selectbox("Status",['Select Status']+['Active','Not Active'])
        # rental_month = st.selectbox("Rental_month",['Select Rental Month']+[6,7,8])
        # rental_day = st.slider("Rental Day", min_value = 1, max_value=31)
        # return_month = st.selectbox("Return_month",['Select Return Month']+[6,7,8])
        rental_actual_duration = st.slider("Rental_actual_duraton", min_value = 1, max_value=100)
        

        details1 = []
        
        
        # if rental_duration != "Rental Duration":
        #     details1.append(float(rental_duration))
        # else:
            # st.warning("Please choose correct any option in body type box")
        if rental_rate:
            details1.append(float(rental_rate))
        if length:
            details1.append(float(length))    
        if replacement_cost != "Select Replacement Cost":
            details1.append(float(replacement_cost))
        else:
            st.warning("Please choose Rental Duration")
        if rating != "Select Rating":
            rating_array = ['PG-13','NC-17','PG','R','G']
            num_rating = rating_array.index(rating)
            details1.append(float(num_rating))
        else:
            st.warning("Please choose Rating")

        if category != "Select Category":
            array = ['Horror', 'Documentary', 'New', 'Classics', 'Games', 'Sci-Fi',
            'Foreign', 'Family', 'Travel', 'Music', 'Sports', 'Comedy',
            'Drama', 'Action', 'Children', 'Animation']
            num = array.index(category)
            details1.append(float(num))
        else:
            st.warning("Please Select Category")           
        if active != 'Select Status':
            status = ['Active','Not Active']
            num_stat = status.index(active)
            details1.append(float(num_stat))
        else:
            st.warning("Please Select Status")
        # if rental_month:
        #     details1.append(float(rental_month))
        # if rental_day:
        #     details1.append(float(rental_day))
        # if return_month:
        #     details1.append(float(return_month))
        # if return_day:
        #     details1.append(float(return_day))\
        if rental_actual_duration:
            details1.append(float(rental_actual_duration))

        # details = [details1]

        
        #st.write(f"Scaled Input Data: {values_scaled}")
    

        if st.button("Estimate Price"):
            dvd_amount = model.predict(np.array([details1]))
            st.success(f"Estimated Price: {round(dvd_amount[0][0], 2)}")
        
    
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.header("About")
            options = ["About the Developer", "Skills take away From This Project", "Objective", 
                    "Prerequisites"]
            choice = st.radio("Go to", options)

        with col2:
            if choice == "About the Developer":
                about_the_developer()
            elif choice == "Skills take away From This Project":
                skills_take_away()
            elif choice == "Objective":
                objective()
            elif choice == "Prerequisites":
                prerequisites()
         


if __name__ == "__main__":
    main()
