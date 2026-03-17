### How to Run the Project

Clone the repository and navigate to it in the terminal:

```bash
git clone https://github.com/yandex-praktikum/kittygram.git
```

```bash
cd kittygram
```

Create and activate a virtual environment:

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

Install dependencies from `requirements.txt`:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python3 manage.py migrate
```

Start the development server:

```bash
python3 manage.py runserver
```
