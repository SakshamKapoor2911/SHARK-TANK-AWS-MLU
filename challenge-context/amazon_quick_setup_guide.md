# Amazon Quick & PartyRock Setup and Sprint Guide

This guide explains how to access, set up, and build on **Amazon Quick** (and the **PartyRock** fallback) during the 60–75 minute Shark Tank build sprint.

---

## 1. What is Amazon Quick?

**Amazon Quick** is AWS's agentic generative AI workspace. In educational symposia and hackathons like Cloud Connect, Amazon Quick provides a rapid prototyping environment where students can build working web applications without writing frontend or backend code from scratch.

### The Two Modes in Amazon Quick
1. **Apps Mode (Recommended Path)**:
   - Describe your app's goal, inputs, logic, and outputs in plain English.
   - Quick automatically creates an interactive web interface with form fields, AI generation blocks, and dynamic UI elements that you can test live and share.
2. **Chat Mode (Alternative Path)**:
   - Conversational assistant mode for rapid queries, testing prompts, and refining data.

---

## 2. How to Access Amazon Quick

During the AWS x MLU Symposium, access is typically provided through one of the following methods:

### Method A: Event Workshop Portal / AWS IAM Identity Center (SSO)
1. Check your symposium welcome email, event Slack/Discord, or the projector slide in your breakout room for the **Workshop URL** (e.g., `https://dashboard.eventengine.run` or an AWS SSO portal link).
2. If given an **Event Engine Hash**:
   - Go to [dashboard.eventengine.run](https://dashboard.eventengine.run).
   - Enter your 12-to-16 digit team/student hash.
   - Choose **AWS Console** or **One-Click Quick Login**.
3. Locate **Amazon Quick** in the services or top navigation bar.
4. Navigate to the **Apps** tab on the left sidebar.

### Method B: Direct URL
- If the event provided a direct link (e.g., `https://quick.aws` or an enterprise workspace portal), sign in using your provided student/team credentials or AWS account.

---

## 3. Step-by-Step: Building in "Apps" Mode (The Winning Path)

### Step 1: Initialize App Generation
1. Inside Amazon Quick, click **Create App** or **New App**.
2. You will see an initial prompt box: *"Describe the app you want to build in plain English..."*

### Step 2: Craft Your "Master Seed Prompt"
Do not just write one sentence. Provide a structured prompt covering your scenario, target user, core requirements, and stretch goal.

**Example Seed Prompt Structure**:
```text
Build a web app called "[App Name]" for college students solving [Core Problem].
The app needs:
1. User Input widget for [Requirement 1, e.g., entering current fridge ingredients].
2. AI Generation widget that creates [Requirement 2, e.g., 3 quick, budget dorm recipes].
3. An interactive Q&A Chat widget for [Requirement 3, e.g., friendly nutrition questions].
4. An Image Generation widget that creates [Stretch Goal, e.g., motivational meal photo].
Make the visual design clean and modern, and make the conversational tone friendly, encouraging, and non-judgmental.
```

### Step 3: Inspect and Test the Generated App
1. Quick will generate a working app layout with connected widgets.
2. Type in sample student data to verify each widget works properly.

### Step 4: Refine & Customize Widgets (Iteration Loop)
1. Click on any widget to open its **Settings / Prompt Editor**.
2. **Connect Widgets**: Ensure downstream widgets reference upstream inputs (e.g., Recipe Generator should reference the Fridge Ingredients input).
3. **Tune Tone**: Add system instructions like: *"Adopt a warm, encouraging college mentor persona. Avoid complex culinary jargon."*
4. **Test the Stretch Goal**: Ensure your bonus feature (image generation, persona toggle, or budget projection) works reliably.

---

## 4. Fallback Plan: Using PartyRock (`partyrock.aws`)

If Amazon Quick encounters network throttling, session timeouts, or login issues during the sprint, immediately pivot to **PartyRock** (AWS's Bedrock-powered no-code playground).

### Step-by-Step PartyRock Setup:
1. Open your browser and navigate to: **[https://partyrock.aws](https://partyrock.aws)**.
2. Click **Log In** or **Sign Up** (Top Right):
   - You can authenticate instantly using an **Amazon account**, **Google account**, or **Apple ID**.
   - **No AWS account or credit card required**; it includes free generative credits for learners.
3. Click **"Build your own app"** or **"Generate App"**.
4. Paste your app description prompt into the generator box.
5. PartyRock will generate a full multi-widget canvas with:
   - **User Input widgets** (text fields, dropdowns)
   - **Text Generation widgets** (Claude 3.5 Sonnet / Amazon Titan text models)
   - **Image Generation widgets** (Amazon Titan Image Generator / SDXL)
   - **Chatbot widgets**
6. Hit **Publish / Make Public** to get a shareable URL that anyone in the room can open on their phone or laptop.

---

## 5. Sprint Execution Checklist (60–75 Minutes)

| Time Window | Phase | Key Milestone |
| :--- | :--- | :--- |
| **00:00 – 00:10** | **Access & Alignment** | Log in to Amazon Quick (or PartyRock). Assign team roles (Prompt Lead, Pitch Speaker, Tester). |
| **00:10 – 00:30** | **App Generation & Core Build** | Run master seed prompt. Build the 3 mandatory core features. |
| **00:30 – 00:50** | **Stretch Goals & Polish** | Add the bonus image generation, persona switch, or projection calculator. Refine system prompts. |
| **00:50 – 01:05** | **Live Testing & QA** | Test with realistic edge cases (e.g., student only has eggs and bread; budget is $15). |
| **01:05 – 01:15** | **Pitch Rehearsal** | Practice the 2-minute overview script. Keep the app open on screen for showcase. |
