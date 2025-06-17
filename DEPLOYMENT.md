# 🚀 DebateHub Deployment Guide

## Platform-Specific Deployment

### 🔵 Vercel Deployment
1. Connect your GitHub repository to Vercel
2. Set environment variables in Vercel dashboard:
   - `SUPABASE_URL`
   - `SUPABASE_KEY` 
   - `SECRET_KEY`
3. Deploy automatically on push to main branch

### 🟣 Heroku Deployment
\`\`\`bash
# Install Heroku CLI and login
heroku login

# Create new app
heroku create your-debate-app-name

# Set environment variables
heroku config:set SUPABASE_URL=your_supabase_url
heroku config:set SUPABASE_KEY=your_supabase_key
heroku config:set SECRET_KEY=your_secret_key

# Deploy
git push heroku main
\`\`\`

### 🟠 Railway Deployment
1. Connect GitHub repository to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically

### 🔴 DigitalOcean App Platform
1. Create new app from GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set run command: `gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:$PORT wsgi:app`
4. Add environment variables

## Environment Variables Required
\`\`\`
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key
SECRET_KEY=your_secure_random_string
FLASK_ENV=production
\`\`\`

## Pre-Deployment Checklist
- [ ] Environment variables configured
- [ ] Supabase database tables created
- [ ] Storage bucket "library" created in Supabase
- [ ] Requirements.txt updated
- [ ] Static files properly configured
- [ ] Health check endpoint working

## Post-Deployment Steps
1. Run database setup: Access `/admin` and run setup scripts
2. Create admin user
3. Test all features
4. Monitor logs for errors

Your Flask app is now ready for deployment! 🎉
