import requests
from bs4 import BeautifulSoup
import os
import PyPDF2  # Install using `pip install PyPDF2`

# Function to scrape a webpage
def scrape_laws_from_website(url, output_folder="scraped_data"):
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all links and text content
        links = soup.find_all('a', href=True)
        law_texts = soup.find_all(['p', 'div', 'span'])  # Adjust tags as needed

        # Save plain text content
        with open(os.path.join(output_folder, 'laws_text.txt'), 'w') as text_file:
            for law_text in law_texts:
                text_file.write(law_text.get_text(strip=True) + '\n')

        # Download and extract PDFs
        for link in links:
            href = link['href']
            if href.endswith('.pdf'):
                pdf_url = href if href.startswith('http') else url + href
                pdf_response = requests.get(pdf_url)
                pdf_path = os.path.join(output_folder, os.path.basename(href))
                with open(pdf_path, 'wb') as pdf_file:
                    pdf_file.write(pdf_response.content)
                print(f"Downloaded PDF: {pdf_path}")

                # Extract text from the PDF
                with open(pdf_path, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    pdf_text = ""
                    for page in pdf_reader.pages:
                        pdf_text += page.extract_text()
                
                # Save extracted PDF text
                pdf_text_path = os.path.splitext(pdf_path)[0] + '_text.txt'
                with open(pdf_text_path, 'w') as pdf_text_file:
                    pdf_text_file.write(pdf_text)
                print(f"Extracted text from PDF: {pdf_text_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with the URL of a website containing laws
    target_url = "https://example.com/laws"  # Replace with the target URL
    scrape_laws_from_website(target_url)
