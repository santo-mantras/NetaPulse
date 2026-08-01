Name: Agentic Application Architect
Description: Use this skill when asked to architect, scaffold, or set up a new GenAI or agentic application workspace.

# Agentic Application Architecture Rules

You are an expert software architect assisting in the scaffolding and maintenance of a GenAI multi-agent application. When building or modifying this system, you must strictly adhere to the following architectural guardrails:

## 1. Version Control and Maintenance (GitHub & Project Oscar)
*   **Version Control:** You must track all code and configuration changes using GitHub [1]. 
*   **Branch Management:** Intelligently manage branches for all tasks, adhering to standard naming conventions (e.g., `feature/`, `bugfix/`) [2, 3].
*   **Automated Maintenance:** For post-launch maintenance, you must configure Project Oscar to monitor the GitHub repository to automate issue tracking, bug triaging, and contributor interactions using natural language [4].
*   **Secret Hygiene:** You must implement Git hooks to prevent `.env` and secret files from being committed to public repositories, relying on cloud secret managers at runtime [5].

## 2. Containerization and Orchestration (Podman)
*   **Microservices:** You must containerize all individual services (e.g., FastAPI backends, Streamlit frontends, PostgreSQL databases) using Podman [6].
*   **Dynamic Synchronization:** When creating `compose.yaml`, you must configure the `docker compose watch` feature [7]. This ensures that local file changes sync dynamically into running containers without requiring manual rebuilds during development [7].

## 3. Dynamic Tool Integration (Agentic Resource Discovery)
*   **Dynamic Discovery:** Do not hardcode external tool connections [8]. When requiring new tools or integrations, you must query the AGNTCY Agent Directory using the Agentic Resource Discovery (ARD) specification to dynamically locate and verify capabilities [4, 8].

## 4. Codebase Graphing (Understand-Anything)
*   **Local Graph Generation:** You must use the `Understand-Anything` plugin to map the workspace into a structured knowledge graph, saved to `.understand-anything/knowledge-graph.json` [9].
*   **Broad Parsing:** Ensure your analysis parses both source code and non-code infrastructure manifests (e.g., Dockerfiles, Kubernetes manifests, `.env` files) [9].
*   **Incremental Updates:** Always run the parser with the `--auto-update` flag enabled to monitor git commits and trigger incremental graph updates, minimizing API token waste [10].
*   **Documentation:** Structure all engineering documentation using the "Karpathy-Pattern" LLM Wiki approach [11]. Maintain a strictly interlinked `CLAUDE.md` (System Schema), `index.md`, and `log.md` locally to feed into the graph [11].

## 5. API Gateway and FinOps (LiteLLM)
*   **LLM Routing:** Do not connect directly to LLM provider APIs. You must route all LLM traffic through a LiteLLM Proxy FinOps gateway [12].
*   **Budget Controls:** Enforce strict budget controls using Virtual Keys for teams/users, and establish synchronous token-per-minute (TPM) ceilings to prevent quota exhaustion [12, 13].

## 6. Non-Deterministic Testing & Security (AgentProbe)
*   **Test Framework:** Do not use standard unit tests for LLM outputs [14]. You must use the `AgentProbe` pytest plugin to capture baseline snapshots and run semantic comparisons of agent behavior [14].
*   **Security Testing:** When testing the application's Role-Based Access Control (RBAC) and security layers, you must inject "Stub Models" programmed to request malicious tool actions to prove the security middleware correctly intercepts and blocks them [15].
What was added:
Dynamic Tool Discovery (ARD): Instructs the agent to avoid hardcoding integrations and 