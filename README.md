# Gibsey MVP Backend

## Purpose
This is the Python backend for the Gibsey MVP (Minimum Viable Product). Gibsey is designed to provide AI-powered functionality with seamless data management capabilities.

## Project Structure
```
├── src/                # Main application code
├── scripts/           # Utility scripts for data upload, seeding, etc.
├── database/          # Database migrations and schema files  
├── requirements.txt   # Python dependencies
├── .env.example      # Environment variables template
└── README.md         # This file
```

## Setup
1. Copy `.env.example` to `.env` and fill in your actual values
2. Install dependencies: `pip install -r requirements.txt`
3. Configure your Supabase and OpenAI credentials

## Dependencies
- **supabase**: Database and backend services
- **openai**: AI model integration
- **tenacity**: Retry logic and resilience
- **tqdm**: Progress bars for long-running operations

## Getting Started
More implementation details coming soon... 