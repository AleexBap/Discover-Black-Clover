from flask import Flask, render_template, request, jsonify
import random

from personagens import (
    PERSONAGENS, CARACTERISTICAS, NOMES_EXIBIDOS,
    comparar, procurar, obter_personagem, valor_bonito,
)

app = Flask(__name__)

jogos = {}

DICA1_APOS = 7
DICA2_APOS = 14


@app.route("/")
def index():
    return render_template(
        "index.html",
        caracteristicas=[{"campo": c, "nome": NOMES_EXIBIDOS[c]} for c in CARACTERISTICAS],
        total_personagens=len(PERSONAGENS),
        dica1_apos=DICA1_APOS,
        dica2_apos=DICA2_APOS,
    )


@app.route("/novo_jogo", methods=["POST"])
def novo_jogo():
    sid = request.json["sid"]
    secreto = random.choice(PERSONAGENS)
    jogos[sid] = {
        "secreto": secreto["nome"],
        "tentativas": [],
    }
    return jsonify({"ok": True})


@app.route("/procurar")
def buscar():
    termo = request.args.get("q", "")
    sid = request.args.get("sid", "")
    resultados = procurar(termo)

    jogo = jogos.get(sid)
    if jogo:
        tentados = set(jogo["tentativas"])
        resultados = [n for n in resultados if n not in tentados]

    return jsonify({"resultados": resultados})


@app.route("/tentativa", methods=["POST"])
def tentativa():
    data = request.json
    sid = data.get("sid")
    nome = data.get("nome")

    jogo = jogos.get(sid)
    if not jogo:
        return jsonify({"erro": "Jogo não iniciado"}), 400

    palpite = obter_personagem(nome)
    secreto = obter_personagem(jogo["secreto"])
    if not palpite:
        return jsonify({"erro": "Personagem inválido"}), 400

    if nome in jogo["tentativas"]:
        return jsonify({"erro": "Já tentaste esse personagem"}), 400

    jogo["tentativas"].append(nome)
    resultado = comparar(palpite, secreto)
    venceu = (nome == jogo["secreto"])
    num = len(jogo["tentativas"])

    resposta = {
        "resultado": resultado,
        "venceu": venceu,
        "num_tentativas": num,
    }
    if venceu:
        resposta["secreto"] = jogo["secreto"]
    return jsonify(resposta)


@app.route("/dica/<int:numero>", methods=["POST"])
def pedir_dica(numero):
    """
    Dicas gerais automáticas:
    - Dica 1: estado (vivo/morto)
    - Dica 2: esquadrão a que pertence
    """
    data = request.json
    sid = data.get("sid")

    jogo = jogos.get(sid)
    if not jogo:
        return jsonify({"erro": "Jogo não iniciado"}), 400

    if numero not in (1, 2):
        return jsonify({"erro": "Dica inválida"}), 400

    num_tentativas = len(jogo["tentativas"])
    limite = DICA1_APOS if numero == 1 else DICA2_APOS

    if num_tentativas < limite:
        faltam = limite - num_tentativas
        return jsonify({
            "erro": f"Ainda faltam {faltam} tentativas erradas para desbloquear esta dica."
        }), 403

    secreto = obter_personagem(jogo["secreto"])

    if numero == 1:
        texto = f"O estado deste personagem é: {valor_bonito(secreto['estado'])}."
    else:
        texto = f"Este personagem pertence ao esquadrão: {valor_bonito(secreto['esquadrao'])}."

    return jsonify({"texto": texto})


if __name__ == "__main__":
    app.run(debug=True)