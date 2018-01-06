# Wordplease

## API usage

**Note: Some endpoints require authentication.**

### How to register an user

First register yourself in the application using the following route:
**POST** [http://localhost:8000/api/1.0/users/](http://localhost:8000/api/1.0/users/)

With some Body like:
```json
{
    "username": "pablito",
    "email": "mail@mail.com",
    "first_name": "Pablito",
    "last_name": "Perez",
    "password":"supersegura"
}
```

### How to get user Token

**Note: The user need to be registered in the application**

To get your token you need to do a **POST** request with the following body:

**POST** [http://localhost:8000/api/1.0/users/get-token/](http://localhost:8000/api/1.0/users/get-token/ "Get user Token")
```json
{
    "username": "pablito",
    "password":"supersegura"
}
```

### Getting available blogs

[http://localhost:8000/api/1.0/blogs/](http://localhost:8000/api/1.0/blogs/ "All Blogs")

### Getting posts from user blog

[http://localhost:8000/api/1.0/blogs/\<username\>](http://localhost:8000/api/1.0/blogs/luis "User Blog")

### How to search for a post within a blog

**The following query_params are allowed:**
* **search:** This will allow you to look in the **title OR body** fields of posts.
* **title:** This will allow you to look in the **title** field of posts.
* **body:** This will allow you to look in the **body** field of posts.

**Examples:**
* Look for posts in username's blog containing case insensitive "wanted_word" in title or in the body.
 [http://localhost:8000/api/1.0/blogs/\<username\>?search=wanted_word](http://localhost:8000/api/1.0/blogs/luis?search=wanted_word "User's Blog posts with the word wanted_word in the body or the title")
* Look for posts in username's blog containing case insensitive "wanted_word" in title.
 [http://localhost:8000/api/1.0/blogs/\<username\>?title=wanted_word](http://localhost:8000/api/1.0/blogs/luis?title=wanted_word "User's Blog posts with the word wanted_word in the title")
* Look for posts in username's blog containing case insensitive "wanted_word" in body.
 [http://localhost:8000/api/1.0/blogs/\<username\>?body=wanted_word](http://localhost:8000/api/1.0/blogs/luis?body=wanted_word "User's Blog posts with the word wanted_word in the body")
* Look for posts in username's blog containing case insensitive "wanted_word" in body and "wanted_word2" in title.
 [http://localhost:8000/api/1.0/blogs/\<username\>?body=wanted_word&title=wanted_word2](http://localhost:8000/api/1.0/blogs/luis?body=wanted_word&title=wanted_word2 "User's Blog posts with the word wanted_word in the body and wanted_word2 in title")

**Note:** Body or title query_params will have priority over search query_param.

### How to order the posts

Simply add the query_param **order_by**. Possible values are:

* **title**, will return results in ascending order.
* **publication_date**, will return results in ascending order.
* **-title**, will return results in descending order.
* **-publication_date**, will return results in descending order.

**Example:**
[http://localhost:8000/api/1.0/blogs/\<username\>?order_by=title](http://localhost:8000/api/1.0/blogs/luis?order_by=title "User's Blog posts sorted by title in ascending order")


### How to create a post

You need to be authenticated to reach this endpoint.

You will need the following Headers on your POST request:
* **Content-Type:** application/json
* **Authorization:** Token 4f5dbe4c76decf3eb187aea636fa68efd3855ef9

Then, you will need to specify some Body in your request:

```json
{
    "title": "Your title",
    "image": "https://source.unsplash.com/random",
    "summary": "The summary",
    "body": "The body",
    "publication_date": "2014-12-10",
    "category":[1,2]
}
```

Or

```json
{
    "title": "Your title",
    "video": "https://source.unsplash.com/random",
    "summary": "The summary",
    "body": "The body",
    "publication_date": "2014-12-10",
    "category":[1,2]
}
```

Then you need to perform the request

**POST** [http://localhost:8000/api/1.0/posts/](http://localhost:8000/api/1.0/posts/)


### How to retreive the detail of a post
If you are authenticated you will see unpublished post if you are a superuser or if your tokens belongs to the post owner
**GET** [http://localhost:8000/api/1.0/posts/\<id\>](http://localhost:8000/api/1.0/posts/\<id\>)
