# Mini Canvas Project

## Overview

This project is a full-stack application featuring:

- **Back-end:** Django REST Framework for API services.
- **Front-end:** Vue 3 with Vite for a modern, reactive UI, including Mapbox GL integration for interactive maps. It displays a set of mock "intelligence events" on an interactive map.

The repository is organized as follows:

- `mini-vue-canvas/` — Vue 3 front-end app (Vite-based)
- `pycanvas/` — Python back-end
- `.github/workflows/` — GitHub Actions for CI/CD and deployment

---

## Prerequisites

This project is built with the following technologies:

- **Python 3.13.3**
- **Node.js 22.16** and **npm**
- **Git**
- **Mapbox account** for map integration

---

## Setup & Run Guide

### 1. Clone the Repository

```bash
git clone https://github.com/NguyenDung98/mini-canvas
cd mini-canvas
```

---

### 2. Back-end: Django REST Framework API

#### a. Create and activate a Python virtual environment

```bash
python3 -m venv pyenv
source pyenv/bin/activate
```

#### b. Install dependencies

```bash
pip install django djangorestframework django-cors-headers
```

#### c. Apply migrations and run the server

```bash
python manage.py migrate
python manage.py runserver 8001
```

- The API will be available at `http://127.0.0.1:8001/`

---

### 3. Front-end: Vue 3 + Vite App

#### a. Install Node.js dependencies

```bash
cd mini-vue-canvas
npm install
```

#### b. Set up environment variables

If you use Mapbox, create a `.env` file and add your Mapbox token and API base URL:

```
VITE_MAPBOX_TOKEN=your_mapbox_token_here
VITE_API_BASE_URL=http://127.0.0.1:8001/
```

#### c. Run the development server

```bash
npm run dev
```

- The front-end will be available at `http://localhost:5173/` (default Vite port)

---

### 4. Build & Deploy

- To build the front-end for production:

    ```bash
    npm run build
    ```

- The output will be in `mini-vue-canvas/dist/`

- GitHub Actions workflow is set up for CI/CD and GitHub Pages deployment.

---

## Accessing the Live Demo

You can access the deployed project via GitHub Pages at:

**[https://nguyendung98.github.io/mini-canvas/](https://nguyendung98.github.io/mini-canvas/)**

> **Note:** The GitHub Pages deployment uses mock data for demonstration purposes. Real API integration is only available when running the project locally.

---

## Design Decisions

- The project uses standard, well-supported frameworks and tools:
  - Django REST Framework for the API (back-end)
  - Vue 3 with Vite for the front-end
  - Mapbox GL for interactive mapping
- The structure is kept simple: one directory for the back-end, one for the front-end, and clear separation of concerns.
- No special or complex design decisions were made.

---

## Challenges Faced

- The main challenge was the short timeframe: quickly learning and setting up Django, Vue.js (with Vite), and Mapbox, and making them work together smoothly.
- Integrating the front-end and back-end (CORS, API endpoints, environment variables) required careful attention.
- Ensuring the Mapbox integration worked seamlessly with Vue 3's reactivity model.
