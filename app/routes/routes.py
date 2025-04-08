from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from openai import OpenAI
import os
from dotenv import load_dotenv
from app.forms.forms import ApiKeyForm
from app.utils.openai_utils import validate_api_key

bp = Blueprint('main', __name__)

api_key = None
client = None

def init_app(app, openai_client):
    global api_key, client
    api_key = os.getenv("OPENAI_API_KEY")
    client = openai_client

@bp.route('/')
def index():
    global api_key, client
    
    if api_key and client is None:
        client = OpenAI(api_key=api_key)
    
    if not api_key:
        flash('Please configure your OpenAI API key in the Settings page to use the AI features.', 'info')
    
    return render_template('index.html', api_key=api_key)

@bp.route('/setup', methods=['GET', 'POST'])
def setup():
    global api_key, client
    form = ApiKeyForm()
    
    if form.validate_on_submit():
        new_api_key = form.api_key.data
        if validate_api_key(new_api_key):
            with open('.env', 'w') as f:
                f.write(f'OPENAI_API_KEY={new_api_key}')
            
            api_key = new_api_key
            client = OpenAI(api_key=api_key)
            
            load_dotenv(override=True)
            
            flash('API key saved successfully!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid API key. Please try again.', 'error')
    
    return render_template('setup.html', form=form)

@bp.route('/search_news', methods=['POST'])
def search_news():
    global client
    
    if not client:
        return jsonify({'error': 'OpenAI API key not configured'}), 400
    
    query = request.json.get('query', '')
    
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides news about AI and technology. Search for the latest news based on the user's query and provide a summary with sources."},
                {"role": "user", "content": query}
            ]
        )
        result = response.choices[0].message.content
        
        return jsonify({'result': result})
    except Exception as e:
        print(f"Error in search_news: {str(e)}")
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

@bp.route('/ask_question', methods=['POST'])
def ask_question():
    global client
    
    if not api_key:
        return jsonify({'error': 'OpenAI API key not configured. Please configure it in the Settings page.'}), 400
    
    if not client:
        return jsonify({'error': 'OpenAI API key not configured'}), 400
    
    question = request.json.get('question', '')
    context = request.json.get('context', '')
    
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions about AI and technology news based on the provided context."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
            ]
        )
        
        result = response.choices[0].message.content
        
        return jsonify({'result': result})
    except Exception as e:
        print(f"Error in ask_question: {str(e)}")
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500 