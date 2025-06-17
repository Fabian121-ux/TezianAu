// DebateHub Frontend JavaScript
console.log("🎯 DebateHub Static Site Loaded")

// Simple routing for static site
const router = {
  init() {
    this.handleRouting()
    this.setupEventListeners()
  },

  handleRouting() {
    const path = window.location.pathname
    console.log("Current path:", path)

    // Redirect to Flask app for dynamic routes
    const dynamicRoutes = ["/auth", "/library", "/admin", "/debate"]
    if (dynamicRoutes.some((route) => path.startsWith(route))) {
      this.redirectToFlaskApp()
    }
  },

  redirectToFlaskApp() {
    console.log("Redirecting to Flask backend...")
    // This would redirect to your actual Flask deployment
    window.location.href = "/app" + window.location.pathname
  },

  setupEventListeners() {
    // Handle CTA button clicks
    document.addEventListener("click", (e) => {
      if (e.target.classList.contains("cta-button")) {
        e.preventDefault()
        this.redirectToFlaskApp()
      }
    })
  },
}

// Initialize when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
  router.init()
})

// Service Worker for PWA capabilities
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/sw.js")
      .then((registration) => {
        console.log("SW registered: ", registration)
      })
      .catch((registrationError) => {
        console.log("SW registration failed: ", registrationError)
      })
  })
}
