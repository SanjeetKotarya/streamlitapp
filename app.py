# Importing necessary libraries
import streamlit as st

# Function to find the largest number among three numbers
def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

# Streamlit app
def main():
    st.title('Find the Largest Among Three Numbers')

    # Input fields for three numbers
    num1 = st.number_input('Enter the first number:')
    num2 = st.number_input('Enter the second number:')
    num3 = st.number_input('Enter the third number:')

    # Button to find the largest number
    if st.button('Find Largest'):
        largest = find_largest(num1, num2, num3)
        st.success(f'The largest number is: {largest}')

if __name__ == '__main__':
    main()
