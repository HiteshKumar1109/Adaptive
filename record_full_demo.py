import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

VIDEO_DIR = Path("demo_recordings_full")
VIDEO_DIR.mkdir(parents=True, exist_ok=True)

SAMPLE_DOC = Path(__file__).resolve().parent / "sample_network_notes.docx"

def smooth_scroll(page, y_delta=300, steps=10, step_delay=50):
    for _ in range(steps):
        page.evaluate(f"window.scrollBy(0, {y_delta // steps});")
        page.wait_for_timeout(step_delay)

def type_text(page, selector, text, delay=45):
    page.click(selector)
    page.fill(selector, "")
    for char in text:
        page.type(selector, char, delay=delay)
    page.wait_for_timeout(400)

def record():
    print("========================================================")
    print("  Starting 4.5 - 5 Minute Full Demo Video Recording...")
    print("========================================================")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            headless=True
        )
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            record_video_dir=str(VIDEO_DIR),
            record_video_size={"width": 1280, "height": 800}
        )
        page = context.new_page()

        # ==========================================
        # SCENE 1: DASHBOARD OVERVIEW (approx 40 sec)
        # ==========================================
        print("[Scene 1/5] Dashboard Overview (40s)...")
        page.goto("http://localhost:5173/dashboard")
        page.wait_for_timeout(6000)

        smooth_scroll(page, 200, 8, 80)
        page.wait_for_timeout(5000)

        # Hover over topic cards
        topic_cards = page.locator("div:has-text('Deadlock conditions')").first
        if topic_cards.is_visible():
            topic_cards.hover()
        page.wait_for_timeout(5000)

        smooth_scroll(page, 250, 8, 80)
        page.wait_for_timeout(6000)

        rec_card = page.locator("h2:has-text('Adaptive Recommendation')").first
        if rec_card.is_visible():
            rec_card.hover()
        page.wait_for_timeout(8000)

        smooth_scroll(page, -450, 10, 60)
        page.wait_for_timeout(5000)

        # ==========================================
        # SCENE 2: LIBRARY & DOCUMENT INGESTION (approx 60 sec)
        # ==========================================
        print("[Scene 2/5] Course Materials Library & Ingestion (60s)...")
        page.click("a:has-text('Library')")
        page.wait_for_timeout(6000)

        smooth_scroll(page, 250, 8, 80)
        page.wait_for_timeout(6000)

        # Show existing indexed files
        doc_card = page.locator("p:has-text('OS Unit 3 - Deadlocks.pdf')").first
        if doc_card.is_visible():
            doc_card.hover()
        page.wait_for_timeout(6000)

        smooth_scroll(page, -250, 8, 60)
        page.wait_for_timeout(4000)

        # Upload sample_network_notes.docx
        print("Uploading sample course document...")
        if SAMPLE_DOC.exists():
            file_input = page.locator("input[type='file']")
            file_input.set_input_files(str(SAMPLE_DOC))
            page.wait_for_timeout(4000)

            # Observe background ingestion banner and polling
            smooth_scroll(page, 200, 6, 80)
            page.wait_for_timeout(10000)

            # Click refresh status button
            refresh_btn = page.locator("button:has-text('Refresh status')").first
            if refresh_btn.is_visible():
                refresh_btn.click()
            page.wait_for_timeout(8000)

        # Click 'Ask about this' on Deadlocks document
        ask_btn = page.locator("a:has-text('Ask about this')").first
        if ask_btn.is_visible():
            ask_btn.click()
        else:
            page.click("a:has-text('AI Tutor')")
        page.wait_for_timeout(6000)

        # ==========================================
        # SCENE 3: RAG GROUNDED TUTOR (approx 90 sec)
        # ==========================================
        print("[Scene 3/5] RAG Grounded Tutor & Evidence Sufficiency (90s)...")
        # Submit the prefilled document summary question if present
        submit_btn = page.locator("button[type='submit']").first
        if submit_btn.is_enabled():
            submit_btn.click()
            page.wait_for_timeout(8000)

        # Question 1: Conditions for deadlock
        print("Submitting question 1: Four necessary conditions...")
        type_text(page, "input[placeholder*='Ask a question']", "What are the four necessary conditions for deadlock?")
        page.wait_for_timeout(1000)
        page.click("button[type='submit']")
        page.wait_for_timeout(8000)

        # Inspect citations
        citation_btn = page.locator("button[title*='View excerpt']").first
        if citation_btn.is_visible():
            citation_btn.click()
            page.wait_for_timeout(6000)
            # Scroll inside sidebar if present
            sidebar = page.locator("aside").first
            if sidebar.is_visible():
                sidebar.hover()
                page.wait_for_timeout(6000)
            # Close sidebar
            close_btn = page.locator("button[aria-label='Close source panel']").first
            if close_btn.is_visible():
                close_btn.click()
                page.wait_for_timeout(2000)

        # Question 2: Circular wait elimination
        print("Submitting question 2: Circular wait...")
        type_text(page, "input[placeholder*='Ask a question']", "How can the circular wait condition be practically eliminated?")
        page.wait_for_timeout(1000)
        page.click("button[type='submit']")
        page.wait_for_timeout(8000)

        smooth_scroll(page, 200, 6, 80)
        page.wait_for_timeout(6000)

        # Question 3: Anti-hallucination check (Quantum Computing)
        print("Submitting question 3: Out-of-domain quantum computing...")
        type_text(page, "input[placeholder*='Ask a question']", "Does our material cover quantum computing and qubits?")
        page.wait_for_timeout(1000)
        page.click("button[type='submit']")
        page.wait_for_timeout(6000)

        smooth_scroll(page, 250, 6, 80)
        # Highlight amber Insufficient Evidence banner
        amber_banner = page.locator("div:has-text('Insufficient Evidence Grounding')").first
        if amber_banner.is_visible():
            amber_banner.hover()
        page.wait_for_timeout(10000)

        # ==========================================
        # SCENE 4: ADAPTIVE QUIZ & ASSESSMENT (approx 65 sec)
        # ==========================================
        print("[Scene 4/5] Adaptive Assessment Engine (65s)...")
        page.click("a:has-text('Quiz')")
        page.wait_for_timeout(6000)

        # Highlight topic input
        topic_input = page.locator("input[placeholder*='Deadlock conditions']").first
        if topic_input.is_visible():
            topic_input.hover()
            page.wait_for_timeout(4000)

        # Click Start Assessment
        start_btn = page.locator("button:has-text('Start Assessment'), button:has-text('Start Quiz')").first
        if start_btn.is_visible():
            start_btn.click()
            page.wait_for_timeout(6000)

            # Question 1
            print("Answering Question 1...")
            page.wait_for_timeout(4000)
            opt1 = page.locator("button:has-text('Preemption')").first
            if opt1.is_visible():
                opt1.click()
                page.wait_for_timeout(4000)

            next_btn = page.locator("button:has-text('Next Question')").first
            if next_btn.is_visible():
                next_btn.click()
                page.wait_for_timeout(5000)

                # Question 2
                print("Answering Question 2...")
                opt2 = page.locator("button:has-text('Circular wait')").first
                if opt2.is_visible():
                    opt2.click()
                    page.wait_for_timeout(4000)

                next_btn2 = page.locator("button:has-text('Next Question')").first
                if next_btn2.is_visible():
                    next_btn2.click()
                    page.wait_for_timeout(5000)

                    # Question 3
                    print("Answering Question 3...")
                    opt3 = page.locator("button:has-text('Require a process')").first
                    if opt3.is_visible():
                        opt3.click()
                        page.wait_for_timeout(4000)

            # Submit assessment
            print("Submitting assessment...")
            finish_btn = page.locator("button:has-text('Submit Assessment'), button:has-text('Submit Quiz'), button:has-text('Finish')").first
            if finish_btn.is_visible():
                finish_btn.click()
                page.wait_for_timeout(8000)

                # Review feedback score
                smooth_scroll(page, 200, 6, 80)
                page.wait_for_timeout(8000)
                smooth_scroll(page, 250, 6, 80)
                page.wait_for_timeout(8000)

        # ==========================================
        # SCENE 5: UPDATED MASTERY & API DOCS (approx 45 sec)
        # ==========================================
        print("[Scene 5/5] Learner Model & Interactive API Docs (45s)...")
        page.click("a:has-text('Dashboard')")
        page.wait_for_timeout(6000)

        smooth_scroll(page, 200, 6, 80)
        page.wait_for_timeout(6000)

        # Inspect updated mastery bar
        updated_card = page.locator("div:has-text('Deadlock conditions')").first
        if updated_card.is_visible():
            updated_card.hover()
        page.wait_for_timeout(6000)

        smooth_scroll(page, 200, 6, 80)
        page.wait_for_timeout(6000)

        # Open FastAPI Swagger Docs
        print("Opening FastAPI Swagger Documentation...")
        page.goto("http://localhost:8000/docs")
        page.wait_for_timeout(6000)

        smooth_scroll(page, 300, 8, 80)
        page.wait_for_timeout(6000)
        smooth_scroll(page, 400, 8, 80)
        page.wait_for_timeout(6000)

        # Clean finish
        print("Finishing recording...")
        page.wait_for_timeout(3000)

        video_obj = page.video
        context.close()
        browser.close()

        saved_path = video_obj.path()
        print(f"Full Demo Video saved at: {saved_path}")
        return saved_path

if __name__ == "__main__":
    record()
