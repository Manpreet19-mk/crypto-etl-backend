 Crypto ETL Backend

A Dockerized backend service that performs ETL (Extract, Transform, Load) operations on cryptocurrency market data using public APIs and stores the data in PostgreSQL. The project exposes REST APIs using FastAPI to trigger ETL jobs and retrieve stored data.



🚀 Features

- Fetches real-time cryptocurrency prices from:
  - CoinGecko (public API)
  - CoinPaprika (public API)
- Stores normalized crypto price data in PostgreSQL
- REST API built using FastAPI
- Dockerized setup using Docker Compose
- Swagger UI for API testing
- Modular ETL architecture (ingestion, services, API layers)



 🧱 Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **ETL**: Custom Python ingestion modules
- **Containerization**: Docker & Docker Compose
- **API Docs**: Swagger (OpenAPI)



 📂 Project Structure

crypto-etl-backend/
│
├── api/
│ └── main.py # FastAPI entry point
│
├── ingestion/
│ ├── coingecko.py # CoinGecko ingestion logic
│ ├── coinpaprika.py # CoinPaprika ingestion logic
│ └── etl_runner.py # Orchestrates ETL process
│
├── services/
│ ├── db.py # Database connection
│ └── models.py # SQLAlchemy models
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md

yaml
 ⚙️ Setup Instructions

 1️⃣ Prerequisites

- Docker
- Docker Compose



 2️⃣ Clone Repository

git clone https://github.com/<your-username>/crypto-etl-backend.git
cd crypto-etl-backend


3️⃣ Run the Application

docker-compose up --build
The API will start at:
http://localhost:8000
📘 API Endpoints
🔹 Swagger UI

http://localhost:8000/docs
🔹 Health Check
GET /health
Response

{
  "db": "connected"
}

🔹 Trigger ETL Job
POST /etl/run

Response

{
  "status": "ETL completed"
}
🔹 Fetch Stored Data
GET /data
Response

[
  {
    "source": "coingecko",
    "symbol": "btc",
    "name": "Bitcoin",
    "price_usd": 43000,
    "timestamp": "2025-12-25T16:40:00"
  }
]
🔐 API Keys
This project uses public endpoints

No API keys are required

Architecture supports environment-based API keys if needed in future

🧪 Notes
ETL can be triggered manually via API

Database persists using Docker volumes

Designed for backend / data engineering assignments

👩‍💻 Author
Manpreet Kaur
Final Year CSE Student
Backend & Data Engineering Enthusiast

