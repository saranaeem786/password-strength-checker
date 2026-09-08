\# Password Strength \& Breach Checker



A Python tool that checks password strength and cross-references real data breach records — available both as a command-line script and a simple web app.



\## What it does



\- \*\*Strength check\*\* — scores a password based on length, uppercase/lowercase letters, numbers, and special characters, then rates it WEAK, MEDIUM, or STRONG

\- \*\*Breach check\*\* — securely checks the password against the HaveIBeenPwned database of real leaked passwords, without ever sending the actual password over the internet (only a partial hash is sent, using the "k-anonymity" method)



\## How to run it



Command line version:



&#x20;   python checker.py



Web version (with a simple interface):



&#x20;   python app.py



Then open http://127.0.0.1:5000 in your browser to check a password through a webpage instead of the terminal.



\## Example output



&#x20;   --- Checking: P@ssw0rd!2024 ---

&#x20;   Strength: STRONG

&#x20;   Breach check: FOUND in 1031 known data breaches!



\## Key takeaway



A password can look complex and still be unsafe if it's been leaked in a real breach — strength and safety aren't the same thing. This tool checks both.



\## Why I built this



Built to demonstrate practical application of secure coding principles (never transmitting a full password) and real-world threat data, as part of my transition into cyber security following my HNC Cyber Security qualification. Later extended with a Flask web interface to demonstrate how this logic could be integrated into a real website's signup process.



\## Future improvements



\- Check multiple passwords from a file at once

\- Add password generation suggestions

\- Deploy the web version online (currently runs locally only)

