
### README  for Django Job Board Platform

**Project Name: Django Job Board Platform**

**Description:**
The Django Job Board Platform is a web application designed to facilitate the connection between job seekers and employers. Built with Django, this platform allows users to create profiles, post job listings, apply for jobs, and manage applications.

### Features
- **User Authentication**: Register, log in, and manage sessions.
- **Profile Management**: Users can create and update their profiles, including uploading resumes and adding skills.
- **Job Listings**: Employers can post job vacancies with details such as job description, requirements, and location.
- **Job Applications**: Job seekers can view listings and submit applications directly through the platform.
- **Communication Tools**: Built-in messaging system for users to communicate.
- **Admin Panel**: For managing users, job postings, applications, and site settings.

### Technologies Used
- **Django**: Web framework for building the platform.
- **PostgreSQL**: Database system for storing user and job data.
- **Bootstrap**: Front-end framework for responsive design.
- **JavaScript**: Enhancements and interactivity on the client side.
- **Heroku**: Cloud platform for hosting the application.

### User Stories

**Job Seeker:**
- As a job seeker, I want to register and create my profile so that I can apply for jobs.
- As a job seeker, I want to search and filter job listings to find positions that match my skills.
- As a job seeker, I want to apply for jobs directly on the platform to streamline my job search process.

**Employer:**
- As an employer, I want to post job vacancies to find suitable candidates.
- As an employer, I want to review applications and manage candidates to fill my open positions efficiently.
- As an employer, I want to communicate with job seekers to discuss their applications.

**Admin:**
- As an admin, I want to manage all user accounts and postings to maintain the integrity of the platform.

### Entity-Relationship Diagram (ERD)
Please refer to the ERD included in the project repository for a detailed overview of the database schema. This diagram illustrates how entities like Users, Profiles, Job Listings, and Applications are interconnected.



<a class="nav-link" href="https://app.diagrams.net/?title=Copy%20of%20jobsPortal.drawio&client=1">JobPortal ERD</a>

### Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tochi-bot/Django-portal-jobs
   cd django-job-board
   ```

2. **Set up a virtual environment:**
   ```bash
  `
   ```

3. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Set up the database:**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python3 manage.py runserver
   ```

   
  **ALLOWED_HOSTS** = [
    'django-job-board.herokuapp.com',
    'localhost',
    '8000-tochibot-djangojobboard-51hlrq7hots.ws.codeinstitute-ide.net',
    'jango-job-board-bc5be9075c6b.herokuapp.com'
]

7. **Visit admin panel:**
   Navigate to `https://8000-tochibot-djangojobboard-51hlrq7hots.ws.codeinstitute-ide.net/admin` to manage the application through Django’s admin panel.

