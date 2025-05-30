# BloomandBrew

Bloom and Brew is

The live link can be found here - [BloomandBrew]()

![Am I Responsive]()

## Table of Contents






## Epics and User Stories



## Design

#### Colour Scheme

This particular colour scheme was chosen as 
![Colour Palette]()

#### Imagery



#### Fonts

I chose  and  as my fonts. 

![]()

![]()

#### Wireframes

<details>

 <summary>Homepage</summary>

![Homepage]()
</details>

## Features

### Navigation Bar

- The navigation at the top of each page provides easy access to all main sections of the website.



### Footer

- The footer is at the bottom of each page and contains social links. I made sure these links opened in another tab to prevent users from being driven away from the site.

![Footer](docs/readme-images/footer.png)

### Home Page



### Profile

- The profile page has user's

![Profile]()

### Sign Up

- When a user signs up, a profile is automatically created for them.

![Sign Up]()

### Log In



![Log In]()

### Error pages
- I created my own error pages and these have navigation buttons.

![Log In]()

### Success Messages
- Success messages inform the user if they have made any changes to their 
![Success]()

## Future Features

In the future I would like to add the following features to further improve the site:

## CRUD Functionality

- User's can Create, Read, Update and Delete both their . 

## Agile Methodology

Github projects was used to manage the development process using an agile approach. Please see link to my project board:

[Project Board]()

## Data Model

This is the data model I designed. It has the Django built-in user model that handles authentication and basic user information. 

![Database Schema]()

## Testing

### HTML

HTML was passed through the W3C validator with no errors.

| Page                   | Result     |
|------------------------|------------|
| base.html              | No errors  |
| home.html              | No errors  |
| all.trips.html         | No errors  |
| create_trip.html       | No errors  |
| delete_trip.html       | No errors  |
| edit_trip.html         | No errors  |
| my_trips.html          | No errors  |
| suggest_activity.html  | No errors  |
| trip_details.html      | No errors  |
| profile.html           | No errors  |
| delete_profile.html    | No errors  |
| edit_profile.html      | No errors  |
| login.html             | No errors  |
| signup.html            | No errors  |
| 403.html               | No errors  |
| 404.html               | No errors  |
| 500.html               | No errors  |


### CSS

CSS was passed through W3C validator with no errors.

### JavaScript

JavaScript was passed through JShint with no errors.

### Python

Python code was passed through the PEP8 CI linter with no errors.

## General Testing


| Test             | Action                                                                 | Success Criteria                                                 |
| --------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Homepage loads**  | Navigate to website URL                                            | Page loads with no errors                     |
| **Links**          | Click on each navigation link, CTAs, buttons, logo, and footer links  | Correct page loads or correct action performed, new tab opens if applicable |
| **Form validation** | Enter data into each input field, ensuring only valid data is accepted  | Form does not submit until correct data is entered, and an error message is shown |
| **Responsiveness**  | Resize viewport window from 320px upwards using Chrome DevTools. Test various devices  | Page layout remains intact and adapts correctly to different screen sizes |

### Lighthouse

Lighthouse validation was run on all pages (both mobile and desktop).  Here are the scores: 

| Page           | Performance  | Accessibility | Best Practices  | SEO |
|----------------|:------------:|:-------------:|:---------------:|:---:|
|                |              |               |                 |     |
| Home           |          97  |           98  |             100 | 100 |
| My Trips       |          98  |           98  |             100 | 100 |
| Trip Details   |          99  |           98  |             100 | 100 |
| Delete trip*   |          99  |           98  |             100 | 100 |
| Create trip*   |          99  |           98  |             100 | 100 |
|SuggestActivity |          100 |           100 |             100 | 100 |
| Delete Trip    |          100 |           100 |             100 | 90  |
| Edit Trip      |          90  |           100 |             100 | 100 |
|All Trips(admin)|          89  |           98  |             100 | 90  |
| Profile        |          98  |           98  |             100 | 100 |
| Login          |          99  |           99  |             100 | 100 |
| Signup         |          100 |           99  |             100 | 100 |
| Edit Profile   |          98  |           100 |             100 | 100 |
| Delete Profile |          98  |           100 |             100 | 91  |

