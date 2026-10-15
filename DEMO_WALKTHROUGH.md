# Adaptive Learning AI — Demo Video Walkthrough Guide

Use this step-by-step walkthrough script to record your demo video for submission. Both the backend and frontend are live and connected.

---

## 🚀 Quick Launch (If restarting the system)
- **One-Click Start**: Double click `start_all.bat` (or run `start_backend.bat` and `start_frontend.bat`).
- **Frontend URL**: [http://localhost:5173](http://localhost:5173)
- **Backend API & Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🎬 Video Recording Script (Step-by-Step)

### Scene 1: Introduction & Architecture Overview (0:00 - 0:45)
- **What to say**: 
  > "Hello! Today I am presenting Adaptive Learning AI — an end-to-end intelligent tutoring system combining RAG-grounded knowledge retrieval, source-verified citations, adaptive assessments, and a dynamic learner model that personalizes the student's learning journey."
- **What to show**:
  - Open the homepage ([http://localhost:5173/dashboard](http://localhost:5173/dashboard)).
  - Briefly mention the full stack: React + TypeScript + Tailwind frontend communicating with a Python + FastAPI backend, vector search engine, and rule-based learner model.

---

### Scene 2: Course Materials Library & Document Ingestion (0:45 - 1:45)
- **What to do**:
  1. Click **Library** in the top navigation ([http://localhost:5173/library](http://localhost:5173/library)).
  2. Point out the pre-indexed files: `OS Unit 3 - Deadlocks.pdf` (Ready for RAG) and `DBMS Normalization.pptx`.
  3. Upload any PDF or DOCX file using the drag-and-drop zone or file picker.
  4. Show the status change from **Indexing & embedding** to **Ready for RAG** (Workflow A: Document Ingestion, section chunking, and metadata tagging).
- **What to say**:
  > "In the Library, students upload PDFs, PPTX slides, Word documents, or lecture media. The backend ingests the files, preserves page and slide numbers, normalizes text into semantic chunks, and creates vector embeddings stored for high-precision retrieval."

---

### Scene 3: RAG Grounded Tutor with Citations & Sufficiency Check (1:45 - 3:00)
- **What to do**:
  1. Navigate to **Chat** ([http://localhost:5173/chat](http://localhost:5173/chat)).
  2. Click on the suggested prompt: **"What are the four necessary conditions for deadlock?"** or type it in.
  3. Watch the AI tutor return the exact grounded explanation:
     - Notice the **Retrieved Sources** pills at the bottom showing `OS Unit 3 - Deadlocks.pdf · p. 12` and `p. 16`.
     - Click on one of the citation buttons to open the **Source Evidence sidebar** on the right, showing the verified excerpt and exact page metadata.
  4. **Crucial Architecture Showcase — Insufficient Evidence**:
     - Click or type: **"Does our material cover quantum computing?"**
     - Show the **amber Insufficient Evidence banner**:
       > *"Insufficient Evidence Grounding: Your indexed course documents do not contain enough verified evidence to answer this question without hallucinating."*
- **What to say**:
  > "Unlike standard chatbots that hallucinate, our RAG pipeline strictly verifies evidence sufficiency. If sufficient evidence exists, it provides exact citations with verifiable page numbers. If evidence is lacking, the system transparently refuses to answer rather than fabricating false information."

---

### Scene 4: Adaptive Assessment & Quiz Engine (3:00 - 4:15)
- **What to do**:
  1. Navigate to **Quiz** ([http://localhost:5173/quiz](http://localhost:5173/quiz)).
  2. Select **"Deadlock conditions"** and click **Start Quiz**.
  3. Show the generated questions with difficulty badges (`easy`, `medium`, `hard`).
  4. Answer the questions:
     - Select: *"Preemption"* for Question 1.
     - Select: *"Circular wait"* for Question 2.
     - Select: *"Require a process to request all required resources at once before execution"* for Question 3.
  5. Click **Submit Quiz**.
  6. View the detailed question-by-question feedback with explanations and score breakdown.
- **What to say**:
  > "The Quiz service generates multiple-choice questions grounded in the indexed lecture chunks with concept tags and difficulty ratings. When submitted, the backend evaluates the answers, stores the attempt, and updates the learner model."

---

### Scene 5: Learner Model & Personalized Recommendations (4:15 - 5:15)
- **What to do**:
  1. Navigate to **Dashboard** ([http://localhost:5173/dashboard](http://localhost:5173/dashboard)).
  2. Show how the mastery progress bars updated in real time (e.g. Deadlock conditions increased to >90%).
  3. Highlight the **Adaptive Recommendation Card**:
     - Explain the pedagogy rules:
       - **Low Mastery (< 40%)** $\rightarrow$ **Reteach**: Recommends reviewing foundational gaps with the AI tutor.
       - **Developing (40% - 69%)** $\rightarrow$ **Practice**: Recommends guided practice quizzes.
       - **High Mastery ($\ge$ 70%)** $\rightarrow$ **Advance / Revise**: Recommends advancing to the next unit or spaced revision.
  4. Click the action button on the recommendation card to show smooth routing.
- **What to say**:
  > "The feedback loop is what makes this truly adaptive: the learner model recalculates topic mastery using attempt history, difficulty weighting, and recency decay. The recommendation engine then prescribes the exact next activity the student needs to master their course."

---

### Scene 6: Deployment & Backend API Verification (5:15 - 6:00)
- **What to do**:
  1. Switch to the browser tab with [http://localhost:8000/docs](http://localhost:8000/docs).
  2. Briefly show the OpenAPI/Swagger documentation displaying the clean REST endpoints:
     - `GET /documents`, `POST /documents`
     - `POST /chat`
     - `POST /quiz/generate`, `POST /quiz/submit`
     - `GET /progress`
  3. Show the `docker-compose.yml` file demonstrating containerized deployment for production with FastAPI, Postgres + pgvector, Redis, and React.
- **What to say**:
  > "Everything conforms strictly to the system architecture contract and is ready for containerized Docker deployment or cloud hosting. Thank you!"
