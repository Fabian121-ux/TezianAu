#!/bin/bash

echo "🚀 Starting build process..."

# Remove existing public directory if it exists
rm -rf public

# Create public directory
mkdir -p public

# Create index.html
cat > public/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DebateHub - Real-time Debate Platform</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            text-align: center;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .logo {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        .subtitle {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.8;
        }
        .features {
            list-style: none;
            padding: 0;
            margin: 2rem 0;
        }
        .features li {
            padding: 0.5rem 0;
            opacity: 0.9;
        }
        .cta {
            display: inline-block;
            padding: 1rem 2rem;
            background: #e50914;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            margin-top: 1rem;
            transition: background 0.3s;
        }
        .cta:hover {
            background: #f40612;
        }
        .spinner {
            border: 2px solid rgba(255,255,255,0.3);
            border-top: 2px solid #e50914;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 1rem auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🎯 DebateHub</div>
        <div class="subtitle">Real-time Debate Platform</div>
        <ul class="features">
            <li>✨ Live Debate Rooms</li>
            <li>📚 Netflix-Style Library</li>
            <li>👥 User Profiles & Avatars</li>
            <li>🔔 Real-time Alerts</li>
            <li>⚡ Admin Dashboard</li>
        </ul>
        <a href="/app" class="cta">Launch App</a>
        <div class="spinner"></div>
        <p style="margin-top: 1rem; opacity: 0.7;">Loading Flask Backend...</p>
    </div>
    <script>
        setTimeout(() => {
            window.location.href = '/app';
        }, 3000);
    </script>
</body>
</html>
EOF

# Create additional required files
cat > public/404.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>404 - Page Not Found</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 2rem; }
        h1 { color: #e50914; }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you're looking for doesn't exist.</p>
    <a href="/">Go back to DebateHub</a>
</body>
</html>
EOF

# Create robots.txt
cat > public/robots.txt << 'EOF'
User-agent: *
Allow: /

Sitemap: /sitemap.xml
EOF

# Create a simple sitemap
cat > public/sitemap.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://your-domain.com/</loc>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>
EOF

# Create manifest.json
cat > public/manifest.json << 'EOF'
{
    "name": "DebateHub",
    "short_name": "DebateHub",
    "description": "Real-time debate platform",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#1a1a1a",
    "theme_color": "#e50914",
    "icons": [
        {
            "src": "/favicon.ico",
            "sizes": "64x64 32x32 24x24 16x16",
            "type": "image/x-icon"
        }
    ]
}
EOF

# Create a simple favicon placeholder
echo "Creating favicon placeholder..."
touch public/favicon.ico

# List contents to verify
echo "✅ Build completed successfully!"
echo "📁 Contents of public directory:"
ls -la public/

echo "🎯 Public directory is ready for deployment!"
EOF

# Make the script executable
chmod +x build.sh

Now let's create a Node.js version of the build script:
