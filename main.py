from fastapi import FastAPI

# Create the main app
app = FastAPI()

# Define a "route" or "endpoint" for the main URL
@app.get("/")
def read_root():
    return {"message": "Hello from my Vercel API!"}

# You can add more routes
@app.get("/predict")
def predict():
    # Later, your ML model code will go here
    return {"prediction": 42}