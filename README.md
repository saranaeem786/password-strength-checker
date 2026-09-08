\# Password Strength \& Breach Checker



A Python tool that checks password strength and cross-references real data breach records.



\## What it does



\- \*\*Strength check\*\* — scores a password based on length, uppercase/lowercase letters, numbers, and special characters, then rates it WEAK, MEDIUM, or STRONG

\- \*\*Breach check\*\* — securely checks the password against the HaveIBeenPwned database of real leaked passwords, without ever sending the actual password over the internet (only a partial hash is sent, using the "k-anonymity" method)



\## How to run it



python checker.py



This tests three example passwords and prints the strength rating, improvement suggestions, and breach status for each.



\## Example output



\--- Checking: P@ssw0rd!2024 ---

VERDICT: STRONG

Breach check: FOUND in 1031 known data breaches!



\## Key takeaway



A password can look complex and still be unsafe if it's been leaked in a real breach — strength and safety aren't the same thing. This tool checks both.



\## Why I built this



Built to demonstrate practical application of secure coding principles (never transmitting a full password) and real-world threat data, as part of my transition into cyber security following my HNC Cyber Security qualification.



\## Future improvements



\- Add a simple web interface

\- Check multiple passwords from a file at once

\- Add password generation suggestions

