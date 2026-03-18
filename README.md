# Drug Discovery Ai

AI drug discovery — molecular generation and property prediction

## Features

- Api
Graph Builder
Models - Generator
Models - Gnn
Models - Property Predictor
Molecule Parser
Visualizer

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Key Dependencies:** pydantic,fastapi,uvicorn,anthropic,openai,numpy
- **Containerization:** Docker + Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

### Installation

```bash
git clone https://github.com/MukundaKatta/drug-discovery-ai.git
cd drug-discovery-ai
pip install -r requirements.txt
```

### Running

```bash
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up
```

## Project Structure

```
drug-discovery-ai/
├── src/           # Source code
├── tests/         # Test suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## License

MIT
