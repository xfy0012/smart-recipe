### Smart Recipe App

An AI-powered recipe recommendation web app that helps users find meals they can cook with ingredients they already have.

This project idea is inspired by the MLH tutorial:  
[Smart Recipe Application with Django and MongoDB](https://news.mlh.io/smart-recipe-application-tutorial-with-django-and-mongodb-05-07-2025?utm_source=mlh&utm_medium=referral&utm_content=mlh.link%2Fghwos525-mongodb-blogpost)


cooker recipes: https://eightportions.com/datasets/Recipes/

### Prerequisites
* IDE: Visual Studio Code
* Python 3.10 or later 
* Docker for containerization
* Atlas CLI for MongoDB integration
* A local Atlas deployment
* Voyage API key for embeddings
* Anthropic API key for the LLM
* Jupyter Notebook for data clean

### Getting Started



<!-- ROADMAP -->
## Roadmap

### Phase 1: Environment Setup 
- [X] Project structure setup
  - [X] `/backend` folder for Django API
  - [X] Virtual environment initialized
  - [X] Python dependencies installed
- [X] Git & GitHub setup
  - [X] `.gitignore` and `LICENSE`
  - [X] Connected local repo to GitHub
  - [X] Initial `README.md` with project intro
- [X] MongoDB Atlas integration
  - [X] Create database and collection
  - [X] Configure connection string in `.env`
  - [ ] Enable IP whitelist and DB user access

---
### Phase 2: Data preparation 
- [X] Download and inspect the `recipes_raw.json` dataset
- [X] Create a Jupyter Notebook `data_cleaning.ipynb` to prepare data for API upload
  - [X] Load and normalize basic fields: `title`, `ingredients`, and `instructions`
  - [X] Clean invalid or incomplete records (e.g. empty ingredients or missing title)
  - [ ] Prepare the `embedding_ingredients` string
  - [ ] Preview cleaned recipe objects
- [ ] Submit cleaned recipes to backend API (`POST /api/recipes/`)
  - [ ] Backend will generate embeddings using Voyage AI
  - [ ] Backend will insert the full recipe (including embedding) into MongoDB
- [ ] Optional: Write a bulk upload script that reads JSON and POSTs to the API


### Phase 3: Backend API Development 
- [ ] Django REST Framework setup
  - [ ] Install `djangorestframework`
  - [ ] Add REST routing for `recipes/search`
- [ ] Core API logic
  - [ ] Implement `POST /api/recipes/search`
  - [ ] Convert ingredients to embedding using Voyage AI
  - [ ] Match similar recipes using cosine similarity
- [ ] Claude LLM integration
  - [ ] Call Claude API with matched recipe context
  - [ ] Return Claude suggestion in response JSON
- [ ] Dataset import utility
  - [ ] Parse and clean external recipe JSON
  - [ ] Generate embeddings and insert into MongoDB

---

### Phase 4: Frontend UI 
- [ ] Frontend project initialization (React + Vite)
- [ ] Build ingredient input form
- [ ] Display API results (recipes + Claude suggestion)
- [ ] UI/UX styling with Tailwind CSS

---

### Phase 5: Deployment & DevOps
- [ ] Dockerize Django backend
  - [ ] Create `Dockerfile` and production-ready image
- [ ] `docker-compose.yml` for full stack (backend + frontend)
- [ ] Deploy to Render, Railway, or AWS
- [ ] `.env.example` and deployment instructions

---

### Phase 6: Testing & Monitoring 
- [ ] Add request/response error handling
- [ ] Log Claude responses and similarity scores
- [ ] Create basic automated tests (pytest or DRF test client)
- [ ] Optional: Add Prometheus & Grafana integration

---

### Bonus Ideas (Stretch Goals)
- [ ] Add user authentication and allow saving favorite recipes
- [ ] Use computer vision to extract ingredients from fridge photos
- [ ] Support multiple languages using Claude LLM prompt customization

<!-- LICENSE -->
## License

Distributed under the project_license. See [LICENSE](./LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


