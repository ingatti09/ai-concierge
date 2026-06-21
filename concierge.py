import json

with open("knowledge_base.json", "r", encoding="utf8") as f:
    kb = json.load(f)


def rispondi(domanda):

    domanda = domanda.lower()

    for chiave, risposta in kb.items():

        if chiave in domanda:
            return risposta

    return "Mi dispiace, non dispongo di questa informazione."