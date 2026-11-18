---
layout: atlas
permalink: /publications/
title: Publications
description: Peer-reviewed publications, ordered by year.
atlas_css: /assets/css/atlas-publications.css
atlas_js: /assets/js/atlas-publications.js
nav: true
nav_order: 2
---

<section class="paper-archive" aria-labelledby="publication-title">
  <header class="paper-intro">
    <h1 id="publication-title">Publications</h1>
    <a href="https://scholar.google.com/citations?user={{ site.scholar_userid | escape }}">Google Scholar <span aria-hidden="true">↗</span></a>
  </header>
  <form class="paper-filters" role="search" aria-label="Search publications" hidden>
    <label>Search publications
      <input type="search" name="query" placeholder="Title, author or venue">
    </label>
    <label>Year
      <select name="year"><option value="">All years</option></select>
    </label>
    <button type="reset">Clear</button>
  </form>
  <p class="paper-count" role="status" aria-live="polite">{% bibliography_count %} publications</p>
  <div class="paper-list">
    {% bibliography --template atlas-bib %}
  </div>
</section>
