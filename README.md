# Django and React

Basic scaffold for a quiz that gives recommendations using Django, Django Rest Framework and React.

The initial inspiration was that I wanted a quiz to tell me what kind of software engineer I should be (frontend, backend, fullstack, data, ux, etc.), and I also wanted to build something other than a blog with Django (which I'm also building). In the end, I decided it should be more generic, so it's a quiz for anything.

## Admin Login

username: admin

password: admin

email: admin@admin.com

## Documentation

Here's a data model diagram!
![Image](docs/rec_quiz_data.png "data diagram")

## Helpful Resources

[Making React and Django play well together](https://fractalideas.com/blog/making-react-and-django-play-well-together/)

[Tutorial: Django REST with React (Django 2.0 and a sprinkle of testing](https://www.valentinog.com/blog/tutorial-api-django-rest-react/)

## Commentary

I don't think Django is actually a good backend solution for this app. I'm only using half of what Django does, when there are smaller single-purpose packages that do what I need - in this case, an API, authentication and data modeling. I like the ease of which I could use those features, but using Django is a bit overkill. React is bit overkill as well. I would prefer lighter frameworks to manage state and views, each separately.

I'm a firm believer in cohesion, decoupling and modularizing as much as possible. Building something with both Django and React in accordance with my coding philosophy is really testing my faith.
