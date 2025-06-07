# PRICEWISE – A Price Comparison Website 🛒💰

**PRICEWISE** is a Django-based web application designed to help users compare product prices across multiple e-commerce platforms. It enables consumers to make informed and cost-effective purchasing decisions by providing a unified interface to create shopping lists, calculate total costs per store, and find the best deals available.

---

## 🚀 Key Features

- 🔍 **Product Search & Filtering**: Search for products and refine results by brand, category, or price range.
- 🛒 **Smart Shopping List**: Add products from various retailers and track them in a centralized basket.
- 💲 **Total Cost Comparison**: Automatically calculates and displays total costs per store.
- 📈 **Scheduled Price Updates**: Periodic refresh of product data for accuracy.
- 🔐 **User Authentication**: Secure registration, login, and session management.
- ⚙️ **Admin Dashboard**: Manage users, prices, and products through Django's admin panel.

---

## 🧰 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript (Django Templating System)
- **Database:** SQLite
- **Image Processing:** Pillow
- **IDE Used:** Visual Studio Code

---

## 🛠️ Local Development Setup

To run the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/pricewise.git
cd pricewise
````

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Now open your browser and navigate to `http://127.0.0.1:8000`.

---

## 📂 Project Structure (Simplified)

```
pricewise/
├── manage.py
├── pricewise_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

## 🔮 Future Enhancements

* ✅ Real-time API-based product data scraping
* 📲 Improved mobile responsiveness
* 🤖 AI-powered recommendations based on user behavior
* 🔔 Email/SMS alerts for price drops
* 📊 Historical price trends and purchase suggestions

---

## 📚 References

See the full list of academic and technical references in the [project report (PDF)](./PRICEWISE_17.pdf).

---

## 📄 License

This project was developed for academic purposes and is released for educational use only. For commercial use or redistribution, please seek permission from the project authors or institution.

> 💡 **Note**: This project was submitted as part of the B.Tech degree requirements under APJ Abdul Kalam Technological University.

