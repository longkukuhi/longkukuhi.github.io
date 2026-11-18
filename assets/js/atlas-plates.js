(() => {
  const menu = document.querySelector(".plate-menu");
  const controls = [...menu.querySelectorAll("[data-plate]")];
  const panels = controls.map((control) => document.getElementById(control.dataset.plate));

  function selectPanel(fragment) {
    const selected = controls.find((control) => control.hash === fragment) || controls[0];
    controls.forEach((control, index) => {
      const active = control === selected;
      if (active) control.setAttribute("aria-current", "true");
      else control.removeAttribute("aria-current");
      panels[index].hidden = !active;
    });
  }

  controls.forEach((control) => {
    control.addEventListener("click", (event) => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      selectPanel(control.hash);
      if (location.hash !== control.hash) history.pushState(null, "", control.hash);
    });
  });
  window.addEventListener("hashchange", () => selectPanel(location.hash));
  window.addEventListener("popstate", () => selectPanel(location.hash));
  selectPanel(location.hash);
})();