## Browser Testing
The Website was tested on Google Chrome, Firefox, Safari browsers with no issues.

## Security Features

### User Authentication
Authorisation is required to reach certain pages such as . Requesting these pages while unauthorised will redirect users to the Login page.

### Form Validation
Incorrect or in certain cases empty data in forms is not accepted and the user is made aware.

### Database Security
The database url and secret key are stored in the .env file to prevent unwanted connections.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.


## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Login to the Heroku dashboard and create a new app.
2. Connect your GitHub repository to your Heroku app.
3. Set environment variables in the Config Vars section of the Settings tab.
4. In the Deploy tab, enable automatic deploys from your GitHub repository.
5. Click the "Deploy Branch" button to deploy the app.
6. Once the app has been deployed, click the "Open App" button to view the app.

-  Under 'Config Vars' the following variables to be set:

    - `DATABASE_URL` - the URL for your Postgres database.
    - `NAME` - the name of your database.
    - `USER` - the username for your database.
    - `PASSWORD` - the password for your database.
    - `HOST` - the host for your database.
    - `PORT` - the port for your database.
    - Django settings:
    - `SECRET_KEY` - the secret key for your Django project. (kept in .env file)
    - `DEBUG` - set to `True` for development, `False` for production.

## Cloning Repository

### <ins> Step 1: </ins>

From the <a href="https://github.com/Amelia5p/travel-planner" target="_blank">GitHub repository</a> click on the 'code' button.

### <ins> Step 2:</ins>

Click 'local' on the top of the drop down menu and copy the URL.

### <ins>Step 3: </ins>

Open Git Bash on windows and change the working directory to the location where you want the cloned directory.

### <ins>Step 4: </ins>

Type 'Git clone' followed by a space and paste the URL previously copied, hit enter.

### <ins> Result: </ins> 

You now have a local copy of the Github repository.

## Forking Repository

### <ins>Step 1:</ins>

From the <a href="https://github.com/Amelia5p/travel-planner" target="_blank">GitHub repository</a> click on the 'fork' button in the top right corner of the page. 

### <ins>Step 2:</ins> 

Choose to copy only the main branch or all branches to the new fork.

### <ins>Step 3: </ins>

Click Create a Fork.

### <ins>Result:</ins>

There is now a forked copy on GitHub.


## Languages

- Python
- HTML
- CSS
- Javascript

### Programs used
- [Django](https://www.djangoproject.com/): main python framework used in the development of this project.
- [Heroku](https://dashboard.heroku.com/login) - used as the cloud based platform to deploy the site on.
- [Balsamiq](https://balsamiq.com/) - used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - used for overall development and testing.
- [Font Awesome](https://fontawesome.com/) - used for icons.
- [GitHub](https://github.com/) - used for agile tool.
- [Google Fonts](https://fonts.google.com/) - used to import fonts.
- [W3C](https://www.w3.org/) - used for HTML & CSS Validation.
- [PEP8 CI Linter](https://pep8ci.herokuapp.com/) - used to validate all the Python code.
- [Jshint](https://jshint.com/) - used to validate javascript.
- [Favicon](https://favicon.io/) - used to create the favicon.
- [Mermaid](https://mermaid.live/) - used to create the database schema design
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/):Framework for developing responsiveness and styling
- [Am I responsive](https://ui.dev/amiresponsive) used for responsive picture
- [Coolors](https://coolors.co/) used for creating colour palette

## Bugs

- Some users do not have a Profile associated with them- fixed by using django signals to auto make profile when sign up.






## Credits
- [Code Institute - Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode)




## Acknowledgements 
This is the fifth and final project, created for the Code Institutes Full Stack Web Developer (eCommerce) course. I would like to thank my cohort facilitator and the Code Institute team for their support.