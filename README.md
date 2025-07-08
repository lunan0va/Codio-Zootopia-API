# Zootopia API Project

## What is this project?

The result of an assignment for [Masterschool]([https://learn.masterschool.com/](https://referral.masterschool.com/u9bTQr92)).

![Static Badge](https://img.shields.io/badge/Zootopia_with_API-100%2F100-brightgreen?style=flat)

A simple Python program that fetches animal data from an external API (API Ninjas) and generates a dynamic HTML page.  
It’s an extension of the original Zootopia project, which used a static JSON file.

## How to use

> [!NOTE]  
> Tested with `Python 3.13.3`

1. Clone the repository:
   ```bash
   git clone https://github.com/lunan0va/Codio-Zootopia-AP
   cd zootopia-api
   ```

2. Install dependencies: 
   ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file in the project folder with your API key:
   ```
   API_KEY='YOUR_API_KEY_HERE'
   ```
4. Run:
   ```bash
   python animals_web_generator.py
   ```

Example prompt:
   ```bash
   Please enter an animal: Fox
   ```
