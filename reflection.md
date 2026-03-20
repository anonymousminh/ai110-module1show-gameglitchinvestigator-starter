# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  It showed the game title "Game Glitch Investigator". On the left, we got Settings with Difficulty of Easy, Normal, Hard and it is set as Normal in default. There is a range of guesses and the attempts also on the left. There is a placeholder for enter the guess. There are buttons for Submit Guess, New Game and Show hint
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
- Bug 1: When we submit a guess number that is higher than the secret number, the hint shows that to go higher instead of lower
- Bug 2: When choosing the Easy mode, the range is set from 1 to 20 but the secret number is sometime not in the range

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
- I used Claude on this project
- An example that AI suggestion is correct is in the Bug 1, the fix is:
Bug 1: Wrong hint direction (app.py:38-40)
The messages are swapped. When guess > secret (guess is too high), it should say "Go LOWER", not "Go HIGHER".

Fix in check_guess:

if guess > secret:
    return "Too High", "📉 Go LOWER!"   # was: "📈 Go HIGHER!"
else:
    return "Too Low", "📈 Go HIGHER!"   # was: "📉 Go LOWER!"
- Right now I didn't see anything misleading from Claude yet and Its answers seem right on point

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
- The bug is fixed where it match with the logic of the game and it also passed any test that related with it
- One test I use pytest is the get_range_for_difficulty("Hard") returns (1, 50), but Normal returns (1, 100). Hard should have a larger range (harder to guess), not a smaller one. It check the logic of my code and it 
- I used Claude to fix the logic breaks and it actually point out which line the logic breaks and also showing the diff when it makes the changes. It also aware of other logic break that has the same context

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---
Reruns are how Streamlit interacts with user input (by running your whole script again), and session state is how you prevent things from being forgotten after a rerun occurs.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
+ I would do the testing after implementing the logic so I can be assured of the application is working and follow the right logic
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
+ I would love to ask it to explain to me about my codebase so I can leverage it when add some new features or change logics 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
+ AI code generated is getting better as it has more context and can solve easy problem for us. It can be able to explain about the issue and help us implement it faster and better. Right now, I feel like I have a partner that can give me suggestion and guide me to code better.
