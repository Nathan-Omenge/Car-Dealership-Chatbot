# RASA Dealership Chatbot

## Overview
AI-powered chatbot for automotive dealership with:
- 660 vehicle inventory records
- 201 customer training questions
- African market pricing (Nigeria, Kenya, South Africa, Ghana)
- WordPress integration ready

## Deployment
Deployed on Railway.app with auto-scaling and HTTPS.

## API Endpoint
- **URL**: `https://your-app.railway.app/webhooks/rest/webhook`
- **Method**: POST
- **Content-Type**: application/json

## Sample Request
```json
{
  "sender": "user123",
  "message": "Hello, I'm looking for a Toyota"
}
```

## Sample Response
```json
[
  {
    "recipient_id": "user123", 
    "text": "Hello! Welcome to our dealership. I found several Toyota vehicles in our inventory. What's your budget range?"
  }
]
```

## Features
- Vehicle search by make/model/price
- Pricing and financing information
- Customer support
- Multi-market inventory
- WordPress integration
