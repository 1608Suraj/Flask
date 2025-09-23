# Flask & Python Interview Q\&A

### 1. What is Flask? Why is it called a microframework?

* Flask is a **lightweight Python web framework** used to build web apps and APIs.
* It’s called a **microframework** because it only provides essentials (routing, request/response) and relies on extensions for extra features.

---

### 2. Compare Flask, Django, and FastAPI.

* **Flask** → Lightweight, flexible, minimal setup, great for small/medium apps.
* **Django** → Full-stack, batteries-included (ORM, admin, auth), good for large projects.
* **FastAPI** → Modern, high-performance, async-based, auto API docs, best for APIs.

---

### 3. What is @app.route() in Flask and why do we use it?

* `@app.route()` is a **decorator** that maps a URL to a function.
* Example:

```python
@app.route("/hello")
def hello():
    return "Hello, Flask!"
```

Visiting `/hello` runs `hello()`.

---

### 4. What is the difference between path parameters and query parameters in Flask?

* **Path parameter** → Part of the URL itself. Example: `/user/5`.
* **Query parameter** → Passed after `?` in the URL. Example: `/search?name=suraj`.

---

### 5. How do you access query parameters inside a Flask route?

```python
from flask import request

@app.route("/search")
def search():
    name = request.args.get("name")
    return f"Searching for {name}"
```

---

### 6. What does debug=True do in app.run()?

* Enables **debug mode**:

  * Shows detailed error messages in browser.
  * Auto-reloads server when code changes.

---

### 7. What is the purpose of the request object in Flask?

* Represents the **incoming HTTP request**.
* Lets us access form data, query params, JSON, headers, cookies, and HTTP method.

---

### 8. Explain the Request → Response Lifecycle in Flask.

1. Client sends a **request** (URL + data).
2. Flask matches the request to a **route** (`@app.route`).
3. Flask runs the matched **view function**.
4. Function returns a **response** (HTML, JSON, text).
5. Flask sends the response back to the client.

---

### 9. What is type hinting in Python? Show an example.

* Type hinting specifies the expected **types of variables/returns** in a function.

```python
def add(x: int, y: int) -> int:
    return x + y
```

---

### 10. Write a Python function to check if a number is prime.

```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False
```
