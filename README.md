# Nightcap.

**Nightcap** is a sleek, modern basic cocktail web app designed to deliver a moody and elevated drink discovery experience. Made by a former Bartender, for Bartenders. Built with a fullstack architecture using **Next.js** as the frontend and **FastAPI** serving the API, it also allows users to generate AI-powered cocktail recommendations and explore handcrafted recipes.

---

![Nightcap Architecture](./assets/diagram.jpeg)

### Stack

- **Frontend**: Next.js 14 (App Router), TailwindCSS, TypeScript
- **Backend**: FastAPI, Python 3.11
- **Containerization**: Docker (multi-stage builds)
- **APIs**: AI cocktail generator endpoint, RESTful cocktail data
- **AWS**: Utilize Terraform to provision Kubernetes Infra. 
- **CI/CD**: GitHub Actions build out
- **Secrets**: Doppler integration for credential management

---

### Features

- **Cocktail Generator** – Input your intrest, get a unique cocktail suggestion.
- **Recipe Pages** – Explore curated recipes with images and descriptions.
- **Dark Mode First** – Built with a moody aesthetic and toggle-ready theme support
- **Dockerized** – Fully containerized frontend and backend for reproducible builds.
- **Rewrite Proxy** – Frontend seamlessly proxies API calls to backend container.

---

### Current State

- Frontend and backend are containerized and communicate via Docker network
- Image assets are handled via the Next.js `public/` directory
- API routes proxy to FastAPI for seamless local dev and container use
- Project structured with future AWS infrastructure support in mind
- Github Actions will be implemented next
- Replacing .env secrets handling with Doppler API credential handling or AWS KMS fetching.

---




