# wordplease

## API usage

### Getting available blogs

[http://localhost:8000/api/1.0/blogs/](http://localhost:8000/api/1.0/blogs/ "All Blogs")

### Getting posts from user blog

[http://localhost:8000/api/1.0/blogs/<username>](http://localhost:8000/api/1.0/blogs/luis "User Blog")

#### How to search for a post within a blog

**The following query_params are allowed:**
* **search:** This will allow you to look in the **title OR body** fields of posts.
* **title:** This will allow you to look in the **title** field of posts.
* **body:** This will allow you to look in the **body** field of posts.

**Examples:**
* Look for posts in <username>'s blog containing case insensitive "wanted_word" in title or in the body.
... [http://localhost:8000/api/1.0/blogs/<username>?search=wanted_word](http://localhost:8000/api/1.0/blogs/luis?search=wanted_word "User's Blog posts with the word wanted_word in the body or the title")
* Look for posts in <username>'s blog containing case insensitive "wanted_word" in title.
... [http://localhost:8000/api/1.0/blogs/<username>?title=wanted_word](http://localhost:8000/api/1.0/blogs/luis?title=wanted_word "User's Blog posts with the word wanted_word in the title")
* Look for posts in <username>'s blog containing case insensitive "wanted_word" in body.
... [http://localhost:8000/api/1.0/blogs/<username>?body=wanted_word](http://localhost:8000/api/1.0/blogs/luis?body=wanted_word "User's Blog posts with the word wanted_word in the body")
* Look for posts in <username>'s blog containing case insensitive "wanted_word" in body and "wanted_word2" in title.
... [http://localhost:8000/api/1.0/blogs/<username>?body=wanted_word&title=wanted_word2](http://localhost:8000/api/1.0/blogs/luis?body=wanted_word&title=wanted_word2 "User's Blog posts with the word wanted_word in the body and wanted_word2 in title")

**Note:** Body or title lookup will have priority over search.



