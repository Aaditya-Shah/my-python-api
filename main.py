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
    # We changed this line!
    return {"prediction": 12345, "status": "it works!"}