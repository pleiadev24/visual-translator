## Background 

OCR, or Optical Character Recognition, is a technology that enables the conversion of different types of documents, such as scanned paper documents, PDFs, or images captured by a digital camera, into editable and searchable data. OCR technology recognizes text within these documents, making it possible to extract, edit, and store the text for various purposes.
Tesseract OCR (Optical Character Recognition) is an open-source software library. It is designed to recognize text in images and convert it into machine-readable text.

# Tesseract OCR Installation Guide

This guide provides step-by-step instructions on how to download and install Tesseract OCR on different operating systems.

## Windows Installation

1. Download Tesseract Installer:
   - Visit the [Tesseract GitHub Releases](https://github.com/tesseract-ocr/tesseract/releases) page.
   - Download the appropriate installer for your Windows version (32-bit or 64-bit).

2. Run the Installer:
   - Double-click the downloaded installer executable.
   - Follow the on-screen instructions to complete the installation.

3. Set Environment Variable (Optional but recommended):
   - Add Tesseract to your system's PATH environment variable.
   - Path example: `C:\Program Files\Tesseract-OCR`
  
4. Verify Installation:
   - Open Command Prompt and type `tesseract --version` to confirm the installation.

## macOS Installation (Using Homebrew)

1. Install Homebrew (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


## Google Cloud Translation API

#### Step 1: Create a Google Cloud Platform (GCP) Account
Go to the GCP Console: Visit the Google Cloud Platform Console.
Create a New Project:
Click on the project drop-down in the upper right corner.
Click on "New Project."
Enter a project name and click "Create."
#### Step 2: Enable Billing for the Project
Enable Billing:
In the GCP Console, go to the "Billing" section.
Select your project from the list.
Click "Open."
Follow the prompts to enable billing for your project.
#### Step 3: Enable the Translation API
Go to the API Library:
In the GCP Console, go to the "API & Services" > "Library" section.
Find the Translation API:
Use the search bar to find "Cloud Translation API."
Click on it in the search results.
Enable the API:
Click "Enable" to enable the Translation API for your project.
#### Step 4: Create Credentials for Your Project
Create Service Account Credentials:
In the GCP Console, go to the "APIs & Services" > "Credentials" section.
Click "Create Credentials" and select "Service account."
Fill out the required fields and click "Done."
Download Credentials JSON File:
After creating the service account, click on the newly created service account.
Click "Add Key" and select "JSON."
Save the downloaded JSON file securely, as it contains your API key.
#### Step 5: Use the API Key in Your Code
In your Python code, use the API key from the JSON file you downloaded to authenticate requests to the Translation API. 
