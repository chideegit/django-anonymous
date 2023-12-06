# Django-Anonymous

Now your friends and colleagues can give you a review while remaining anonymous.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Description

Who doesn't like an anonymous review?! The reviewers feel safe to share what they think about something and you in turn can hinge of the suspense to guessing who posted what and if the review connects any dot. You can easily share the review link with your friends and colleagues to leave a review. Maybe a review for yourself, your processes, products or company. Either ways, you get to enjoy truthful reviews. 

## Features

Here are what makes the project tick! Please go through the features to see why this project is awesome!

- Simple Dashboard
    - This is the landing page for all authenticated users. However, users would be directed to the login page when they are not authenticated. 
    - You can add customizations to change the looks of the dashboard to suit your taste. 
- User Authentication
    - Users would need to register to get their own profile and a shareable link. 
    - Anonymous users can interact with the app, but would need to be signed in if they want to read their own reviews 
- Default Message Framework Integration
    - This only improves the user's experience by letting them know the outcome of the operations that they've completed within the applicaition.

## Installation

Setting up and installing this project is quite straightforward and easy. Below are detailed step on how to get this web app up and running. 

1. Install a virtual environment. 
```bash
pip intall virtualenv

```

2. Create and activate a virtual environment 
```bash
virtualenv generic_name

cd generic_name && Scripts\activate
```

3. Clone the project's github repo and cd into project
```bash
git clone https://github.com/chideegit/django-anonymous

cd django-anonymous
```

4. Install all the dependencies contained in the [requirements.txt](./requirements.txt) file. 
```bash
pip install -r requirements.txt
```

5. Make migrations, migrate and  then run local server 
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Usage
Navigating through the app is as easy as it look. You can follow through the steps below to have an idea of the experience before diving in yourself.

1. Navigate to http://127.0.0.1:8000/ 
2. If there's an existing account, then you would have to log in, if not, click on the 'Sign Up' link to create a new user account. 
3. After creating a new user account, you'd be required to log in. 
4. Once logged in, you can copy your shareable link and share with your friends and colleagues on all social media platforms. 
5. When the review starts coming in, you can easily view it directly in your dashboard, in real time. 

## Contributing
If you would like to contribute to the project, please follow the guidelines outlined in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

## License
This project is licensed under the MIT License - see the [LICENSE file](./LICENSE) for details.

## Acknowledgments
Special thanks to the Django community for providing a robust framework.

Feel free to reach out for any questions, issues, or feature requests!

Happy coding🚀