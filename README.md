DISTRIBUTED URL SHORTNER

A URL shortening service built using Python and Flask. This project converts long URLs into short, easy-to-share links using Base62 encoding and stores the URL mappings in a database.

## Features
- Generate short URLs from long URLs
- Redirect short URLs to the original URLs
- Base62 encoding for compact URL generation
- Persistent URL storage using SQLite
- REST API based implementation
- Optional Redis caching support
- Error handling for invalid URLs

## Technologies Used
- Python
- Flask
- SQLite
- Redis (Optional)
- Base62 Encoding
- REST API

## File Description
| app.py | Contains Flask API routes for URL shortening and redirection |
| database.py | Handles SQLite database connection and table creation |
| encoder.py | Implements Base62 encoding algorithm |
| cache.py | Handles optional Redis cache configuration |
| requirements.txt | Contains required Python packages |
| urls.db | Stores URL mappings |
| README.md | Project documentation |

## Installation

### 1. Clone the repository
git clone <>

### 2. Navigate to the project directory
cd distributed-url-shortener

### 3. Create a virtual environment
python -m venv venv

### 4. Activate the virtual environment
Windows:
venv\Scripts\activate

### 5. Install dependencies
pip install -r requirements.txt

## Running the Application
Start the Flask server:
python app.py

The application will run at:
http://127.0.0.1:5000

## API Usage
## 1. Generate Short URL
### Endpoint
POST /shorten

### Request
Send form data:
url=https://example.com

### Example using curl
curl.exe -X POST -F "url=https://google.com" http://127.0.0.1:5000/shorten

### Response
json
{
    "short_url": "http://127.0.0.1:5000/1"
}

## 2. Redirect to Original URL
Open the generated short URL:
http://127.0.0.1:5000/1
The application will redirect the user to the original URL.

## How It Works
1. User submits a long URL through the API.
2. The URL is stored in the SQLite database.
3. A unique database ID is generated.
4. The ID is converted into a Base62 encoded short code.
5. The short URL is returned to the user.
6. When the short URL is accessed, the code is decoded.
7. The original URL is retrieved and the user is redirected.

## Base62 Encoding
Base62 encoding converts numeric IDs into shorter strings using:
0-9, a-z, A-Z
Example:
Database ID: 62
Encoded value: 10

This allows the application to generate compact URLs.

## Database Design
The application uses SQLite with the following table:

### URLs Table

| Column | Description |
|--------|-------------|
| id | Unique identifier |
| long_url | Original URL |

## Redis Caching
Redis support is included as an optional caching layer.
When enabled:
- Frequently accessed URLs can be stored in memory.
- Redirect response time can be improved.
- Multiple application instances can share cached data in a distributed setup.

## Future Improvements
- Add URL expiration time
- Add click tracking and analytics
- Add user authentication
- Add rate limiting using token bucket algorithm
- Replace SQLite with PostgreSQL/MySQL
- Deploy using Docker and cloud services
- Add load balancing for multiple server instances

  ## Author
  YASHU A.B.

