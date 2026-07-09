# AI-Augmented Developer Toolkit 🚀🤖

A collection of Python-based CLI tools leveraging **Google Gemini AI** to automate daily development workflows, accelerate learning, and improve code quality. 

This repository was created as part of the recruitment process for the **AI-Augmented Developer Intern (Backend)** position at Boldare, showcasing my ability to use AI as an active thinking and development tool.

## 🛠️ Included Tools

### 1. AI Code Reviewer & Commenter (`asystent.py`)
A script that reads raw code files, analyzes the logic using the Gemini API, and automatically generates clean, human-readable comments explaining the code's functionality. 
* **Tech stack:** Python, Google Gemini API

### 2. AI PHPUnit Test Generator (`generator_testow.py`)
An automation tool that acts as a bridge between Python and PHP. It analyzes a given PHP class (e.g., `Koszyk.php`), prompts Gemini 2.5 Flash to write a comprehensive Unit Test, and saves it. 
Furthermore, it includes a **Dockerized environment** (`Dockerfile`) to instantly run the generated tests in complete isolation without polluting the host OS.
* **Tech stack:** Python, PHP 8.4, PHPUnit 11, Docker (Infrastructure as Code)

---

## 🚀 How to run the PHPUnit Generator

**Step 1: Prepare the environment**
Ensure you have Docker running and your `.env` file contains your `GEMINI_API_KEY`.

**Step 2: Generate the test file**
Run the Python script to create the test file:
`python generator_testow.py`

**Step 3: Build the isolated PHP container**
Create the Docker image with PHP 8.4 and PHPUnit:
`docker build -t asystent-php .`

**Step 4: Run the tests**
Execute the tests inside the container using this command:
`docker run --rm -v "${PWD}:/app" asystent-php php /usr/local/bin/phpunit KoszykTest.php`

---

## 🧠 Reflection: How AI helped me build this

As a developer building this toolkit, AI wasn't just a "code generator"—it was my pair-programmer and mentor. 

Coming into this task, I wanted to target the backend stack (PHP, PHPUnit, Docker) mentioned in the job offer. Instead of spending hours configuring a local PHP environment or learning PHPUnit syntax from scratch, I used Gemini to rapidly prototype the test structure. When I encountered environment issues (such as WSL misconfigurations on Windows or PHPUnit version mismatches inside the container), AI helped me debug the Docker container step-by-step. 

This approach allowed me to build a fully functional, containerized Infrastructure-as-Code solution in a fraction of the time, proving that AI is the ultimate tool for fast-tracking the adoption of new technologies.

---
*Created by Piotr Regeńczuk*