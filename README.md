# GroupF Django Project Workflow

## Setting Up Virtual Environment

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   ```
2. **Navigate to Project Directory:**
3. **Create Virtual Environment:**

```bash
virtualenv <name of environment>
```

4. **Activate Virtual Environment:**

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  env\Scripts\activate
  ```

5. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

## Running the Project

1. **Navigate to Project Directory (if not already there).**

2. **Activate Virtual Environment (if not already activated).**

3. **Run Django Server:**

```bash
python manage.py runserver
```

4. **Access the Project:**

- Open a web browser and go to `http://localhost:8000`.

## Collaborating with Git

### Pushing Changes

1. **Add Changes to Staging:**

```bash
git add .
```

2. **Commit Changes:**

```bash
git commit -m "<your message here>"
```

3. **Push Changes to Remote Repository:**

```bash
git push
```

### Pulling Changes

1. **Always ensure your branch is up to date with main:**

```bash
git pull origin main
```

### Checking Out to a Branch

1. **Switch to Your working Branch:**

```bash
git checkout <branch_name>
```

2. **Pull all remote branches:**

```bash
git pull
```

3. **List Available Branches:**

```bash
git branch
```

3. **Delete a Branch (if needed):**

4. **Push Changes to Remote Repository (if you created a new branch):**

```bash
git push`
```
