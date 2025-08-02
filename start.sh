#!/bin/bash
# Railway.app startup script

echo "🚀 Starting RASA Dealership Chatbot..."
echo "📊 Training model if needed..."

# Train model if not exists
if [ ! -d "models" ] || [ -z "$(ls -A models)" ]; then
    echo "🎓 Training RASA model..."
    rasa train --quiet
else
    echo "✅ Model already trained"
fi

echo "🌐 Starting RASA server..."
echo "📍 Server will be available at: http://0.0.0.0:$PORT"
echo "🔗 Webhook endpoint: /webhooks/rest/webhook"

# Start RASA server
exec rasa run --enable-api --cors '*' --port $PORT --host 0.0.0.0
