const fs = require("fs")
const path = require("path")

console.log("🔍 Verifying build output...")

const publicDir = path.join(__dirname, "public")
const requiredFiles = ["index.html", "style.css", "app.js", "manifest.json", "robots.txt", "sitemap.xml"]

// Check if public directory exists
if (!fs.existsSync(publicDir)) {
  console.error("❌ Public directory does not exist!")
  process.exit(1)
}

// Check required files
let allFilesExist = true
requiredFiles.forEach((file) => {
  const filePath = path.join(publicDir, file)
  if (fs.existsSync(filePath)) {
    console.log(`✅ ${file} exists`)
  } else {
    console.error(`❌ ${file} missing`)
    allFilesExist = false
  }
})

if (allFilesExist) {
  console.log("🎉 All required files exist in public directory!")
  console.log("📁 Build output is ready for deployment")
} else {
  console.error("❌ Some files are missing from build output")
  process.exit(1)
}
