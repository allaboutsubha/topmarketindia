@echo off
color 0a
cls

set github_user=allaboutsubha
set /p repo_name="Enter GitHub Repository Name: "
set /p commit_msg="Enter Commit Message (Press Enter for Default): "

:: যদি মেসেজ খালি থাকে তবে ডিফল্ট মেসেজ সেট হবে
if "%commit_msg%"=="" set commit_msg=Update via Batch Script

set repo_url=https://github.com/%github_user%/%repo_name%.git

echo.
echo Target URL: %repo_url%
echo Checking Git Status...
echo ---------------------------------------

if not exist ".git" (
    echo [INFO] Initializing new repository...
    git init
)

:: ১. Git Add
git add . && echo [OK] Files added || echo [ERROR] Add failed

:: ২. Git Commit (এখন আর খালি থাকবে না)
git commit -m "%commit_msg%" && echo [OK] Commit Success || echo [ERROR] Nothing new to commit
echo.

:: ৩. Git Branch
git branch -M main

:: ৪. Git Remote Update
git remote remove origin >nul 2>&1
git remote add origin %repo_url%

:: ৫. Git Push
echo Uploading...
git push -u origin main -f && echo [OK] Files are on GitHub || echo [ERROR] Push Failed
echo.

echo ---------------------------------------
echo Done!
echo ---------------------------------------
pause