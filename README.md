# Flask Repo

This repository contains simple Flask examples demonstrating **basic routing, string manipulation, number checking**, and **HTML template rendering for eligibility checking**.

---

## 📁 Repository Structure

```
Flask/
├── first.py                # Day 1 Flask app (basic routes)
├── Interview.md           # Q&A document for Flask/Python interview prep
├── day2_agecheck.py       # Day 2 Flask app (eligibility check with templates)
├── templates/
│   ├── eligible.html       # Template for eligible users
│   └── noteligible.html    # Template for not eligible users
└── README.md              # This file
```

---

# 🔖 Day 1 — Basic Flask Routes

### 🚀 Features Implemented

* Root route (`/`) → returns **Hello, World!**
* Reverse string route (`/reverse/<string:text>`) → returns original and reversed string
* Armstrong number checker (`/check/<int:num>`) → checks if a number is an Armstrong number

### ▶️ Run Instructions

```bash
# Navigate into repo
cd Flask  

# Install dependencies
pip install flask  

# Run Day 1 app
python day1_first.py
```

App runs on: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 🌐 Routes Summary

| Route                    | Method | Purpose                                                                 |
| ------------------------ | ------ | ----------------------------------------------------------------------- |
| `/`                      | GET    | Returns `"Hello, World!"`                                               |
| `/reverse/<string:text>` | GET    | Returns original + reversed string (`/reverse/hello` → `olleh`)         |
| `/check/<int:num>`       | GET    | Checks if number is Armstrong (`/check/153` → Armstrong number message) |

---

# 🔖 Day 2 — Eligibility Check with Templates

### 📚 Learning (Step-up from Day 1)

* Learned how to use **Flask’s render\_template()** to connect Python with HTML
* Introduced **Jinja2 templating** to dynamically display variables (`{{ age }}`) in HTML
* Applied **separation of logic and presentation** (Python logic in `.py`, UI in `.html`)
* Understood **conditional rendering** (eligible vs not eligible)

---

<div align="center">
  <img src="https://via.placeholder.com/400x200.png?text=Eligible+Page" alt="Eligible Page" />
  <img src="https://via.placeholder.com/400x200.png?text=Not+Eligible+Page" alt="Not Eligible Page" />
</div>

---

### 🚀 Features Implemented

* Root route (`/`) → simple welcome message
* Age route (`/age/<int:age>`) → checks if a person is **eligible** or **not eligible**
* Uses **Jinja2 templates** (`eligible.html` and `noteligible.html`) for styled output

### ▶️ Run Instructions

```bash
# Navigate into repo
cd Flask  

# Run Day 2 app
python day2_agecheck.py
```

App runs on: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 🌐 Routes Summary

| Route            | Method | Purpose                                                               |
| ---------------- | ------ | --------------------------------------------------------------------- |
| `/`              | GET    | Returns a welcome message with instructions                           |
| `/age/<int:age>` | GET    | Renders an HTML page showing whether the person is **Eligible / Not** |

---

## 🧰 Notes

* Both apps run in **debug mode** (`debug=True`) for auto-reload and detailed error messages.
* **Day 1** demonstrates *basic routing & string/number logic*.
* **Day 2** introduces *Flask template rendering (HTML with Jinja2 variables)*.

---

## ✅ Contributing

Feel free to:

* Add new routes / examples
* Improve templates & UI
* Suggest enhancements via fork & pull request

---
