from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Crear la aplicación Flask
app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    # Leer el mensaje entrante enviado por Twilio
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Respuestas básicas del chatbot
    if 'hola' in incoming_msg:
        msg.body("¡Hola! Bienvenido a Sora Spa. ¿Cómo puedo ayudarte?\n1. Horarios\n2. Ubicación\n3. Servicios")
    elif '1' in incoming_msg:
        msg.body("Nuestros horarios son de lunes a viernes de 9:00 a 18:00.")
    elif '2' in incoming_msg:
        msg.body("Estamos ubicados en Pasaje Roma 69, Frutillar.")
    elif '3' in incoming_msg:
        msg.body("En Sora Spa ofrecemos servicios de relajación, masajes y bienestar. ¡Contáctanos para más información!")
    else:
        msg.body("Lo siento, no entendí tu mensaje. Por favor, intenta nuevamente enviando 'hola' para ver las opciones.")

    return str(resp)

if __name__ == "__main__":
    # Ejecutar la aplicación Flask
    app.run(host='0.0.0.0', port=5000, debug=True)

