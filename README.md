# Festival Organizer (Python Matrix App)

An interactive terminal application built in Python to help groups of friends agree on a music festival schedule. The app takes raw user votes, prevents double-booking through algorithmic validation, and mathematically calculates a conflict-free concert itinerary.

# The Problem
Trying to get a group of friends to agree on a festival schedule usually results in chaotic group chats, overlapping plans, and double-booked time slots. This app turns a frustrating group decision into a structured, automated voting game.

# Technical Highlights
Behind the fun interface, this script demonstrates strong foundational programming logic:
* **Matrix Data Structures:** Utilizes a 3x3 matrix (2D list) to act as the festival grounds, storing the Time Slot, Band Name, and Vote Count for every stage to maintain spatial organization.
* **Input Validation & Crash-Proofing:** Engineered `while` loops and `try/except` blocks (Exception Handling). If a user types a letter instead of an integer, the app catches the error instead of crashing.
* **Algorithmic Collision Detection:** A custom `validate_vote` function cross-references a user's current choice against their historical inputs using coordinate mapping to strictly enforce a "one vote per time slot" rule.
* **Automated Tie-Breaking:** Loops through the final matrix to find maximum values and automatically flags exact 50/50 ties for human review.

# How to Run
1. Ensure you have Python 3 installed.
2. Run the script in your terminal: `python festival_organizer.py`
3. Follow the prompts to build your 3-stage festival schedule.
4. Tell the app how many friends are voting, and take turns casting your votes (IDs 1-9).
5. Let the algorithm calculate your final itinerary!

# Future Enhancements (V2)
* **Data Export:** Integrate the `pandas` library to export the final winning schedule into a `.csv` file.
* **Data Visualization:** Incorporate `matplotlib` to generate a bar chart showing the final vote distribution across all bands.
