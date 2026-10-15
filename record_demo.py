import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

VIDEO_DIR = Path("demo_recordings")
VIDEO_DIR.mkdir(parents=True, exist_ok=True)

def record():
    print("Launching automated browser to record system demo...")
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

        print("1. Opening Dashboard...")
        page.goto("http://localhost:5173/dashboard")
        page.wait_for_timeout(3000)

        print("2. Opening Library...")
        page.goto("http://localhost:5173/library")
        page.wait_for_timeout(3500)

        print("3. Navigating to Chat...")
        page.goto("http://localhost:5173/chat")
        page.wait_for_timeout(2500)

        # Ask starter question
        print("Asking grounded deadlock question...")
        starter_btn = page.locator("button:has-text('What are the four necessary conditions for deadlock?')").first
        if starter_btn.is_visible():
            starter_btn.click()
        else:
            page.fill("input[placeholder*='Ask a question']", "What are the four necessary conditions for deadlock?")
            page.click("button[type='submit']")

        page.wait_for_timeout(4000)

        # Click citation pill to open source evidence panel
        citation_pill = page.locator("button[title*='View excerpt']").first
        if citation_pill.is_visible():
            citation_pill.click()
            page.wait_for_timeout(3000)

        # Ask out-of-domain question to show Insufficient Evidence
        print("Asking out-of-domain question (quantum computing)...")
        page.fill("input[placeholder*='Ask a question']", "Does our material cover quantum computing?")
        page.click("button[type='submit']")
        page.wait_for_timeout(4000)

        print("4. Opening Quiz...")
        page.goto("http://localhost:5173/quiz")
        page.wait_for_timeout(2500)

        # Start Quiz
        start_btn = page.locator("button:has-text('Start Assessment'), button:has-text('Start Quiz')").first
        if start_btn.is_visible():
            start_btn.click()
            page.wait_for_timeout(3000)

            # Answer Question 1
            opt1 = page.locator("button:has-text('Preemption')").first
            if opt1.is_visible():
                opt1.click()
                page.wait_for_timeout(1500)

            # Next Question
            next_btn = page.locator("button:has-text('Next Question')").first
            if next_btn.is_visible():
                next_btn.click()
                page.wait_for_timeout(1500)

                # Answer Question 2
                opt2 = page.locator("button:has-text('Circular wait')").first
                if opt2.is_visible():
                    opt2.click()
                    page.wait_for_timeout(1500)

                next_btn2 = page.locator("button:has-text('Next Question')").first
                if next_btn2.is_visible():
                    next_btn2.click()
                    page.wait_for_timeout(1500)

                    # Answer Question 3
                    opt3 = page.locator("button:has-text('Require a process')").first
                    if opt3.is_visible():
                        opt3.click()
                        page.wait_for_timeout(1500)

            # Submit Quiz
            submit_btn = page.locator("button:has-text('Submit Assessment'), button:has-text('Submit Quiz'), button:has-text('Finish')").first
            if submit_btn.is_visible():
                submit_btn.click()
                page.wait_for_timeout(4000)

        print("5. Back to Dashboard to see updated mastery...")
        page.goto("http://localhost:5173/dashboard")
        page.wait_for_timeout(4000)

        # Get video path before close
        video_obj = page.video
        context.close()
        browser.close()

        saved_path = video_obj.path()
        print(f"Recorded video saved to: {saved_path}")
        return saved_path

if __name__ == "__main__":
    record()
