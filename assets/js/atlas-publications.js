(() => {
  const archive = document.querySelector(".paper-archive");
  if (!archive) return;
  const form = archive.querySelector(".paper-filters");
  const query = form.elements.query;
  const yearSelect = form.elements.year;
  const status = archive.querySelector(".paper-count");

  function words(text) {
    return (
      text
        .toLowerCase()
        .normalize("NFKD")
        .replace(/\p{M}/gu, "")
        .match(/[\p{L}\p{N}]+/gu) || []
    );
  }

  const groups = Array.from(archive.querySelectorAll(".paper-list > ol"), (list) => {
    const heading = list.previousElementSibling;
    const year = heading.textContent.trim();
    yearSelect.add(new Option(year, year));
    const papers = Array.from(list.children, (item) => {
      const details = item.querySelectorAll("h3, .paper-authors, .paper-venue, .paper-venue-abbr");
      const text = Array.from(details, (part) => part.textContent.trim()).join(" ");
      const repositoryName = item.querySelector(".paper-code")?.pathname.split("/").pop() || "";
      return { item, terms: words(text + " " + repositoryName) };
    });
    return { list, heading, year, papers };
  });

  function filter() {
    const wanted = words(query.value);
    let total = 0;
    for (const { list, heading, year, papers } of groups) {
      const includesYear = !yearSelect.value || yearSelect.value === year;
      let count = 0;
      for (const { item, terms } of papers) {
        const matches = includesYear && wanted.every((word) => terms.some((term) => term.startsWith(word)));
        item.hidden = !matches;
        if (matches) count++;
      }
      list.hidden = heading.hidden = count === 0;
      total += count;
    }
    status.textContent = total ? total + (total === 1 ? " publication" : " publications") : "No matches. Try another search or clear the filters.";
  }

  query.addEventListener("input", filter);
  yearSelect.addEventListener("change", filter);
  form.addEventListener("submit", (event) => event.preventDefault());
  form.addEventListener("reset", (event) => {
    event.preventDefault();
    query.value = "";
    yearSelect.value = "";
    filter();
    query.focus();
  });
  form.hidden = false;
  filter();
})();
