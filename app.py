import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

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

# Load pickled objects
with open('label_encoders.pkl', 'rb') as file:
    encoder = pickle.load(file)

with open('scaler1.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('carprice.pkl', 'rb') as file:
    model = pickle.load(file)

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
    st.caption("Data Scraping")
    st.caption("Data Cleaning")
    st.caption("Python")
    st.caption("Pandas")
    st.caption("Machine Learning")
    st.caption("Algoirthms in Machine Learning")
    st.caption("Streamlit Application")

def objective():
    st.header("Objective")
    st.write("To Develop a streamlit application to predict the prices of the used cars using Machine Learning Algorithms")

def prerequisites():
    st.header("Prerequisites")
    st.write("1. Python Environment: Install Python on your system.")
    st.write("2. Pandas, Scikit-learn, Matplotlib, Seaborn, Numpy, JSON")

def Approach():
    st.header("Approach")
    st.write("Structuring the Given Dataset")
    st.write("Data Cleansing - Especially on Null values, duplicates and redundancy")
    st.write("Exploratory Data Analysis - Skewness, Outliers handling, Correlation")
    st.write("Getting the dataframe ready for machine learning usng encoders")
    st.write("Choosing the best machine learning algorithms and hypertune if necessary")
    st.write("Export the model as pickle")
    st.write("Develop streamlit application to receive pickle parameters as input and display the predicted results")
    
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
        st.title("Car Dekho Price Prediction")
        
        
        bt = st.selectbox("Body Type",["Select bodytype"]+['Hatchback' ,'SUV', 'Sedan', 'MUV',  'Minivans', 'Wagon'])
        km =st.slider("Kilo Meter", min_value=700, max_value=150000)
        trans = st.selectbox("Transmission",["Select Transmission"]+['Manual','Automatic'])
        owners = st.selectbox("No of Owners",["Select no.of.owner"]+[0,1,2,3,4,5])
        brand = st.selectbox("Brand",["Select Brand"]+['Maruti', 'Ford', 'Tata', 'Hyundai', 'Datsun', 'Honda' ,'Renault', 'Volkswagen',
                                            'Mahindra', 'Skoda', 'MG', 'Kia', 'Toyota', 'Nissan' ,'Fiat', 'Chevrolet',
                                                        'Citroen' ,'Mini', 'Hindustan Motors'])

        model_year =st.slider("Model Year", min_value=1985, max_value=2023)
        # insurance = st.selectbox("Insurance Validity",["Select Insurance Validity"]+['Third Party', 'Comprehensive', 'Zero Dep', 'Not Available'])
        fueltype = st.selectbox("Fuel Type",["Select Fuel Type"]+['Petrol', 'Diesel', 'LPG', 'CNG'])
        mileage = st.slider("Mileage", min_value=10.0, max_value=28.0)
        engine =st.slider("Engine CC", min_value=700, max_value=2000)
        seat = st.slider("No of Seats", min_value = 4, max_value = 8)
        # color = st.selectbox("Color",["Select Color"]+['white', 'red', 'others', 'gray', 'maroon', 'orange', 'silver', 'blue', 'brown',
        #                                                 'yellow', 'black', 'gold', 'green', 'purple'])
        # gears = st.selectbox("Gear Box",["Select Gears"]+[5, 7, 4, 6, 0, 8])
        steering_type = st.selectbox("Steering Type",["Select Steering type"]+['EPAS', 'Electronic', 'Manual', 'Power']) 
        front_brake = st.selectbox("Front Brake",["Select Front Brake type"]+['Disc', 'others']) 
        rear_brake = st.selectbox("Rear Brake",["Select Rear brake type"]+['Disc', 'Drum']) 
        tyre_type = st.selectbox("Tyre Type",["Select Tyre type"]+['Radial', 'Tubeless']) 
        door = st.slider("No of Doors", min_value=4, max_value=5)
        city = st.selectbox("City",["Select City"]+['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata'])

        details1 = []
        
        
        if bt != "Select bodytype":
            encoded_value = encoder["bt"].transform([bt])[0]
            details1.append(int(encoded_value))
        else:
            st.warning("Please choose correct any option in body type box")
        if km:
            details1.append(km)

        if trans != "Select Transmission":
            encoded_value = encoder["transmission"].transform([trans])[0]
            details1.append(int(encoded_value))
        else:
            st.warning("Please choose correct any option in transmission box")
        
        if owners != "Select no.of.owner":
            details1.append(owners)
        else:
            st.warning("Please choose correct any option in owners box")
            
        
        if brand != "Select Brand":
            encoded_value = encoder["oem"].transform([brand])[0]
            details1.append(int(encoded_value))
        else:
            st.warning("Please choose correct any option in brand box")

        if model_year:
            details1.append(float(model_year))
      
        # if insurance != "Select Insurance Validity":
        #     encoded_value = encoder["Insurance Validity"].transform([insurance])[0]
        #     details1.append(int(encoded_value))
        # else:
        #     st.warning("Please choose correct any option in insurance box")

        if fueltype != "Select Fuel Type":
            encoded_value = encoder["Fuel Type"].transform([fueltype])[0]
            details1.append(int(encoded_value))
        else:
            st.warning("Please choose correct any option in fueltype")
        
        if mileage:
            details1.append(mileage)

        if engine:
            details1.append(engine)

        # Add mean values
        max_power_mean = 83.284
        details1.append(max_power_mean)

        torque_mean = 127.384
        details1.append(torque_mean)

        # if color != "Select Color":
        #     encoded_value = encoder["Color"].transform([color])[0]
        #     details1.append(int(encoded_value))
        # else:
        #     st.warning("Please choose correct any option in color box")

        if seat:
            details1.append(seat)
        
        cylinder_mean = 4
        details1.append(cylinder_mean)

        valuespercylinder_mean = 4
        details1.append(valuespercylinder_mean)
        
        Length_mean = 3880.395
        details1.append(Length_mean)

        Width_mean = 1690.101
        details1.append(Width_mean)

        Height_mean = 1542.333
        details1.append(Height_mean)

        wheelbase_mean = 2465.064
        details1.append(wheelbase_mean)

        if door:
            details1.append(door)



        if steering_type != "Select Steering type":
            # city = city.lower()
            encoded_value = encoder["Steering Type"].transform([steering_type])[0]
            details1.append(int(encoded_value))
            print(encoded_value)
        else:
            st.warning("Please choose correct any option in city box")

        if front_brake != "Select Front Brake type":
            # city = city.lower()
            encoded_value = encoder["Front Brake Type"].transform([front_brake])[0]
            details1.append(int(encoded_value))
            print(encoded_value)
        else:
            st.warning("Please choose correct any option in city box")

        if rear_brake != "Select Rear Brake type":
            # city = city.lower()
            encoded_value = encoder["Rear Brake Type"].transform([rear_brake])[0]
            details1.append(int(encoded_value))
            print(encoded_value)
        else:
            st.warning("Please choose correct any option in city box")

        if tyre_type != "Select Tyre type":
            # city = city.lower()
            encoded_value = encoder["Tyre Type"].transform([tyre_type])[0]
            details1.append(int(encoded_value))
            print(encoded_value)
        else:
            st.warning("Please choose correct any option in city box")
        

        # if gears != "Select Gears":
        #     details1.append(gears)
        # else:
        #     st.warning("Please choose correct any option in gears box")
        if city != "Select City":
            # city = city.lower()
            encoded_value = encoder["City"].transform([city])[0]
            details1.append(int(encoded_value))
            print(encoded_value)
        else:
            st.warning("Please choose correct any option in city box")
        # Convert to DataFrame and scale
        details = [details1]
        if len(details1) == 24:
            values_scaled = scaler.transform(details)
        
        #st.write(f"Scaled Input Data: {values_scaled}")
    

        if st.button("Estimate Price"):
            car_price_pred = model.predict(values_scaled)
            st.success(f"Estimated Price: ₹{round(car_price_pred[0][0], 2)}")
    
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.header("About")
            options = ["About the Developer", "Skills take away From This Project", "Objective", 
                    "Prerequisites", "Required Python Libraries", "Approach"]
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
            elif choice == "Approach":
                Approach()


if __name__ == "__main__":
    main()
