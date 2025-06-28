# Patient Registration Flask Application

A simple Flask application for patient registration with therapist assignment. This application allows users to submit patient information through a web form with secure database storage.


## Features

- **Simple Registration Form** - Patient first name, last name, date of birth, and therapist name
- **SQLite Database Storage** - Automatic table creation and data persistence
- **Jinja2 Templating** - Dynamic confirmation page displaying submitted data
- **Clean Form Validation** - Required field validation
- **Confirmation Display** - Shows entered information after successful submission


## Technologies Used

- **Python 3.x**
- **Flask** - Lightweight web framework
- **SQLite** - Embedded database storage
- **Jinja2** - Template rendering for dynamic content
- **HTML5** - Clean form interface


## Installation

1. **Clone or download the project files**
   ```bash
   cd flask_screening
   ```

2. **Install required dependencies:**
   ```bash
   pip install flask
   ```
   
3. **Run the application:**
    ```bash
    python app.py
    ```
   
4. **Access the application:**
   Open your web browser and go to `http://localhost:5000`


## Project Structure

```
flask_screening/
├── app.py                   # Main Flask application
├── patients.db              # SQLite database (auto-created)
├── static/
├── templates/
│   ├── confirmation.html    # Success confirmation page with Jinja2 templating
│   └── form.html            # Patient registration form
└── README.md                # Project documentation
```


## Application Routes

* **`/`** - Main registration form page
* **`/submit`** - Form submission handler (POST only)


## Form Fields

The screening form collects the following information:
* Patient First Name (required)
* Patient Last Name (required)
* Date of Birth (required)
* Therapist Name (required)


## Database Schema

**Table:** `patients`
```sql
- id (INTEGER PRIMARY KEY AUTOINCREMENT)
- first_name (TEXT NOT NULL)
- last_name (TEXT NOT NULL)
- date_of_birth (TEXT NOT NULL)
- therapist_name (TEXT NOT NULL)
- submitted_at (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
```


## Jinja2 Usage
The confirmation page uses Jinja2 templating to display submitted data:
* `{{ first_name }}` - Patient's first name
* `{{ last_name }}` - Patient's last name
* `{{ date_of_birth }}` - Patient's date of birth
* `{{ therapist_name }}` - Assigned therapist name



## Usage Workflow

1. Navigate to the home page
2. Fill out the patient registration form
3. Submit the form
4. View confirmation page with entered details
5. Data is automatically stored in SQLite database


## License

This project is licensed under the MIT License. See the LICENSE file for details.


## Support

For questions or issues, please refer to the Flask documentation or create an issue in the project repository.