# Discord Welcome Bot - Test Assignment

This is a test project that implements a simple Discord bot. The bot welcomes new members to a Discord server and shares a link to an onboarding document. For this assignment, the bot was hosted on **Replit** for simplicity and cost-effectiveness.

---

## Features
- **Welcome Message**: Greets new members with a personalized message.
- **Document Sharing**: Provides a link to an onboarding document for new members to review.
- **Automated Responses**: Uses Discord intents to track member join events and respond in real time.

---

## Hosting Details

### Hosting Platform: **Replit**
The bot is hosted on Replit, an online IDE and hosting platform. Replit was chosen for the following reasons:

   - Replit offers free hosting for small-scale projects, making it ideal for this test assignment.
   - Other hosting platforms like AWS, Google colab, or Heroku can incur significant costs, especially for long-running bots or projects with limited budgets.
   - Replit provides an intuitive interface for writing, running, and debugging Python code directly in the browser. This makes it convenient for quick assignments or small-scale projects.
   - Built-in support for environment variables simplifies secure token management.
   - While the free version of Replit may not keep the bot running 24/7, upgrading to a paid plan is still more affordable compared to other platforms.
---

## How to Run on Replit
1. Create a new Python project on [Replit](https://replit.com/).
2. Paste the code from the `tripletestbotcode.py` file into the project.
3. Add your Discord bot token as a secret environment variable:
   - Go to the **Secrets** tab (🔑) in Replit.
   - Add a new variable named `DISCORD_BOT_TOKEN` and paste your bot token as the value.
4. Click **Run** to start the bot. Replit will automatically host the bot and make it accessible to your Discord server.

---

## Conclusion
Replit was chosen as the hosting platform for this test assignment due to its cost-effectiveness, ease of use, and quick deployment capabilities. This makes it an excellent choice for small-scale or test projects like this one.
