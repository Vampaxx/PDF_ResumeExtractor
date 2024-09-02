# PDF_ResumeExtractor


This project is a Flask application that allows users to upload PDF resumes and extracts relevant information such as Name, Phone Number, Email Address, and Experience using the Groq API. The extracted details are then displayed on the web interface.

## Features

- **PDF Resume Upload**: Users can upload a PDF resume.
- **Resume Parsing**: The application uses the Groq API to extract key information from the uploaded PDF.
- **Display Parsed Information**: Extracted details are presented in a user-friendly format.

## Installation

Follow the steps below to set up the application locally.

### 1. Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/Vampaxx/PDF_ResumeExtractor
```

### 3. Install the Required Dependencies

Make sure you have Python and pip installed. Then install the required dependencies:

```bash

pip install -r requirements.txt
```
### Usage

Run the Flask Application:

Start the application by executing:

```bash

python app.py
```
## DEMO WORKING 



https://github.com/user-attachments/assets/510b9027-65e9-4d15-bb10-340366d4e3f4



### Access the Web Interface:

Open your web browser and go to http://127.0.0.1:5000/. You will see the resume upload form.

### Upload a PDF Resume:

Use the form to select and upload a PDF resume.

### View Parsed Information:

After the upload and parsing, the extracted details will be displayed on the screen




## Project Summary

The PDF Resume Parser application is designed to streamline the process of extracting relevant information from uploaded PDF resumes. By leveraging the Groq API for parsing, this application extracts key details such as the candidate's name, email address, phone number, and project experience. The project aims to enhance user efficiency in managing resumes by providing an easy-to-use interface for uploading and retrieving extracted information.
Approach to the Project

1. Project Setup:
    Begin by setting up a Flask web application framework to handle user interactions and file uploads.
    Organize the project structure to separate concerns, such as API handling, data processing, and UI components.

2. PDF File Handling:
    Implement a function to load and extract text from PDF files using a library like PyPDF2 or PyMuPDF.
    Develop a method for processing file paths to ensure consistency in file naming (e.g., replacing hyphens and spaces with underscores).

3. Data Modeling:
    Use Pydantic to create models that validate and structure the extracted data. This includes models for personal information and project titles.
    Define custom validation logic to ensure that phone numbers are in the correct format.

4. Integration with Groq API:
    Set up the Groq API for parsing the resume data, configuring it to extract the necessary fields from the text.
    Create a prompt template that instructs the API on how to summarize the text and extract the required information.

5. User Interface Development:
    Build a user-friendly interface using HTML and Flask's templating engine, allowing users to upload their resumes easily and view the extracted details.
    Provide clear instructions and feedback to users during the upload and parsing process.

6. Testing and Validation:
    Test the application with various PDF resumes to ensure that it handles different formats and layouts effectively.
    Validate the extracted data to confirm that the application meets the expected output format.

## Challenges                            

During the development of the PDF Resume Parser application, I encountered some challenges, particularly with the deployment process. While I have yet to resolve the issues faced when deploying on Vercel, I view this as an opportunity for growth and learning. Each challenge has provided valuable insights into the intricacies of web application deployment, and I am optimistic about finding a solution. I'm excited to explore new strategies to overcome these hurdles, and I'm confident that this experience will strengthen my skills for future projects!
