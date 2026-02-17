from flask import Flask, render_template, request, jsonify
from data import TALKS, EVENT_INFO
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', event=EVENT_INFO, talks=TALKS)

@app.route('/api/talks')
def get_talks():
    search_query = request.args.get('q', '').lower()
    filtered_talks = []
    
    if not search_query:
        return jsonify(TALKS)

    for talk in TALKS:
        # Check title
        if search_query in talk['title'].lower():
            filtered_talks.append(talk)
            continue
        
        # Check category
        if search_query in talk['category'].lower():
            filtered_talks.append(talk)
            continue
            
        # Check speakers
        speaker_match = False
        for speaker in talk['speakers']:
            full_name = f"{speaker['first_name']} {speaker['last_name']}".lower()
            if search_query in full_name:
                speaker_match = True
                break
        
        if speaker_match:
            filtered_talks.append(talk)
            
    return jsonify(filtered_talks)

if __name__ == '__main__':
    # Use 0.0.0.0 to make it accessible if needed, but localhost is fine for dev
    app.run(debug=True, port=5000)
