---
layout: atlas
title: News
permalink: /news/
description: Research announcements and publication updates, by posting date.
atlas_css: /assets/css/atlas-resources.css
---

<section class="resources-archive" aria-labelledby="news-heading">
  <header class="resources-heading">
    <h1 id="news-heading">News</h1>
    <p>{{ page.description }}</p>
  </header>
  <div class="updates-list">
    {% assign updates = site.news | sort: 'date' | reverse %}
    {% for item in updates %}
      <article class="updates-item" id="{{ item.slug | escape }}">
        <time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: '%d %b %Y' }}</time>
        <div>
          <h2><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a></h2>
          <div class="updates-copy">{{ item.content | markdownify }}</div>
        </div>
      </article>
    {% endfor %}
  </div>
</section>
