
$projects = @(
    "Python_Vulnerability_Scanner",
    "Secure_Chat_Protocol",
    "WiFi_Deauth_Tool",
    "Steganography_Tool",
    "Password_Strength_AI",
    "DevOps_Dashboard_UI",
    "E_Commerce_API",
    "Realtime_Weather_App"
)

Write-Host "🚧 Starting Bulk Upload to GitHub..." -ForegroundColor Cyan

# 1. Upload Projects
foreach ($proj in $projects) {
    if (Test-Path $proj) {
        Write-Host "Processing $proj..." -ForegroundColor Yellow
        Push-Location $proj
        
        # Initialize Git
        if (-not (Test-Path ".git")) {
            git init | Out-Null
        }
        
        git add .
        git commit -m "Initial release of $proj" | Out-Null
        
        # Create GitHub Repo and Push
        # We use --confirm to avoid prompts if repo exists, or check first
        # Try to create. If it fails (exists), we just link remote.
        
        try {
            gh repo create "kyle21pixel/$proj" --public --source=. --remote=origin --push
            Write-Host "✅ Uploaded $proj" -ForegroundColor Green
        }
        catch {
            Write-Host "⚠️  Could not create/push $proj (Repo might already exist?)" -ForegroundColor Red
        }
        
        Pop-Location
    } else {
        Write-Host "❌ Folder $proj not found!" -ForegroundColor Red
    }
}

# 2. Handle the Special Profile Repo
# We need to move the README.md to a clean folder named 'kyle21pixel' so it matches the repo name requirement
$profileDir = "kyle21pixel"
if (-not (Test-Path $profileDir)) {
    New-Item -ItemType Directory -Force -Path $profileDir | Out-Null
    Copy-Item "README.md" -Destination $profileDir
} else {
    Copy-Item "README.md" -Destination $profileDir -Force
}

Write-Host "Processing Profile (kyle21pixel)..." -ForegroundColor Yellow
Push-Location $profileDir
if (-not (Test-Path ".git")) {
    git init | Out-Null
}
git add .
git commit -m "Update Profile README" | Out-Null
try {
   gh repo create "kyle21pixel/kyle21pixel" --public --source=. --remote=origin --push
   Write-Host "✅ Uploaded Profile" -ForegroundColor Green
}
catch {
   Write-Host "⚠️  Could not create/push Profile (Might already exist)" -ForegroundColor Red
}
Pop-Location

Write-Host "🎉 All Done! Check https://github.com/kyle21pixel" -ForegroundColor Cyan
