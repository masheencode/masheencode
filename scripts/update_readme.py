import os
import requests
from datetime import datetime
import re

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
USERNAME = os.environ.get('USERNAME')

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_user_repos():
    """Fetch user's repositories"""
    url = f'https://api.github.com/users/{USERNAME}/repos?sort=updated&per_page=100'
    response = requests.get(url, headers=headers)
    return response.json()

def get_repo_languages(repo_name):
    """Get languages used in a repository"""
    url = f'https://api.github.com/repos/{USERNAME}/{repo_name}/languages'
    response = requests.get(url, headers=headers)
    return response.json()

def generate_featured_projects():
    """Generate featured projects section"""
    repos = get_user_repos()
    
    featured = [r for r in repos if not r['fork'] and r['stargazers_count'] >= 0]
    featured = sorted(featured, key=lambda x: x['stargazers_count'], reverse=True)[:6]
    
    content = ""
    for repo in featured:
        name = repo['name']
        description = repo['description'] or 'No description available'
        stars = repo['stargazers_count']
        forks = repo['forks_count']
        language = repo['language'] or 'Unknown'
        url = repo['html_url']
        
        content += f"""
### [{name}]({url})
{description}

![Stars](https://img.shields.io/badge/⭐_Stars-{stars}-yellow?style=flat-square)
![Forks](https://img.shields.io/badge/🔱_Forks-{forks}-blue?style=flat-square)
![Language](https://img.shields.io/badge/💻_Language-{language}-green?style=flat-square)

---
"""
    return content

def generate_tech_stack():
    """Generate technology stack from all repositories"""
    repos = get_user_repos()
    all_languages = {}
    
    for repo in repos:
        if not repo['fork']:
            languages = get_repo_languages(repo['name'])
            for lang, bytes_count in languages.items():
                all_languages[lang] = all_languages.get(lang, 0) + bytes_count
    
    sorted_langs = sorted(all_languages.items(), key=lambda x: x[1], reverse=True)[:10]
    
    content = "<p align=\"center\">\n"
    
    lang_colors = {
        'JavaScript': 'F7DF1E', 'Python': '3776AB', 'TypeScript': '3178C6',
        'Java': '007396', 'Go': '00ADD8', 'Rust': '000000',
        'C++': '00599C', 'C': 'A8B9CC', 'Ruby': 'CC342D',
        'PHP': '777BB4', 'Swift': 'FA7343', 'Kotlin': '0095D5',
        'HTML': 'E34F26', 'CSS': '1572B6', 'Shell': '89e051'
    }
    
    for lang, _ in sorted_langs:
        color = lang_colors.get(lang, '808080')
        content += f"  <img src=\"https://img.shields.io/badge/-{lang}-{color}?style=for-the-badge&logo={lang.lower()}&logoColor=white\" />\n"
    
    content += "</p>"
    return content

def update_readme():
    """Update README.md with dynamic content"""
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    
    projects_content = generate_featured_projects()
    readme = re.sub(
        r'<!--START_SECTION:repos-->.*?<!--END_SECTION:repos-->',
        f'<!--START_SECTION:repos-->\n{projects_content}\n<!--END_SECTION:repos-->',
        readme,
        flags=re.DOTALL
    )
    
    tech_stack = generate_tech_stack()
    readme = re.sub(
        r'<!--START_SECTION:tech-stack-->.*?<!--END_SECTION:tech-stack-->',
        f'<!--START_SECTION:tech-stack-->\n{tech_stack}\n<!--END_SECTION:tech-stack-->',
        readme,
        flags=re.DOTALL
    )
    
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    readme = re.sub(
        r'<!--START_SECTION:update_time-->.*?<!--END_SECTION:update_time-->',
        f'<!--START_SECTION:update_time-->{current_time}<!--END_SECTION:update_time-->',
        readme,
        flags=re.DOTALL
    )
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print("✅ README updated successfully!")

if __name__ == '__main__':
    update_readme()
