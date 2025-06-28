# Patient Registration Flask Application

A simple Flask application for patient registration with therapist assignment. This application allows users to submit patient information through a web form with secure database storage and comprehensive validation.


## Features

- **Simple Registration Form** - Patient first name, last name, date of birth, and therapist name
- **SQLite Database Storage** - Automatic table creation and data persistence
- **Jinja2 Templating** - Dynamic confirmation page displaying submitted data
- **Form Validation** - Required field validation with flash messages
- **Date Validation** - Ensures date of birth is in the past
- **Error Handling** - User-friendly error messages for invalid submissions
- **Confirmation Display** - Shows entered information after successful submission


## Technologies Used

- **Python 3.x**
- **Flask** - Lightweight web framework with flash messaging
- **SQLite** - Embedded database storage
- **Jinja2** - Template rendering for dynamic content and error display
- **HTML5** - Clean form interface with styling


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
├── app.py                   # Main Flask application with validation logic
├── patients.db              # SQLite database (auto-created)
├── static/
├── templates/
│   ├── confirmation.html    # Success confirmation page with Jinja2 templating
│   └── form.html            # Patient registration form with error display
└── README.md                # Project documentation
```


## Application Routes

* **`/`** - Main registration form page
* **`/submit`** - Form submission handler with validation (POST only)


## Form Fields

The screening form collects the following information:
* Patient First Name (required)
* Patient Last Name (required)
* Date of Birth (required, must be in the past)
* Therapist Name (required)


## Validation Features

* Required Field Validation - All fields must be filled
* Date Validation - Date of birth cannot be in the future
* Flash Messages - Clear error messages displayed to users
* Form Persistence - Invalid submissions return to form with error display


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

- Confirmation page: Displays submitted data using template variables
- Form page: Shows validation error messages using Flask's flash messaging system
- Error styling: CSS styling for user-friendly error display


## Usage Workflow

1. Navigate to the home page
2. Fill out the patient registration form
3. Submit the form
4. If validation fails: View error messages and correct issues
5. If validation passes: View confirmation page with entered details
6. Valid data is automatically stored in SQLite database


## License

This project is licensed under the MIT License. See the LICENSE file for details.