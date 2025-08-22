# WordPulse - Online Product Review Analyzer

An intelligent sentiment analysis web application that automatically classifies e-commerce product reviews into positive, negative, and neutral categories using natural language processing.

## Project Overview

WordPulse helps e-commerce companies process thousands of product reviews efficiently by automating sentiment analysis. Instead of manually reading through reviews, businesses can now get instant insights into customer satisfaction and identify areas for improvement.

## Problem Statement

E-commerce companies receive thousands of product reviews daily. Manually analyzing these reviews to understand customer sentiment is:
- Time-consuming and resource-intensive
- Prone to oversight and human error
- Difficult to scale with growing review volumes
- Slow to provide actionable business insights

## Research Question

"How can we automatically analyze customer reviews to determine whether they are positive, neutral, or negative?"

## Key Features

### Core Functionality
- CSV Upload: Easy file upload for review datasets
- Text Preprocessing: Automated cleaning and tokenization
- Sentiment Classification: Real-time analysis using TextBlob
- Interactive Visualizations: Dynamic charts and graphs
- Export Reports: Downloadable analysis results

### Functional Components
- Input text cleaning module - Preprocesses raw review data
- Sentiment prediction model - TextBlob-powered classification
- Classification display with visual chart - Interactive result visualization
- Aggregate score generation per product - Product-level insights
- Export sentiment report - Comprehensive downloadable reports

## Sample Dataset Format

Review Text,Rating
"Excellent product and quality!",5
"Poor packaging and late delivery.",2
"Average experience, nothing special.",3

## Expected Output

- Positive Reviews: 70%
- Negative Reviews: 20%
- Neutral Reviews: 10%

Plus detailed metrics, confidence scores, and product-wise breakdowns.

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Quick Start

1. Clone the repository
   git clone https://github.com/yourusername/wordpulse.git
   cd wordpulse

2. Install dependencies
   pip install -r requirements.txt

3. Run the application
   streamlit run WordPulse.py

4. Open your browser and navigate to http://localhost:8501

## Dependencies

streamlit
pandas
textblob
matplotlib
seaborn
plotly
numpy

## How to Use

1. Launch the App: Run streamlit run WordPulse.py
2. Upload Data: Use the file uploader to select your CSV file
3. Analyze: Click the analyze button to process reviews
4. Explore Results: View interactive charts and insights
5. Export: Download detailed reports for further analysis

## Project Structure

wordpulse/
├── WordPulse.py          # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── sample_data/         # Sample datasets
└── screenshots/         # Application screenshots

## Technology Stack

- Frontend: Streamlit
- Backend: Python
- NLP: TextBlob
- Data Processing: Pandas
- Visualization: Matplotlib, Plotly
- Deployment: Streamlit Cloud (optional)

## Use Cases

- E-commerce Platforms: Monitor product satisfaction
- Marketing Teams: Understand customer perception
- Product Managers: Identify improvement opportunities
- Customer Service: Prioritize response to negative feedback
- Business Intelligence: Track sentiment trends over time

## Future Enhancements

- Advanced ML models (BERT, RoBERTa)
- Multi-language support
- Real-time sentiment monitoring
- API integration
- Cloud deployment options
- Mobile-responsive design
