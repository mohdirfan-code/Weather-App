# 🌦️ Weather App — Real-Time Weather, Forecast & Air Quality Platform

**Created by Irfan**  
_Fullstack AI/ML Project_

---

## 🚀 Project Overview

This repository hosts the **Weather App**, a robust full-stack application designed to provide real-time weather data and air quality information for any location—using a modern, user-friendly interface and a scalable, extensible backend.

Built as part of an AI/ML Software Engineer technical assessment, this project demonstrates best practices in API design, user input handling, data validation, database CRUD operations, and optional integrations with third-party platforms (e.g., YouTube, Google Maps).

> **Key Value:**  
> - Real-world API integration  
> - Clean, modular codebase  
> - Designed for extensibility and professional deployment  
> - Ready for demonstration, portfolio, or further development

---

## ✨ Features

- **Universal Location Input:**  
  Search weather and air quality by city, zip code, coordinates, or landmarks. Robust validation and fuzzy matching for user convenience.

- **Real-Time Weather & 5-Day Forecast:**  
  Live data from [OpenWeatherMap](https://openweathermap.org/api), including detailed weather info, icons, and at-a-glance summaries.

- **Air Quality Index (AQI) Data:**  
  Instantly retrieve current air quality information for user-selected locations, powered by OpenWeatherMap Air Pollution API.

- **Geolocation Support:**  
  Instantly fetch weather and air quality for your current position—using your browser/device location (with user permission).

- **Comprehensive CRUD:**  
  Save, update, view, and delete weather and air quality queries/records. All data is persisted in a robust SQLite database via SQLAlchemy ORM.

- **Data Export:**  
  Export your search history or saved records to **JSON**, **CSV**, **XML**, or **PDF** formats with one click. Great for data portability, analytics, and reporting.

- **API Integrations:**
  - **Google Maps:** Visualize searched locations on the map.
  - **YouTube:** Watch trending videos about your searched location.
  - **OpenWeatherMap Weather & Air Quality APIs**  

- **Responsive & Accessible UI:**  
  Clean, mobile-friendly design with flexible color gradients and intuitive controls. Accessibility best practices followed.

- **Error Handling:**  
  Clear, actionable error messages for every input and API call.

- **No Authentication Required:**  
  All features are open for demonstration and review.

- **Info Button:**  
  Learn more about the project and about me, [Mohd Irfan](https://www.linkedin.com/in/irfan786msfri/), from the Info page.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.12+, Flask, SQLAlchemy, SQLite
- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Jinja2
- **APIs:** OpenWeatherMap (Weather & Air Quality), YouTube Data API, Google Maps
- **Utilities:** Pandas (export), FPDF (PDF export), python-dotenv (for secure API key management)
- **Testing:** (Add your test framework, e.g., pytest, if implemented)
- **Deployment:** Easily deployable on Heroku, Render, or any WSGI-compatible service

---

## 🖼️ App Screenshots
**Home Page**
![Home Page](https://github.com/user-attachments/assets/1afa06b3-a0bc-4320-9742-5017848e07f8)  

**Search Result**
![Search Result](https://github.com/user-attachments/assets/ea56b5c4-7996-48ae-aea4-b5bc1ed714ab)  

**Air Quality**
![Air Quality](https://github.com/user-attachments/assets/217982ea-1937-46c0-8307-37c11ef67288)  

**Google Location & YouTube Videos**
![Google Location & Youtube Videos](https://github.com/user-attachments/assets/3c2c1985-66f8-4a0c-b31f-c179b2687c83)  

**Records (CRUD)**
![Records (CRUD)](https://github.com/user-attachments/assets/f1a9c705-03a4-4845-8f86-41c474d80be1)  

**Info Page**
![Info Page](https://github.com/user-attachments/assets/918a2e9f-533f-40f2-b281-576e445f6819)  

---

## 🏗️ Project Structure

```
weather-app/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── run.py
├── test.py
│
├── app/
│   ├── air_quality.py
│   ├── export.py
│   ├── forms.py
│   ├── geocode.py
│   ├── maps_api.py
│   ├── models.py
│   ├── routes.py
│   ├── utils.py
│   ├── weather_api.py
│   ├── youtube_api.py
│   └── __init__.py
│
├── instance/
│   └── weather_app.db
│
├── static/
│   ├── style.css
│   ├── css/
│   ├── img/
│   └── js/
│
├── templates/
│   ├── base.html
│   ├── create.html
│   ├── edit.html
│   ├── history.html
│   ├── index.html
│   ├── info.html
│   ├── list.html
│   ├── view.html
│   └── weather.html
│
└── __pycache__/
```

---

## ⚡ Quickstart Guide

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### 2. **Create and Activate a Virtual Environment**

```bash
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Setup Environment Variables**

- Copy the example file and add your API keys:
  ```bash
  cp .env.example .env
  ```
- Get a free [OpenWeatherMap API Key](https://openweathermap.org/api)
- Get a [YouTube Data API Key](https://console.developers.google.com/)

### 5. **Run the Application**

```bash
flask run
```
- Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 💾 CRUD & Data Export

- **Create:** Save any weather or air quality search with location and date range.
- **Read:** Review all your saved queries and their results.
- **Update:** Modify existing records (location or date).
- **Delete:** Remove any record with one click.
- **Export:** Download all your data in JSON, CSV, XML, or PDF.

---

## 📹 Demo Video

> _Embed your screencast or YouTube demo link below for reviewers and LinkedIn viewers:_
>
> 📹 [Watch Demo on Vimeo](https://vimeo.com/1091614971/790150541a?share=copy)

---

## 📇 Contact

- **Author:** Irfan
- **Email:** mohdirfanwork786@gmail.com
- **LinkedIn:** [Mohd Irfan](https://www.linkedin.com/in/irfan786msfri/)
- **GitHub:** [mohdirfan-code](https://github.com/mohdirfan-code)
- **Twitter/X:** [@Irfu6428](https://x.com/Irfu6428)

---

## ⭐ Show your support!

If you found this project useful or inspiring:
- Star this repo ⭐
- Fork and contribute 🤝

---

**_Thank you so much for checking out my Weather App!_**

---
