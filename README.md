# AI-Augmented Developer Toolkit 🚀🤖

A collection of containerized, Python-based CLI tools leveraging **Google Gemini AI** to automate daily development workflows, accelerate learning, and improve code quality. 

This repository showcases the ability to use Artificial Intelligence as an active engineering and development partner, focusing on Infrastructure as Code (Docker), automated testing (PHPUnit), and CI workflows.

## 🛠️ Toolkit Architecture

The repository is structured as a monorepo containing distinct developer tools:

### 1. AI Code Reviewer (`/ai_reviewer`)
An autonomous script that acts as a strict Git pre-commit hook. It reads staged changes (`git diff --cached`), analyzes the logic using the Gemini 2.5 Flash API, and automatically generates semantic Git commit messages.
- **Tech Stack:** Python 3.11, Google GenAI SDK, Git
- **Infrastructure:** Runs in an isolated `python:3.11-slim` Docker container.

### 2. AI PHPUnit Test Generator (`/phpunit_generator`)
An automation bridge between Python and PHP. It analyzes raw PHP classes, dynamically prompts the AI to write comprehensive Unit Tests, and instantly verifies them in a disposable, containerized environment.
- **Tech Stack:** Python 3.11, PHP 8.4, PHPUnit 11
- **Infrastructure:** Utilizes a custom `php:8.4-cli` Docker image.

---

## 🚀 How to Run the Tools

**Prerequisites:** Ensure Docker is running and your `.env` file (containing `GEMINI_API_KEY=your_key`) is placed in the root directory.

### Running the Code Reviewer

**Step 1: Stage your changes**
```bash
git add .
```

**Step 2: Build the environment** (run from the root directory)
```bash
docker build -f ai_reviewer/Dockerfile -t ai-assistant .
```

**Step 3: Execute the interactive review**
```bash
docker run --rm -it --env-file .env -v "${PWD}:/app" ai-assistant ai_reviewer/asystent.py
```

### Running the PHPUnit Generator

**Step 1: Generate the test file**
Run the Python script to dynamically create the test file (ensure dependencies are installed locally or run via a container).

**Step 2: Build the isolated PHP testing environment** (run from the root directory)
```bash
docker build -f phpunit_generator/Dockerfile -t asystent-php .
```

**Step 3: Execute the tests inside the container**
```bash
docker run --rm -v "${PWD}/phpunit_generator:/app" asystent-php php /usr/local/bin/phpunit KoszykTest.php
```

---

## 🧠 Reflection: Building alongside AI

As a developer building this toolkit, AI wasn't just a "code generator"—it was my pair-programmer and mentor. 

Instead of spending hours configuring a local PHP environment or learning PHPUnit syntax from scratch, I used Gemini to rapidly prototype the test structure. When I encountered complex environment issues (like dependency management, volume mounting, or syntax updates in the SDK), AI helped me debug the Docker containers step-by-step. 

This approach allowed me to build a fully functional, containerized system in a fraction of the time, proving that AI is the ultimate tool for fast-tracking the adoption of new technologies.