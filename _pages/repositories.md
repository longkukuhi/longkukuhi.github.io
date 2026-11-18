---
layout: atlas
permalink: /repositories/
title: Research code
description: Implementations and evaluation resources for my work on retrieval, robotic perception and visual recognition.
nav: true
nav_order: 4
atlas_css: /assets/css/atlas-resources.css
---

<section class="resources-archive" aria-labelledby="code-heading">
  <header class="resources-heading">
    <h1 id="code-heading">Research <em>code</em></h1>
    <p>{{ page.description }}</p>
  </header>
  <ul class="resources-grid" role="list">
    {% for repo in site.data.repositories.github_repos %}
      {% assign project_name = repo | split: '/' | last %}
      {% assign project = site.data.atlas_repositories[project_name] %}
      <li>
        {% if project.venue %}<p class="resources-venue">{{ project.venue }}</p>{% endif %}
        <h2><a href="https://github.com/{{ repo }}" aria-label="{{ project_name | escape }} on GitHub">{{ project_name | escape }} <span aria-hidden="true">↗</span></a></h2>
        {% if project.description %}<p class="resources-description">{{ project.description | escape }}</p>{% endif %}
        {% if project.paper %}
          <a class="resources-paper" href="{{ '/publications/' | relative_url }}#{{ project.paper }}" aria-label="{{ project_name | escape }} publication details">Publication details <span aria-hidden="true">→</span></a>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
</section>
