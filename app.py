from flask import Flask, render_template,request
import requests
from datetime import datetime, timezone
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/details")
def details():
    username= request.args.get('username','').strip()
    if not username:
        return render_template("homepage.html")
    
    user_response = requests.get(f"https://api.github.com/users/{username}")
    user_data=user_response.json()
    repo_count= user_data['public_repos']
    followers=user_data['followers']

    repo_response= requests.get(f"https://api.github.com/users/{username}/repos")
    repo_data=repo_response.json()
    languages=[repo['language'] for repo in repo_data]

    language_counts={}

    for lang in languages:
        if lang is None:
            continue
        if lang in language_counts:
            language_counts[lang]+=1
        else :
            language_counts[lang]=1

    top_language=max(language_counts, key=language_counts.get)

    now = datetime.now(timezone.utc)
    most_recent_push = None
    for repo in repo_data:
        pushed_at_str = repo['pushed_at']
        pushed_at_date = datetime.fromisoformat(pushed_at_str.replace('Z', '+00:00'))
        if most_recent_push is None or pushed_at_date > most_recent_push:
            most_recent_push = pushed_at_date

    is_active = False
    if most_recent_push:
        difference = now - most_recent_push
        is_active = difference.days < 90

    created_at_str=user_data['created_at']
    created_at_date = datetime.fromisoformat(created_at_str.replace('Z','+00:00'))

    now = datetime.now(timezone.utc)
    account_age_days = (now - created_at_date).days
    account_age_years = account_age_days // 365

    # if account_age_years>=1:
    #     account_age_display= f"{account_age_years} years on GitHub"
    # else :
    #     account_age_display= f"{account_age_days} days on Github"
    
    return render_template(
        'details.html',
        username=username,
        repo_count=repo_count,
        is_active =is_active, 
        languages= languages,
        followers=followers,
        top_language=top_language,
        language_counts=language_counts,
        account_age_days=account_age_days,
        account_age_years=account_age_years
        )

if __name__ == '__main__':
    app.run(debug=True)