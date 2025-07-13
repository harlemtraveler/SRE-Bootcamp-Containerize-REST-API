# Containerize the REST API

This document describes the goals, requirements, and step-by-step implementation for containerizing a REST API using Docker.

---

## Goals

- Learn how to Dockerize a REST API application
- Implement a multi-stage Dockerfile
- Apply Dockerfile best practices for security and performance
- Run the API as a container using injected environment variables
- Ensure images are properly version-tagged using semantic versioning
- Keep Docker image size minimal

---

## Functional Requirements

The following must be implemented:

1. The REST API must be runnable via a Docker container
2. A **multi-stage Dockerfile** must be created:
   - Build dependencies in one stage
   - Run the API in a minimal base image
3. Docker image should support **runtime config via environment variables**
4. All sensitive config (e.g., DB URL) should be externalized
5. Image should be tagged using semantic versioning (e.g., `student-api:0.1.0`)
6. Avoid using the `latest` tag
7. Use `.dockerignore` and other techniques to reduce image size
8. Update the Makefile with Docker build and run commands
9. Update the README with instructions to build and run the image

---

## Project Structure

```plaintext
student-api/
├── Dockerfile
├── .dockerignore
├── .env
├── Makefile
├── run.py
├── requirements.txt
├── app/
│   ├── models.py
│   ├── db.py
│   └── routes/
```

---

## Running the Project with Docker

1. Build the Docker Image
```
make docker-build
```

This command builds the image using the multi-stage `Dockerfile` and tags it as `student-api:0.1.0`.



Make sure you have a `.env` file with:
```
DATABASE_URL=sqlite:///students.db
```
Then run:
```
make docker-run
```

Your API should be available at:
- http://localhost:5000/api/v1/students
- http://localhost:5000/healthcheck


3. Open a Shell in the Container (Optional)
```
make docker-shell
```

Useful for debugging or running manual commands inside the container.


---


## Best Practices Summary

| Practice                          | Implemented                         |
| --------------------------------- | ----------------------------------- |
| Multi-stage Dockerfile            | ✅                                   |
| Environment variables from `.env` | ✅                                   |
| Semantic version tagging for images         | ✅ (`0.1.0`)                         |
| Avoid use of `latest` tag         | ✅                                   |
| Minimized image size              | ✅ (uses `slim` and `.dockerignore`) |
| External config                   | ✅ via `config.py` and `.env`        |


---


## Optional Improvements
- Add `gunicorn` in production image
- Use a non-root user inside container
- Container healthcheck for orchestration (e.g., Docker Compose, Kubernetes)
- Publish image to Docker Hub or AWS ECR


---


## Completion Checklist

| Task                               | Status |
| ---------------------------------- | ------ |
| Dockerfile with multi-stage build  | ✅      |
| Inject config via env vars         | ✅      |
| Make targets for build/run         | ✅      |
| Small image size                   | ✅      |
| Tagged with version (not `latest`) | ✅      |
| README updated                     | ✅      |


---


## License

This project is licensed under the MIT License.

---

## Author

Timothy Keaveny - [@harlemtraveler](https://github.com/harlemtraveler)


---


## Citation & Reference

[One2N - SRE Bootcamp - Containerize REST API](https://one2n.io/sre-bootcamp/sre-bootcamp-exercises/2-containerise-rest-api)