# Zillow

A web scraping project that scrapes rental listings from the Zillow website using a web spider that runs on Scrapy. Specific filters were used (For sale, Manhattan NY, $100k-$300k). Cover images of the listings are also scraped and stored in the folder ./Zillow/images.

To run this project:

Activate the anaconda virtual environment: `conda activate {virtual env name}`

Install Pillow: `conda install Pillow -y`

Run the spider: `scrapy crawl Zillow -o listings.json`
