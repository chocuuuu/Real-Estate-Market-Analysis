import requests
import json
import pandas as pd
import os

# =========================================================================
# === IMPORTANT: The script now reads from environment variables ===
# =========================================================================
APIFY_TOKEN = os.environ.get("APIFY_TOKEN")
ACTOR_RUN_ID = os.environ.get("ACTOR_RUN_ID")
KEY_VALUE_STORE_ID = os.environ.get("KEY_VALUE_STORE_ID")
DATASET_ID = os.environ.get("DATASET_ID")

# Ensure all required variables are set before proceeding
if not all([APIFY_TOKEN, ACTOR_RUN_ID, KEY_VALUE_STORE_ID, DATASET_ID]):
    raise ValueError("One or more required environment variables are not set.")

fields = [
    "zpid","location","address","isFeatured","isShowcaseListing","rental","currency",
    "country","listingDateTimeOnZillow","bestGuessTimeZone","isUnmappable",
    "listCardRecommendation","bathrooms","bedrooms","livingArea","yearBuilt",
    "lotSizeWithUnit","propertyType","listing","daysOnZillow","isPreforeclosureAuction",
    "price","estimates","zillowOwnedProperty","taxAssessment","region",
    "personalizedResult","propertyDisplayRules","ssid","hasFloorPlan","scrapedAt",
    "openHouseShowingList","title","groupType","newConstruction","mapDotTag",
]
fields_param = "%2C".join(fields)
# =========================================================================

def fetch_apify_run_data():
    """
    Fetches the input, log, and dataset from a specific Apify actor run.
    """
    # Define the API base URL and the headers with the token.
    APIFY_API_BASE_URL = "https://api.apify.com/v2"
    
    # Define the endpoints for fetching the run's log, input, and dataset.
    log_endpoint = f"{APIFY_API_BASE_URL}/logs/{ACTOR_RUN_ID}?token={APIFY_TOKEN}"
    input_endpoint = f"{APIFY_API_BASE_URL}/key-value-stores/{KEY_VALUE_STORE_ID}/records/INPUT?token={APIFY_TOKEN}"
    # The dataset endpoint to fetch the scraped data.
    dataset_endpoint = (
        f"{APIFY_API_BASE_URL}/datasets/{DATASET_ID}/items"
        f"?token={APIFY_TOKEN}&format=json&clean=1&fields={fields_param}"
    )

    print("Attempting to fetch data from the Apify actor run...")

    # =========================================================================
    # === Fetching the Run's Input ===
    # =========================================================================
    try:
        print("\n--- Fetching actor run input ---")
        input_response = requests.get(input_endpoint)
        input_response.raise_for_status()
        
        input_data = input_response.text
        print("Input fetched successfully:")
        print(input_data)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching input: {e}")
        if input_response.status_code in [401, 403]:
            print("Please check that your 'APIFY_TOKEN' is correct and has the necessary permissions.")
            
    # =========================================================================
    # === Fetching the Run's Log ===
    # =========================================================================
    try:
        print("\n--- Fetching actor run log ---")
        log_response = requests.get(log_endpoint)
        log_response.raise_for_status()

        log_data = log_response.text
        print("Log fetched successfully:")
        print(log_data)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching log: {e}")
        if log_response.status_code in [401, 403]:
            print("Please check that your 'APIFY_TOKEN' is correct.")

    # =========================================================================
    # === Fetching the Run's Dataset ===
    # =========================================================================
    try:
        print("\n--- Fetching actor run dataset ---")
        dataset_response = requests.get(dataset_endpoint)
        dataset_response.raise_for_status()
        
        dataset_data = dataset_response.json()
        
        if dataset_data:
            print(f"Dataset fetched successfully. Found {len(dataset_data)} records.")
            
            # Convert the list of dictionaries to a pandas DataFrame for better readability and structure
            df = pd.DataFrame(dataset_data)
            
            # Print the first few records for a quick preview
            print("\n--- First 5 Scraped Properties (Preview) ---")
            print(df.head().to_string())
            
            # You can also save the entire dataset to a CSV file.
            csv_filename = "zillow_properties.csv"
            df.to_csv(csv_filename, index=False)
            print(f"\nAll scraped data saved to '{csv_filename}'.")
            
        else:
            print("The dataset is empty. No property records were found.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching dataset: {e}")
        if dataset_response.status_code in [401, 403]:
            print("Please check that your 'APIFY_TOKEN' is correct and that the dataset ID is valid.")
    except json.JSONDecodeError:
        print("Failed to decode JSON from the dataset response. The data format may be incorrect.")

if __name__ == "__main__":
    fetch_apify_run_data()
