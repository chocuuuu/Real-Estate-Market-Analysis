# Real-Estate Market Analysis

This project is a **web scraping solution** designed to extract and analyze real estate data from [Zillow.com](https://www.zillow.com/).  
The core of this project is an automated workflow leveraging the **Apify platform** to scrape property listings and save them into a CSV file, providing a clean dataset for future analysis.

---

## 📌 Project Status
Currently in the **data gathering phase**.  
- ✅ Collecting a comprehensive dataset of Zillow properties.  
- ⏳ Data analysis and visualization are **work in progress**.  

---

## 🗂️ Scraped Data Fields
The scraper collects a wide range of attributes for each property listing.  
Key fields include:

- **`zpid`** → Unique property ID on Zillow  
- **`address`** → Full property address  
- **`location`** → Geographic location / region  
- **`price`** → Current listing price  
- **`bedrooms`** → Number of bedrooms  
- **`bathrooms`** → Number of bathrooms  
- **`livingArea`** → Square footage of the property  
- **`lotSizeWithUnit`** → Lot size (with units)  
- **`yearBuilt`** → Year the property was built  
- **`propertyType`** → Type of property (house, condo, etc.)  
- **`daysOnZillow`** → How long the listing has been active  
- **`listingDateTimeOnZillow`** → Date/time first listed  
- **`estimates`** → Zillow’s price estimate data (Zestimate, rent estimate, etc.)  
- **`openHouseShowingList`** → Upcoming open house events (if available)  

These fields provide the **core dataset** for pricing trends, housing supply analysis, and property comparisons.

---

## ✨ Key Features
- **Automated Web Scraping** → Python script initiates & manages an Apify actor.  
- **Real-time Data** → Scrapes up-to-date Zillow listings with configurable search parameters.  
- **Data Export** → Saves to `zillow_properties.csv`.  
- **GitHub Actions Integration** → Workflow automates scraping & data export on push to `main`.  
- **Secure Credential Management** → API tokens & IDs stored safely in **GitHub Secrets**.  

---

## ⚙️ How It Works
The automation is handled by a **GitHub Actions workflow**:  
`.github/workflows/apify_workflow.yml`

1. Push to `main` or manually trigger the workflow.  
2. GitHub injects **credentials** from repository secrets into the environment.  
3. `main.py` script runs, connecting to Apify API.  
4. Script launches the **Zillow scraper** and fetches results.  
5. Data is saved to `zillow_properties.csv`.  
6. Workflow’s **upload-artifact step** saves the CSV as a downloadable artifact.  

---

## 🚀 Setup for New Users
To use this project in your own GitHub account:

1. **Fork this repository.**  
2. Go to **Settings > Secrets and variables > Actions** in your fork.  
3. Add the following **repository secrets** (from your Apify account):
   - `APIFY_TOKEN`
   - `ACTOR_RUN_ID`
   - `KEY_VALUE_STORE_ID`
   - `DATASET_ID`
4. Push to your `main` branch.  
   - The scraping workflow will **automatically run**.  
   - Download the generated `zillow-data.zip` artifact from the **Actions tab**.  

---

## 📊 Next Steps
- 🔍 Perform exploratory data analysis (EDA).  
- 📈 Build dashboards & visualizations.  
- 🧠 Apply machine learning for **price predictions & market trends**.  

---
