UPSTATE VETERAN COMPASS — FIRST-TIME SETUP (WINDOWS)

WHAT THIS ZIP DOES
- Provides a simple independent website.
- Fetches the official VA news-release RSS feed.
- Runs automatically once daily using GitHub Actions.
- Saves headlines, links, dates, and short feed descriptions into news.json.
- Does NOT use a paid AI service yet. This is free RSS automation, not AI-generated summaries.

STEP 1 — CREATE YOUR REPOSITORY
1. Sign in at https://github.com/
2. Click + (top right) > New repository.
3. Repository name: upstate-veteran-compass
4. Choose Public.
5. Check Add a README file.
6. Click Create repository.

STEP 2 — UPLOAD THE ZIP CONTENTS, NOT THE ZIP ITSELF
1. Download and extract the ZIP on Windows: right-click > Extract All.
2. Open the extracted folder.
3. In your GitHub repository, click Add file > Upload files.
4. Select all files and folders inside the extracted folder. Make sure the .github folder is included. If hidden folders are not visible in File Explorer, choose View > Show > Hidden items.
5. Drag the selected contents into the GitHub upload area.
6. Scroll down and click Commit changes.
IMPORTANT: index.html must appear at the top level of the repository, not inside an extra nested folder.

STEP 3 — ALLOW AUTOMATION TO SAVE NEWS
1. In the repository, click Settings.
2. In the left sidebar, click Actions > General.
3. Scroll to Workflow permissions.
4. Select Read and write permissions.
5. Click Save.

STEP 4 — RUN THE FIRST FEED UPDATE
1. Click the Actions tab.
2. In the left list, click Update official VA news feed.
3. Click Run workflow > Run workflow.
4. Wait for the run to finish with a green check mark. Click the run to inspect errors.
5. Return to the Code tab. After a successful run, news.json should contain VA news items.

STEP 5 — TURN ON FREE WEBSITE HOSTING
1. Click Settings > Pages.
2. Under Build and deployment, choose Deploy from a branch.
3. Select branch main and folder /(root), then click Save.
4. Wait a few minutes. GitHub Pages will show your site URL, usually:
   https://YOUR-GITHUB-USERNAME.github.io/upstate-veteran-compass/
5. Open that URL. If news has not appeared, confirm news.json contains items and refresh.

AUTOMATION NOTES
- The scheduled job runs daily at 12:17 UTC. GitHub may delay scheduled runs during busy periods.
- Scheduled workflows run only from the default branch. GitHub can disable scheduled workflows in public repositories with no activity for 60 days.
- If a run fails, open Actions > the failed run and read the error message.
- Never add passwords, private veteran records, API keys, or personal data to this public repository.
- Headlines and short descriptions are sourced from the feed and linked to VA. Verify deadlines and eligibility on official pages.
- This is an independent website, not an official VA website.
- AI-generated summaries and an AI support chatbot are NOT included yet. A secure backend and potentially paid API usage are needed for real AI. Never put API keys in website JavaScript.

OFFICIAL FEED
https://news.va.gov/news-releases/feed/
VA Press Room: https://news.va.gov/va-press-room/
