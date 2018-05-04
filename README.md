# Comparing Python With Javascript
> Which one is more effective?  
> Which one requires less code?  
> Which one takes up the least memory when built?

## The challange
> The challange is to build a JSON API, the API should do the following:

* Have an endpoint to register users
* Have an endpoint to fuzzy search users by their username
* Have an endpoint to send a message to a user
* Encrypt the users password when registering

### The endpoints
> _registering a user_:  
> `PUT: /api/user`  
> This accepts a JSON object with all the fields of the `User` Model.

> _fuzzy search users_:  
> `GET: /api/user?q={query}`

> _sending a message to a user_:  
> `PUT /api/message/{user_id}`  
> This accepts a JSON object with all the fields of a message.

### The models
> _The User model_:

* username - String
* email - String
* password - String

> _The Message model_:

* message - String
* created - Datetime

> How you connect messages with users is _up to you!_.
