from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Return your student number in properly formatted JSON
    return jsonify({"student_number": "200604560"}), 200

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    # Extract the intent name from the request
    intent_name = req.get('queryResult', {}).get('intent', {}).get('displayName', '')

    # Initialize an empty response text
    response_text = "I'm not sure how to help with that."

    # Determine the appropriate response based on the intent
    if intent_name == "Special Offers":
        response_text = "Check out our special offer: Get 20% off on all custom mugs with code MUGLOVE20!"
    elif intent_name == "Product Inquiry":
        response_text = "We offer a wide range of products for customization, including t-shirts, mugs, and phone cases."
    elif intent_name == "Order Status":
        response_text = "Please provide your order number, and I'll check the status for you."
    # Add more elif statements here for other intents as needed

    # Construct the fulfillment response to send back to Dialogflow
    response = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        We are offering a 20% discount on all items until April 5th, 2024
                    ]
                }
            }
        ]
    }

    return jsonify(response), 200

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)  # Set debug=False for production
