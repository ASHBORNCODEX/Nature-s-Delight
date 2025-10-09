# My Django Project

This is a demo-ready version of my Django project for interviews.

## Setup Instructions

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd <repo-folder>

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
pip install -r requirements.txt


python manage.py migrate


python manage.py loaddata sample_data.json


python manage.py runserver
