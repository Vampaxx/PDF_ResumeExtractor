from flask import Flask, request, render_template, flash, redirect
import os
from main import ResumeProcessor

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

UPLOAD_FOLDER = "uploaded_pdf"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16MB
ALLOWED_EXTENSIONS = {'pdf'}

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the file is a PDF."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename    = file.filename
        file_path   = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Initialize the ResumeProcessor with the uploaded file path
        resume_processor    = ResumeProcessor(file_path)
        parsed_data         = resume_processor.process_resume()  # This should return the parsed dictionary
        
        return render_template('index.html', parsed_data=parsed_data)
    
    flash('File type not allowed. Please upload a PDF file.')
    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)
