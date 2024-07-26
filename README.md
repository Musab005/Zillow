A web scraping project that scrapes properties from the Zillow website with specific filters (For sale, Manhattan NY, $100k-$300k). Cover images of the listings are also scraped and stored in the folder ./Zillow/images.

To run this project:

Activate the anaconda virtual environment: `conda activate {virtual env name}`
Install Pillow: `conda install Pillow -y`
Run the spider: `scrapy crawl Zillow -o listings.json`
