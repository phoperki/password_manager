# Password Manager Mini-Project - Roadmap

## Project Overview
Build a command-line password manager that stores account credentials securely in a CSV file. This project applies everything you've learned (CSV, file I/O, error handling, menus) in a cybersecurity-focused context.

---

## Version Breakdown

### v0.1 - Basic Storage (Day 14 - 45-60 min)
**Core Goal:** Store and retrieve passwords

**Features:**
1. Store account credentials (account name, username, password)
2. View all stored passwords
3. Basic menu system
4. CSV file storage

**Functions Needed:**
- `add_password(account, username, password)` - Add new entry
- `view_passwords()` - Display all stored passwords
- `main()` - Menu loop

**Skills Practiced:**
- CSV DictWriter/DictReader (you already know this!)
- File creation and appending
- Basic menu system (you've done this!)

**Success Criteria:**
- Can add multiple accounts
- Can view all accounts in readable format
- Data persists between program runs

---

### v0.2 - Password Strength Integration (Day 15 - 30-45 min)
**Core Goal:** Add password strength checking when storing passwords

**New Features:**
1. Check password strength when adding (reuse your old password strength checker!)
2. Warn user if password is weak
3. Store strength rating with password (add new CSV column)

**Functions to Add/Modify:**
- `check_password_strength(password)` - Returns strength rating
- Modify `add_password()` to include strength check

**Skills Practiced:**
- Reusing/adapting old code (your password checker)
- Modifying existing functions
- Adding CSV columns

**Success Criteria:**
- Password strength is checked before storing
- Strength rating is saved and displayed
- User gets feedback on weak passwords

---

### v0.3 - Search and Retrieve (Day 16 - 30-45 min)
**Core Goal:** Find specific passwords without viewing all

**New Features:**
1. Search for password by account name
2. Display matching results
3. Handle "not found" cases

**Functions to Add:**
- `search_password(account_name)` - Find and display specific account
- Optional: `delete_password(account_name)` - Remove account

**Skills Practiced:**
- Searching through list of dictionaries
- String matching (exact vs. partial matches)
- User-friendly error messages

**Success Criteria:**
- Can search by account name
- Returns clear message if not found
- Optional: Can delete unwanted entries

---

### v0.4 - Password Generator (Day 17 - 45-60 min)
**Core Goal:** Generate strong random passwords

**New Features:**
1. Option to generate password instead of manually entering
2. Configurable length and character types
3. Automatically use strong generated password

**Functions to Add:**
- `generate_password(length, include_special, include_numbers)` - Creates random password
- Modify menu to offer generation option

**Skills Practiced:**
- Random module (`random.choice()`, `random.sample()`)
- String concatenation for character pools
- Optional parameters with defaults

**Success Criteria:**
- Can generate passwords of custom length
- Generated passwords are strong (checked by v0.2 function)
- User can choose to generate or enter manually

---

### v0.5+ - Advanced Features (Optional Extensions)

**Possible Additions:**
1. **Master Password Protection**
   - Require password to access program
   - Store hashed master password
   
2. **Password Categories**
   - Tag passwords (work, personal, social media, etc.)
   - Filter by category
   
3. **Password Expiration Tracking**
   - Store date password was created
   - Warn when passwords are old (90+ days)
   
4. **Encryption Hints** (not full encryption - that's advanced)
   - Simple Caesar cipher on passwords
   - Basic obfuscation (not secure, but educational)

5. **Export/Import**
   - Backup passwords to separate file
   - Import from backup

6. **Password Update**
   - Change password for existing account
   - Keep password history

---

## Recommended Approach

### For Each Version:
1. **Read requirements** - Understand what you're building
2. **Plan functions** - What do you need to write?
3. **Build minimum version** - Get it working first
4. **Test thoroughly** - Try to break it
5. **Add polish** - Error handling, user feedback
6. **Celebrate** - Working code deserves recognition!

### Time Estimates:
- v0.1: 45-60 min (most is setup, you know CSV already)
- v0.2: 30-45 min (adding to existing code)
- v0.3: 30-45 min (similar patterns to v0.2)
- v0.4: 45-60 min (new concept: random generation)

**Total project time (v0.1-v0.4): ~3-4 hours across 4 days**

---

## Coaching Style for This Project

### What I'll Do:
✅ Provide requirements for each version  
✅ Break down what functions you'll need  
✅ Give hints when you're stuck (concept-level, not code)  
✅ Point you to documentation/resources  
✅ Help debug by asking questions about your code  
✅ Celebrate your wins and working code  
✅ Suggest optional improvements after it works  

### What I Won't Do:
❌ Give you complete solutions upfront  
❌ Write your functions for you  
❌ Fix your bugs directly (I'll guide you to fix them)  
❌ Hand-hold through step-by-step instructions  

### When You're Stuck:
1. Show me your code and describe what's not working
2. Tell me what you've tried
3. I'll ask clarifying questions
4. I'll give hints that point you toward the solution
5. You'll fix it and learn the concept

---

## Getting Started (Day 14)

**When you're ready to start v0.1, tell me:**
1. "I'm ready to start v0.1 of the password manager"
2. I'll give you the detailed requirements
3. You build it
4. We iterate until it works
5. You move to v0.2 when ready

**You can also:**
- Ask questions about any version before starting
- Skip versions (e.g., go straight to v0.3 if you want)
- Combine versions if you're feeling ambitious
- Stop at any version (v0.1 alone is a complete project!)

---

## Why This Project is Perfect for You

✅ **Applies skills you already have** - CSV, menus, file I/O  
✅ **Cybersecurity-focused** - Aligns with your background  
✅ **Incremental versions** - Build in small, testable chunks  
✅ **Practical and useful** - You might actually use this!  
✅ **Extends naturally** - Always more features to add  
✅ **Portfolio-worthy** - Shows real problem-solving  

---

## Notes

- Take your Day 13 break guilt-free! The streak isn't about perfection, it's about consistency.
- You can start whenever you're ready - Day 14, 15, or whenever feels right
- This project will take multiple days - that's normal and expected
- Ask for hints liberally - struggling is good, but spinning wheels isn't
- You're not racing - build at your pace

**See you on Day 14!** 🔥

---


