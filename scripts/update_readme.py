from datetime import datetime

README_PATH = "README.md"

content = f"""
# 🚀 Code Masheen

**Building scalable digital products & automation solutions**

🌐 Website: https://www.codemasheen.in  
📅 Last updated: {datetime.utcnow().strftime('%d %b %Y, %H:%M UTC')}

---

## 🏢 About Us

**Code Masheen** is a technology-driven company focused on:
- ⚙️ Automation & backend systems
- 🧠 Scalable software architectures
- 🌐 Web & API development
- 📊 Data-driven engineering solutions

We create and maintain **multiple production-grade projects** for startups and enterprises.

---

## 🛠️ Tech Stack

- Python, Node.js
- FastAPI, Django
- PostgreSQL, MongoDB
- Docker, GitHub Actions
- AWS, CI/CD Automation

---

## 📌 Recent GitHub Activity
<!--START_SECTION:activity-->
<!--END_SECTION:activity-->

---

✨ _Engineering with precision. Scaling with purpose._
"""

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("README updated successfully")


# import os
# import requests
# import re
# from datetime import datetime

# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# USERNAME = os.getenv("USERNAME")

# HEADERS = {
#     "Accept": "application/vnd.github+json",
# }

# if GITHUB_TOKEN:
#     HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


# def get_repos():
#     url = f"https://api.github.com/users/{USERNAME}/repos?per_page=50&sort=pushed"
#     res = requests.get(url, headers=HEADERS)
#     if res.status_code != 200:
#         return []
#     return res.json()


# def get_repo_languages(repo_name):
#     url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/languages"
#     res = requests.get(url, headers=HEADERS)
#     if res.status_code != 200:
#         return {}
#     return res.json()


# def generate_featured_projects():
#     repos = get_repos()

#     repos = [
#         r for r in repos
#         if not r.get("fork")
#         and not r.get("archived")
#         and r.get("description")
#     ]

#     repos = sorted(
#         repos,
#         key=lambda r: (r["stargazers_count"], r["forks_count"]),
#         reverse=True
#     )[:6]

#     output = ""
#     for r in repos:
#         output += f"""
# ### [{r['name']}]({r['html_url']})
# {r['description']}

# ⭐ Stars: **{r['stargazers_count']}**  
# 🔱 Forks: **{r['forks_count']}**  
# 💻 Language: **{r['language'] or 'Multiple'}**

# ---
# """
#     return output.strip()


# def generate_tech_stack():
#     repos = get_repos()
#     language_totals = {}

#     for r in repos:
#         if r.get("fork"):
#             continue
#         languages = get_repo_languages(r["name"])
#         for lang, size in languages.items():
#             language_totals[lang] = language_totals.get(lang, 0) + size

#     top_languages = sorted(
#         language_totals.items(),
#         key=lambda x: x[1],
#         reverse=True
#     )[:10]

#     badges = "<p align=\"center\">\n"
#     for lang, _ in top_languages:
#         badges += (
#             f"<img src=\"https://img.shields.io/badge/"
#             f"{lang}-black?style=for-the-badge&logo={lang.lower()}&logoColor=white\" />\n"
#         )
#     badges += "</p>"

#     return badges


# def update_readme():
#     with open("README.md", "r", encoding="utf-8") as f:
#         content = f.read()

#     content = re.sub(
#         r"<!--START_SECTION:repos-->.*?<!--END_SECTION:repos-->",
#         f"<!--START_SECTION:repos-->\n{generate_featured_projects()}\n<!--END_SECTION:repos-->",
#         content,
#         flags=re.S
#     )

#     content = re.sub(
#         r"<!--START_SECTION:tech-stack-->.*?<!--END_SECTION:tech-stack-->",
#         f"<!--START_SECTION:tech-stack-->\n{generate_tech_stack()}\n<!--END_SECTION:tech-stack-->",
#         content,
#         flags=re.S
#     )

#     timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
#     content = re.sub(
#         r"<!--START_SECTION:update_time-->.*?<!--END_SECTION:update_time-->",
#         f"<!--START_SECTION:update_time-->{timestamp}<!--END_SECTION:update_time-->",
#         content,
#         flags=re.S
#     )

#     with open("README.md", "w", encoding="utf-8") as f:
#         f.write(content)

#     print("✅ README updated successfully")


# if __name__ == "__main__":
#     update_readme()
