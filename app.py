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
    page_title="Car Price Prediction",
    page_icon='imgs/carlogo.png'
)

# Inject CSS with markdown
st.markdown(page_bg_img, unsafe_allow_html=True)

model = load_model('DL_Algo.h5')

# Set page configuration


# Apply CSS styling
st.markdown("""
<style>
h1 {
    color: red; /* Change to your desired color */
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
    st.caption("Data Fetching from PostgreSQL")
    st.caption("Data Cleaning")
    st.caption("EDA")
    st.caption("Python")
    st.caption("Pandas")
    st.caption("Deep Learning")
    st.caption("Streamlit Application")

def objective():
    st.header("Objective")
    st.write("To Develop a streamlit application to predict the prices movies using Deep Learning")

def prerequisites():
    st.header("Prerequisites")
    st.write("1. Python Environment: Install Python on your system.")
    st.write("2. Pandas, Scikit-learn, Matplotlib, Seaborn, Numpy, Tensorflow")

def main():
    option = st.sidebar.radio("Navigation", ["Home", "App Page","About Developer"])
    if option == "Home":
        st.title("About Car Dekho")
        st.write("""
        CarDekho.com is India's leading car search venture that helps users buy cars that are right for them. 
        Its website and app carry rich automotive content such as expert reviews, detailed specs and prices, 
        comparisons as well as videos and pictures of all car brands and models available in India. 
        The company has tie-ups with many auto manufacturers, more than 4000 car dealers, and numerous financial institutions to 
        facilitate the purchase of vehicles.
        """)
        # st.image(r"C:\Users\shank\Desktop\car_dheko\CarDekho-FY22-social.jpg")
        st.write("""
        CarDekho.com has launched many innovative features to ensure that users get an immersive experience of the car 
                 model before visiting a dealer showroom. These include a Feel The Car tool that gives 360-degree interior/exterior 
                 views with sounds of the car and explanations of features with videos; search and comparison by make, model, price, 
                 features; and live offers and promotions in all cities. The platform also has used car classifieds wherein users can 
                 upload their cars for sale, and find used cars for buying from individuals and used car dealers.
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
                    "Prerequisites", "Required Python Libraries"]
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
            elif choice == "Required Python Libraries":
                required_python_libraries()


if __name__ == "__main__":
    main()
