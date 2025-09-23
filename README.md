# Flask Repo

This repository contains simple Flask examples demonstrating basic
routing, string manipulation, and a number‑checking endpoint.

------------------------------------------------------------------------

## 📁 Repository Structure

    Flask/
    ├── first.py        # Flask app with several routes
    ├── Interview.md    # Q&A document for Flask/Python interview prep
    └── README.md       # This file

------------------------------------------------------------------------

## 🚀 Getting Started

These steps will help you run the Flask app locally.

### Prerequisites

-   Python 3.x installed\
-   `pip` for installing dependencies

### Installation & Running

1.  Clone the repo:

    ``` bash
    git clone https://github.com/1608Suraj/Flask.git
    cd Flask
    ```

2.  Install Flask:

    ``` bash
    pip install flask
    ```

3.  Run the app:

    ``` bash
    python first.py
    ```

    The app runs in **debug mode** and listens by default on
    `http://127.0.0.1:5000`

------------------------------------------------------------------------

## 🧰 Functionality / Routes

Here are the example endpoints provided:

  ----------------------------------------------------------------------------------------
  Route                      Method                  Purpose
  -------------------------- ----------------------- -------------------------------------
  `/`                        GET                     Returns "Hello, World!"

  `/reverse/<string:text>`   GET                     Returns the original text plus its
                                                     reverse. Example: `/reverse/hello` →
                                                     `Original: hello | Reversed: olleh`

  `/check/<int:num>`         GET                     Checks if `num` is an Armstrong
                                                     number. Example: `/check/153` → "153
                                                     is an Armstrong number!"
  ----------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🔧 Notes

-   The code is using `debug=True` in `app.run()` so any changes to the
    code will auto‑reload the server, and detailed errors are shown in
    browser.\
-   Path parameters (like `<string:text>` and `<int:num>`) are used to
    pass data via the URL path.

------------------------------------------------------------------------

## ✅ Contributing

Feel free to suggest enhancements, add new routes / examples, or fix
issues. Fork & pull requests are welcome.

------------------------------------------------------------------------

## 📄 License

This project is open source. Use it freely.
