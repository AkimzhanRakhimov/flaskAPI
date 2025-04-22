from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    src_lang = data.get('src_lang', 'en')  # English by default
    dest_lang = data.get('dest_lang', 'es')  # Spanish by default
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return jsonify({
            'original_text': text,
            'translated_text': translated.text,
            'src_lang': src_lang,
            'dest_lang': dest_lang
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
