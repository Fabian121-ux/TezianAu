#!/bin/bash

echo "🚀 Starting DebateHub deployment preparation..."

# Create public directory
mkdir -p public/assets public/images

# Run build script
echo "📦 Building static assets..."
node build.js

# Copy any additional static files
if [ -d "static" ]; then
    echo "📁 Copying static files..."
    cp -r static/* public/assets/ 2>/dev/null || echo "No static files to copy"
fi

# Create deployment info
echo "📝 Creating deployment info..."
cat > public/deployment-info.json << EOF
{
    "app": "DebateHub",
    "version": "1.0.0",
    "deployed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
    "platform": "Multi-platform Flask App",
    "features": [
        "Real-time debates",
        "User authentication", 
        "Netflix-style library",
        "Admin dashboard",
        "Alert system",
        "Supabase integration"
    ]
}
EOF

echo "✅ Deployment preparation complete!"
echo "📁 Public directory created with all necessary files"
echo "🎯 Your app is ready for deployment on any platform!"
