# FastAPI Sentiment Analysis App

This is a simple web application built using FastAPI for sentiment analysis. The app uses a Hugging Face model as well as pretrained models to predict the sentiment of the provided text.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. Additionally, install the required dependencies:

```bash
pip install fastapi uvicorn transformers  
```
### Running the App

1.  **Clone the repository:**
    

    
   ```
   git clone https://github.com/your-username/fastapi-sentiment-analysis-app.git
   ``` 
    
2.  **Navigate to the project directory:**
    

    
    `cd fastapi-sentiment-analysis-app` 
    
3.  **Run the FastAPI app:**
    
 
    
    `uvicorn main:app --reload` 
    
4.  **Open your web browser and go to** http://127.0.0.1:8000 **to access the app.**
    

## Usage

1.  Enter text in the provided input field.
2.  Click the "Predict" button to get the sentiment analysis results.

## Project Structure

-   **`main.py`**: FastAPI application code.
-   **`templates/`**: Directory containing HTML templates.
    -   `index.html`: HTML template for the app.
-   **`static/`**: Directory containing static files (CSS and JavaScript).
    -   `style.css`: CSS file for styling.
    -   `script.js`: JavaScript file for client-side functionality.

