# Event Management System (EMS)

This is an Event Management System (EMS) designed to manage events, handle user profiles, and allow for login/logout functionality. It includes features such as viewing a list of events, accessing detailed event information, and managing user profiles.

## Features
- **Event Management**: Allows users to view a list of events and their details.
- **User Authentication**: Users can log in, view their profiles, and log out.
- **Event Details**: Users can view detailed information about events.
- **Profile Management**: Authenticated users can access and manage their profiles.

## Technologies Used
- **Django**: For the backend API and server-side logic.
- **HTML/CSS**: For front-end UI, including event cards and navigation bar.
- **Font Awesome**: For icons in the UI.
- **JavaScript**: For interactive elements, such as the dropdown menu for user profiles.
  
## Setup Instructions

### Prerequisites

Make sure you have the following installed on your system:
- Python 3.x
- Django
- Other required Python libraries (listed in `requirements.txt`)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/EventManagementSystem.git
   cd EventManagementSystem
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```

3. **Install dependencies**:
   Create a `requirements.txt` with the following content:
   ```
   Django>=3.0
   ```

   Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up database**:
   Make sure the database is set up and run the migrations:
   ```bash
   python manage.py migrate
   ```

5. **Run the server**:
   Start the development server:
   ```bash
   python manage.py runserver
   ```

   The application should now be accessible at `http://127.0.0.1:8000/`.

## File Structure

```
EventManagementSystem/
├── myapp/
│   ├── migrations/
│   ├── static/
│   │   └── profile-user.png
│   │   └── styles.css
│   ├── templates/
│   │   └── base.html
│   │   └── event_list.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── db.sqlite3
```

### Static Files:
- The **static files** (CSS and images) are placed in the `myapp/static/` directory.
- **styles.css**: Contains the main styles for the event list and layout.
- **profile-user.png**: Default profile icon for users.

### Templates:
- **base.html**: The main template that defines the general layout (header, footer, and navigation).
- **event_list.html**: Template for displaying the list of events and their details.

## Contributing

If you'd like to contribute to the development of this project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.
