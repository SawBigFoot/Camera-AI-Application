# Fennoscandia Studios Website

This repository contains the front-end code for Fennoscandia Studios, a platform offering AI-based identity detection through facial recognition technology. Below is an overview of the different pages and their functionalities.

## Pages Overview:

1. **Home Page**  
   **Description**: The landing page for Fennoscandia Studios, welcoming users to explore the platform.  
   **Features**:
   - **Navigation Bar**: Links for logging in and signing up.
   - **Styling**: Tailored design with custom fonts and colors, including a soft, warm color palette of beige and orange.
   - **Buttons**:
     - Logg Inn: Redirects to the login page.
     - Registrer Deg: Redirects to the sign-up page.
   - **Main Message**: Welcomes users and briefly introduces the AI facial recognition technology.

2. **Login Page**  
   **Description**: A simple login page for existing users.  
   **Features**:
   - **Username and Password Inputs**: Required fields for logging in.
   - **Error Message**: Displays an error message if login fails (via {{ info }}).
   - **Submit Button**: Allows users to log in.
   - **Link to Sign-up**: A redirect for users who don't have an account yet.

3. **Signup Page**  
   **Description**: A page allowing new users to register for the platform.  
   **Features**:
   - **Form Fields**: Username, email, and password input fields.
   - **Validation**: Password has a 12-character limit, and email input ensures proper formatting.
   - **Modal for Verification**: After submitting the signup form, a modal appears for the user to enter a verification code sent to their email.
   - **Custom Design**: Tailored with custom fonts (TheFlameProofer) and a warm color scheme (beige, orange, dark red).

4. **Identity Detection Camera Page**  
   **Description**: The main dashboard for users to interact with the AI camera model.  
   **Features**:
   - **Welcome Message**: Displays a personalized greeting ({{ name }}) after the user logs in.
   - **Run AI Model Button**: Starts the facial recognition AI model with a loading indicator.
   - **Button Interaction**: Users can click the button to trigger the AI model and view results.
   - **Footer**: Includes copyright information.

## Design & Features:

- **Tailwind CSS**: Utilizes Tailwind for responsive, customizable styling.
- **Custom Fonts & Colors**: Incorporates custom fonts (e.g., 'TheFlameProofer') and a warm color scheme for an inviting experience.
- **Interactivity**: Buttons have hover effects and smooth transitions for a polished user experience.
- **JavaScript**: Used for handling form submission, modal management, and integration with AI technology.

## Technologies Used:

- **HTML**: Basic structure and layout of each page.
- **CSS**: Custom styling for elements such as buttons, background colors, and modals.
- **JavaScript**: Used to manage interactivity, including handling form submission, generating verification codes, and interacting with the AI camera model.

## Detailed Code Overview:

### 1. Home Page (Navigation)  
This page serves as the landing point for the users to either log in or sign up.

```html
{% extends "home.html" %}

{% block content %}
<h2 class="text-2xl font-semibold text-white">Welcome to the Sidebar App</h2>
<p class="mt-4">Click the buttons on the sidebar to navigate between forms and articles.</p>
{% endblock %}
