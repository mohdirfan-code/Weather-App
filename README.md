# 🌦️ Weather App — Real-Time Weather & Forecast Platform

**Created by Irfan**  
_Fullstack AI/ML Software Engineer Project_

---

## 🚀 Project Overview

This repository hosts the **Weather App**, a robust full-stack application designed to provide real-time weather data for any location—using a modern, user-friendly interface and a scalable, extensible backend.

Built as part of an AI/ML Software Engineer technical assessment, this project demonstrates best practices in API design, user input handling, data validation, database CRUD operations, and optional integrations with third-party platforms (e.g., YouTube, Google Maps).

> **Key Value:**  
> - Real-world API integration  
> - Clean, modular codebase  
> - Designed for extensibility and professional deployment  
> - Ready for demonstration, portfolio, or further development

---

## ✨ Features

- **Universal Location Input:**  
  Search weather by city, zip code, coordinates, or landmarks. Robust validation and fuzzy matching for user convenience.

- **Real-Time Weather & 5-Day Forecast:**  
  Live data from [OpenWeatherMap](https://openweathermap.org/api), including detailed weather info, icons, and at-a-glance summaries.

- **Geolocation Support:**  
  Instantly fetch weather for your current position—using your browser/device location (with user permission).

- **Comprehensive CRUD:**  
  Save, update, view, and delete weather queries/records. All data is persisted in a robust SQLite database via SQLAlchemy ORM.

- **Data Export:**  
  Export your search history or saved records to **JSON**, **CSV**, **XML**, or **PDF** formats with one click. Great for data portability, analytics, and reporting.

- **API Integrations (Optional):**  
  - **YouTube:** Watch trending videos about your searched location.
  - **Google Maps:** Visualize searched locations on the map.

- **Responsive & Accessible UI:**  
  Clean, mobile-friendly design with flexible color gradients and intuitive controls. Accessibility best practices followed.

- **Error Handling:**  
  Clear, actionable error messages for every input and API call.

- **No Authentication Required:**  
  All features are open for demonstration and review.

- **Info Button:**  
  Learn about the [Product Manager Accelerator (PMA)](https://www.linkedin.com/company/product-manager-accelerator/) from within the app.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.12+, Flask, SQLAlchemy, SQLite
- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Jinja2
- **APIs:** OpenWeatherMap, (Optional: YouTube Data API, Google Maps)
- **Utilities:** Pandas (export), FPDF (PDF export), python-dotenv (for secure API key management)
- **Testing:** (Add your test framework, e.g., pytest, if implemented)
- **Deployment:** Easily deployable on Heroku, Render, or any WSGI-compatible service

---

## 🖼️ App Screenshots

> _Paste your working app images or GIFs here for maximum engagement!_
>
> ![Home Page](./assets/screenshot-home.png)
> ![Search Result](./assets/screenshot-weather.png)
> ![Records (CRUD)](./assets/screenshot-records.png)
> ![Data Export](./assets/screenshot-export.png)

---

## 🏗️ Project Structure

```
weather-app/
├── app.py
├── models.py
├── routes/
│   ├── weather.py
│   ├── records.py
│   └── export.py
├── static/
│   ├── style.css
│   └── icons/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── records.html
│   ├── info.html
│   └── ...
├── requirements.txt
├── .env.example
├── README.md
└── ...
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

- **Create:** Save any weather search with location and date range.
- **Read:** Review all your saved queries and their results.
- **Update:** Modify existing records (location or date).
- **Delete:** Remove any record with one click.
- **Export:** Download all your data in JSON, CSV, XML, or PDF.

---

## 🧑‍💻 Development & Contribution

Contributions, suggestions, and forks are welcome!  
- Please open Issues or submit Pull Requests for improvements.
- For major changes, open an Issue to discuss first.

---

## 📝 Assessment Requirements Mapping

| Requirement                      | Implemented? | Notes                                    |
| --------------------------------- | ------------ | ---------------------------------------- |
| User-friendly location input      | ✅           | Supports city, zip, coords, landmarks    |
| Real API weather data             | ✅           | OpenWeatherMap integration               |
| 5-day forecast                    | ✅           | Shown with icons and summary             |
| Current location support          | ✅           | Uses browser geolocation                 |
| CRUD (Create, Read, Update, Del)  | ✅           | All operations with validation           |
| Data export (JSON, CSV, XML, PDF) | ✅           | Multiple formats supported               |
| API integration (YouTube, Maps)   | ✅           | YouTube and Google Maps                  |
| Info button (PMA description)     | ✅           | Linked to PMA LinkedIn                   |
| Error handling & validation       | ✅           | All user input & API errors handled      |
| Demo video                        | ➡️           | [Add your demo video link below]         |

---

## 📹 Demo Video

> _Embed your screencast or YouTube demo link below for reviewers and LinkedIn viewers:_
>
> [![Watch Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://your-demo-link.com)

---

## 🌐 About the Product Manager Accelerator (PMA)

> **Product Manager Accelerator (PMA)** is a premier training and internship platform for aspiring product managers and AI engineers.  
> PMA offers hands-on projects, mentorship from industry leaders, and a direct pathway to launching your PM/AI career.
>
> [Learn more on LinkedIn]([https://www.linkedin.com/company/product-manager-accelerator/](https://www.linkedin.com/school/pmaccelerator/posts/?feedView=all))

---

## 📇 Contact

- **Author:** Irfan
- **Email:** mohdirfanwork786@gmail.com
- **LinkedIn:** [Your LinkedIn Profile]([https://www.linkedin.com/in/yourprofile/](https://www.linkedin.com/in/irfan786msfri/))
- **Project Issues:** [Submit an Issue](https://github.com/mohdirfan-code/weather-app/issues)

---

## ⭐ Show your support!

If you found this project useful or inspiring:
- Star this repo ⭐
- Fork and contribute 🤝

---

**_Thank you for checking out my Weather App!_**

---
