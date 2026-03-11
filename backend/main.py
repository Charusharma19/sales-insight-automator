from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import pandas as pd

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Sales Insight API running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    try:

        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)

        elif file.filename.endswith(".xlsx"):
            df = pd.read_excel(file.file)

        else:
            return {"error": "Only CSV or Excel allowed"}

        # simple summary (NO AI)
        rows = len(df)
        columns = len(df.columns)

        summary = f"Dataset contains {rows} rows and {columns} columns. Sales data uploaded successfully."

        return {"AI_summary": summary}

    except Exception as e:
        return {"error": str(e)}