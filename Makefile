.PHONY: build clean install

build:
	@echo "🚀 Building DebateHub..."
	@mkdir -p public
	@echo "<!DOCTYPE html><html><head><title>DebateHub</title></head><body><h1>🎯 DebateHub</h1><p>Real-time debate platform loading...</p><script>setTimeout(() => window.location.href = '/app', 2000);</script></body></html>" > public/index.html
	@echo "User-agent: *\nAllow: /" > public/robots.txt
	@touch public/favicon.ico
	@echo "✅ Build completed - public directory created!"
	@ls -la public/

clean:
	@rm -rf public/
	@echo "🧹 Cleaned build directory"

install:
	@pip install -r requirements.txt
	@echo "📦 Dependencies installed"
