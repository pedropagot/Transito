
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', '').strip()
    number = data.get('phone', '')

    resposta = ""

    if message == "1":
        resposta = "📍 Possui inscrição estadual no Estado do Maranhão?\n[1] Sim\n[2] Não"
    elif message == "2":
        resposta = ("❗ Não podemos atender a sua solicitação.\n\n"
                    "Este canal de comunicação é exclusivo para tratar de mercadorias em trânsito "
                    "retidas em postos fiscais do Estado.\n\n"
                    "Para demais informações e solicitações, procure uma unidade da Sefaz-MA:\n"
                    "https://sistemas1.sefaz.ma.gov.br/portalsefaz/jsp/pagina/pagina.jsf?codigo=1585")
    elif message == "1-1":
        resposta = "🔢 Por favor, digite o número da sua Inscrição Estadual no Estado do Maranhão:"
    elif message == "1-2":
        resposta = "🔢 Por favor, digite o número do CNPJ ou CPF do responsável pela mercadoria:"
    else:
        resposta = ("📝 Por favor, relate brevemente a situação e, se necessário, "
                    "envie os documentos relacionados (NFe, CTe, MDFe, etc.).\n\n"
                    "📨 Obrigado pelas informações. Seu atendimento foi encaminhado para análise da equipe interna.\n"
                    "Em breve, um atendente entrará em contato para dar continuidade ao atendimento.")

    return jsonify({"answer": resposta})

if __name__ == '__main__':
    app.run(port=5000)
