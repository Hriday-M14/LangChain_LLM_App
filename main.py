import langchain_helper as lch
import streamlit

streamlit.title("Pet's Name Generator")

animal_type = streamlit.sidebar.selectbox("What is Your Pet?", ("Cat", "Dog", "Parrot"))

if animal_type == "Cat":
    pet_color = streamlit.sidebar.text_area(label="What Color is Your Cat?", max_chars=15)
elif animal_type == "Dog":
    pet_color = streamlit.sidebar.text_area(label="What Color is Your Dog?", max_chars=15)
elif animal_type == "Parrot":
    pet_color = streamlit.sidebar.text_area(label="What Color is Your Parrot?", max_chars=15)

if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    streamlit.text(response['pet_name'])