# Qafza Task ETL Pipeline

This repository contains an ETL (Extract, Transform, Load) pipeline designed to automate the process of extracting data from YouTube channels, analyzing it, and storing the results in a structured format.

## Overview

The pipeline is deployed using GitHub Actions and runs automatically every day at **00:15**. Below are the key steps performed by the pipeline:

1. **Extract**:
   - Fetch videos from selected YouTube channels.
   - Scrape comments associated with these videos.

2. **Transform**:
   - Clean the extracted text data.
   - Perform sentiment analysis on the cleaned data.

3. **Load**:
   - Store the results in a CSV file for further use or analysis.


