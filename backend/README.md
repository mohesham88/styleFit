# StyleFit Backend

This is the backend service for StyleFit, built with Django and MongoDB.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohesham88/stylefit.git
   cd stylefit/backend
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set up MongoDB:**
   - Install MongoDB and start the service
   - Configure the database connection in Django settings

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Data Structure

### Example JSON Representation
```json
{
    "Id": "1a2b3c",
    "Category": "top",
    "Color": "blue",
    "Season": "summer",
    "Type": "casual",
    "Pattern": "solid",
    "Material": "cotton",
    "Description": "Lightweight blue t-shirt for summer",
    "Image": "path/to/image.jpeg"
}
```

## Tech Stack
- Django
- Django REST Framework
- MongoDB
- Python 3.x
