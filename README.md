# ChronicleQuest

A competitive AI-judged survival story game built on GenLayer Intelligent Contracts.

Players respond to crisis scenarios and get scored 0-100 on creativity by an on-chain AI. Scores are stored permanently on the blockchain in a live leaderboard. No human judges. No cheating.

**Live: https://chronicle-quest.netlify.app

---

## How It Works

1. Read the survival scenario
2. Write your creative response (min 30 characters)
3. Submit via GenLayer Studio
4. The AI scores you 0-100 based on originality, depth, and tension
5. Your score is saved on-chain and appears on the leaderboard

---

## Contract

Built with Python on GenLayer a blockchain that lets smart contracts call AI models and make decisions on-chain.

Contract address: 0x3068340C67dEAA29105923aCE20047ab070DF85e

Network: GenLayer Studio

### Methods

| Method | Type | Description |
|--------|------|-------------|
| get_scenario | Read | Returns the current scenario |
| get_scores | Read | Returns all player scores |
| get_leaderboard | Read | Returns the leaderboard |
| submit_action | Write | Submit your response to be scored |
| advance_round | Write | Move to next scenario (owner only) |
| reset_game | Write | Reset the game (owner only) |

---

## How to Deploy Your Own Copy

1. Go to studio.genlayer.com
2. Create a new contract and paste the code from ChronicleQuest.py
3. Click Deploy - no constructor parameters needed
4. Copy your contract address once deployed
5. Update the CONTRACT variable in index.html with your new address

---

## Tech Stack

- Smart Contract: Python on GenLayer
- AI Judging: GenLayer gl.nondet.exec_prompt() with Equivalence Principle consensus
- Frontend: Plain HTML, CSS, JavaScript
- Hosting: Netlify

---

## Built By

DC - built using GenLayer Intelligent Contracts.

Read the full build story on Medium.
https://medium.com/@Alice501/how-i-built-an-ai-judged-survival-game-on-genlayer-873ed2e780dc
