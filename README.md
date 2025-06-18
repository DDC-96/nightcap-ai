# 🍸 Nightcap

**Nightcap** is a sleek, modern basic cocktail web app designed to deliver a moody and elevated drink discovery experience. Made by a former Bartender, for Bartenders. Built with a fullstack architecture using **Next.js** as the frontend and **FastAPI** serving the API, it also allows users to generate AI-powered cocktail recommendations and explore handcrafted recipes leveraging an AI LLM.

---

### 🛠 Tech Stack

- **Frontend**: Next.js 14 (App Router), TailwindCSS, TypeScript
- **Backend**: FastAPI, Python 3.11
- **Containerization**: Docker (multi-stage builds), Docker networks
- **APIs**: AI cocktail generator endpoint, RESTful cocktail data
- **AWS**: AWS Infra for Kubernetes cluster using EKS
- **CI/CD**: GitHub Actions build out
- **Secrets**: Doppler integration for credential management

---

### 🔍 Features

- **Cocktail Generator** – Input your intrest, get a unique cocktail suggestion.
- **Recipe Pages** – Explore curated recipes with images and descriptions.
- **Dark Mode First** – Built with a moody aesthetic and toggle-ready theme support
- **Dockerized** – Fully containerized frontend and backend for reproducible builds.
- **Rewrite Proxy** – Frontend seamlessly proxies API calls to backend container.

---

### 🧪 Current State

- Frontend and backend are containerized and communicate via Docker network
- Image assets are handled via the Next.js `public/` directory
- API routes proxy to FastAPI for seamless local dev and container use
- Project structured with future AWS infrastructure support in mind
- Github Actions will be implemented next
- Replacing .env secrets handling with Doppler API credential handling or AWS KMS fetching.

---

### ⚠️ Notes

- For local Docker builds, make sure both containers share the same Docker network (e,g. docker run -d --name nightcap-frontend --network `networkname` -p 3000:3000 nightcap-frontend) do the same for the backend container that would be running on port `8000:8000`.
- Rewrites are configured to route `/api/*` to the backend service in production builds
- Build Github Actions workflow for Docker, integrate Doppler Secrets

---


