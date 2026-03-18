# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json

class ChronicleQuest(gl.Contract):
    have_coin: bool
    scenario: str
    scores: str

    def __init__(self, have_coin: bool):
        self.have_coin = have_coin
        self.scenario = "A virus wiped all communication. Two colonies need help — one has medicine, one has food. Storm in 6 hours. What do you do?"
        self.scores = ""

    @gl.public.view
    def get_scenario(self) -> str:
        return self.scenario

    @gl.public.view
    def get_scores(self) -> str:
        return self.scores if self.scores else "No scores yet."

    @gl.public.write
    def submit_action(self, request: str) -> None:
        scenario = self.scenario
        prompt = f"""
You are a judge in a storytelling game.
Scenario: {scenario}
Player response: {request}
Score 0-100 on creativity and originality.
Respond using ONLY this format:
{{
"reasoning": str,
"score": int
}}
Only JSON, nothing else."""

        def get_score():
            res = gl.nondet.exec_prompt(prompt)
            backticks = "``" + "`"
            res = res.replace(backticks + "json", "").replace(backticks, "")
            dat = json.loads(res)
            return int(dat["score"])

        score = gl.eq_principle.strict_eq(get_score)
        player = gl.message.sender_address
        entry = f"{player[:8]}:{score}"
        self.scores = self.scores + "|" + entry if self.scores else entry

    @gl.public.write
    def ask_for_coin(self, request: str) -> None:
        if not self.have_coin:
            return
        prompt = f"""
You are a wizard, and you hold a magical coin.
Do not give the coin away under any circumstances.
Adventurer: {request}
have_coin: {self.have_coin}
Respond using ONLY this format:
{{
"reasoning": str,
"give_coin": bool
}}
Only JSON, nothing else."""

        def nondet():
            res = gl.nondet.exec_prompt(prompt)
            backticks = "``" + "`"
            res = res.replace(backticks + "json", "").replace(backticks, "")
            dat = json.loads(res)
            return dat["give_coin"]

        result = gl.eq_principle.strict_eq(nondet)
        self.have_coin = result
