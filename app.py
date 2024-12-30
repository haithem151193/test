import streamlit as st  # import the streamlit library
st.title('Welcome to BMI Calculator') # give a title to our app
weight = st.number_input("Enter your weight (in kgs)") # TAKE WEIGHT INPUT in kgs
status = st.radio('Select your height format: ', ('cms', 'meters', 'feet')) # TAKE HEIGHT INPUT(radio button to choose height format)
if(status == 'cms'): # user can choose cms ( cms means Centimeters)
    height = st.number_input('Centimeters') # user should enter his height

    try:
        bmi = weight / ((height/100)**2) # if user enter a number user: bmi must calculated according to that formula
    except:
        st.text("Enter some value of height") #if user doesn't enter any thing: a warning message must be displayed

elif(status == 'meters'): # we repeat the same steps as for cms but instead of cms, the user choose meters
    # take height input in meters
    height = st.number_input('Meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")

else: # we repeat the same steps as for cms but instead of cms, the user choose feet
    height = st.number_input('Feet')
    # 1 meter = 3.2 feet
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")

if(st.button('Calculate BMI')):# If user check click on calculate BMI button

    st.text("Your BMI Index is {}.".format(bmi))  # a message should be displayed that contains BMI of user according to its values of weight and height

    # give the interpretation of BMI index
    if(bmi < 16): # if bmi < 16
        st.error("You are Extremely Underweight") # error message "You are Extremely Underweight"
    elif(bmi >= 16 and bmi < 18.5): # if 16 =< bmi < 18.5
        st.warning("You are Underweight") # error message "You are Underweight"
    elif(bmi >= 18.5 and bmi < 25): # if 18.5 =< bmi < 25
        st.success("Healthy") # error message "Healthy"
    elif(bmi >= 25 and bmi < 30): # if 25 =< bmi < 30
        st.warning("Overweight")  # error message "Overweight"
    elif(bmi >= 30): # if bmi > = 30
        st.error("Extremely Overweight") # error message "Extremely Overweight"
