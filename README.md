# Comparing Python With Javascript
> Which one is more effective?  
> Which one requires less code?  
> Which one takes up the least memory when built?

## The challange
> The challange is to build a JSON API, the API should do the following:

* Have an endpoint to register users
* Have an endpoint to fuzzy search users by their username
* Have an endpoint to send a message to a user
* Have an endpoint to fetch all messages that a user has sent
* Have an endpoint to fetch all messages that has been sent to a user
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

> _fetching messages that a user has sent_:  
> `GET /api/message/{user_id}/sent`

> _fetching messages that has been sent to a user_:  
> `GET /api/message/{user_id}/received`

### The models
> _The User model_:

* username - String
* email - String
* password - String

> _The Message model_:

* message - String
* created - Datetime
* sender - User
* receiver - User

### Database
> For simplicity, you should only store data in plain JSON files on
> the filesystem.
